#!/usr/bin/python3
import json
import os
import sys
import time
import zipfile

from requests.adapters import HTTPAdapter
from urllib3 import Retry

from reqs.itunes import *
from reqs.store import *
import argparse

import logging
from rich.logging import RichHandler
from rich.console import Console
import rich

rich.get_console().file = sys.stderr
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logger = logging.getLogger('main')

import requests

def get_zipinfo_datetime(timestamp=None):
    # Some applications need reproducible .whl files, but they can't do this without forcing
    # the timestamp of the individual ZipInfo objects. See issue #143.
    timestamp = int(timestamp or time.time())
    return time.gmtime(timestamp)[0:6]


def downloadFile(url, outfile):
    with requests.get(url, stream=True) as r:
        totalLen = int(r.headers.get('Content-Length', '0'))
        downLen = 0
        r.raise_for_status()
        with open(outfile, 'wb') as f:
            lastLen = 0
            for chunk in r.iter_content(chunk_size=1 * 1024 * 1024):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
                downLen += len(chunk)
                if totalLen and downLen - lastLen > totalLen * 0.05:
                    logger.info("Download progress: %3.2f%% (%5.1fM /%5.1fM)" % (
                    downLen / totalLen * 100, downLen / 1024 / 1024, totalLen / 1024 / 1024))
                    lastLen = downLen

    return outfile

class IPATool(object):
    def __init__(self):
        self.sess = requests.Session()

        retry_strategy = Retry(
            connect=4,
            read=2,
            total=8,
        )
        self.sess.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        self.sess.mount("http://", HTTPAdapter(max_retries=retry_strategy))

        self.appId = None
        # self.appInfo = None
        self.appVerId = None
        
        self.jsonOut = None
    
    def tool_main(self):
        commparser = argparse.ArgumentParser(description='IPATool-Python Commands.', add_help=False)
        subp = commparser.add_subparsers(dest='command', required=True)
        lookup_p = subp.add_parser('lookup')
        lookup_p.add_argument('--bundle-id', '-b', dest='bundle_id', required=True)
        lookup_p.add_argument('--country', '-c', dest='country', required=True)
        lookup_p.add_argument('--get-verid', dest='get_verid', action='store_true')
        lookup_p.set_defaults(func=self.handleLookup)

        def add_auth_options(p):
            auth_p = p.add_argument_group('Auth Options', 'Must specify either Apple ID & Password, or iTunes Server URL')
            appleid = auth_p.add_argument('--appleid', '-e')
            passwd = auth_p.add_argument('--password', '-p')
            itunessrv = auth_p.add_argument('--itunes-server', '-s', dest='itunes_server')

            ## Multiple hack here just to achieve (appleid & password) || itunes_server
            # p._optionals.conflict_handler = 'ignore'
            # p._optionals._handle_conflict_ignore = lambda *args: None
            auth_p = p.add_mutually_exclusive_group(required=True)
            auth_p._group_actions.append(appleid)
            auth_p._group_actions.append(itunessrv)

            auth_p = p.add_mutually_exclusive_group(required=True)
            auth_p._group_actions.append(passwd)
            auth_p._group_actions.append(itunessrv)

        down_p = subp.add_parser('download')
        add_auth_options(down_p)
        down_p.add_argument('--appId', '-i', dest='appId')
        down_p.add_argument('--appVerId', dest='appVerId')

        down_p.add_argument('--output-dir', '-o', dest='output_dir', default='.')
        down_p.set_defaults(func=self.handleDownload)

        his_p = subp.add_parser('historyver')
        his_p.add_argument('--appId', '-i', dest='appId')
        add_auth_options(his_p)
        his_p.set_defaults(func=self.handleHistoryVersion)

        parser = argparse.ArgumentParser(description='IPATool-Python.', parents=[commparser])
        parser.add_argument('--log-level', '-l', dest='log_level', default='info',
                            help='output level (default: info)')
        parser.add_argument('--json', dest='out_json', action='store_true',
                            help='output json in stdout (log will always be put into stderr)')
        
        # parse global flags & first comm's arguments
        args, rest = parser.parse_known_args()
        logging.getLogger().setLevel(args.log_level.upper())
        outJson = args.out_json

        while True:
            args.func(args)
            if not rest:
                break
            args, rest = commparser.parse_known_args(rest)

        if outJson and self.jsonOut:
            print(json.dumps(self.jsonOut, ensure_ascii=False))

    def _outputJson(self, obj):
        self.jsonOut = obj

    def handleLookup(self, args):
        logger.info('Looking up app in country %s with ID %s' % (args.country, args.bundle_id))
        iTunes = iTunesClient(self.sess)
        appInfos = iTunes.lookup(args.bundle_id, country=args.country)
        if appInfos.resultCount != 1:
            logger.fatal("Failed to find app in country %s with ID %s" % (args.country, args.bundle_id))
            return
        appInfo = appInfos.results[0]
        logger.info("Found app:\n\tName: %s\n\tVersion: %s\n\tappId: %s" % (appInfo.trackName, appInfo.version, appInfo.trackId))
        self.appId = appInfo.trackId
        # self.appInfo = appInfo

        ret = {
            "name": appInfo.trackName,
            "version": appInfo.version,
            "appId": appInfo.trackId,
        }

        if args.get_verid:
            logger.info("Retriving verId using iTunes webpage...")
            verId = iTunes.getAppVerId(self.appId, args.country)
            logger.info("Got current verId using iTunes webpage: %s" % verId)
            ret["appVerId"] = verId

        self._outputJson(ret)

    def _get_StoreClient(self, args):
        Store = StoreClient(self.sess)

        if args.itunes_server:
            logger.info("Using iTunes interface %s to download app!" % args.itunes_server)
            servUrl = args.itunes_server
            def handle_iTunes_provider(url):
                r = requests.get(servUrl, params={
                    'url': url
                })
                ret = r.json()
                kbsync = bytes.fromhex(ret.pop('kbsync'))
                guid = ret.pop('guid')
                retHdrs = ret.pop('headers')
                return {
                    'headers': retHdrs,
                    'kbsync': kbsync,
                    'guid': guid,
                }
            Store.iTunes_provider = handle_iTunes_provider
        else:
            appleid = args.appleid
            applepass = args.password

            logger.info("Logging into iTunes...")

            if appleid.lower() == 'itunes':
                logger.info("Using iTunes interface to download app!")
                Store.authenticate(appleid, applepass)
            else:
                Store.authenticate(appleid, applepass)
            logger.info('Logged in as %s' % Store.accountName)
        return Store

    def _handleStoreException(self, _e):
        e = _e # type: StoreException
        logger.fatal("Store %s failed! Message: %s%s" % (e.req, e.errMsg, " (errorType %s)" % e.errType if e.errType else ''))
        logger.fatal("    Raw Response: %s" % (e.resp.as_dict()))

    def handleHistoryVersion(self, args):
        if args.appId:
            self.appId = args.appId

        if not self.appId:
            logger.fatal("appId not supplied!")
            return

        logger.info('Retriving history version for appId %s' % self.appId)

        try:
            Store = self._get_StoreClient(args)

            logger.info('Retriving download info for appId %s' % (self.appId))
            downResp = Store.download(self.appId)
            
            if not downResp.songList:
                logger.fatal("failed to get app download info!")
                raise StoreException('download', downResp, 'no songList')
            downInfo = downResp.songList[0]
            logger.info('Got available version ids %s', downInfo.metadata.softwareVersionExternalIdentifiers)
            self._outputJson({
                "appVerIds": downInfo.metadata.softwareVersionExternalIdentifiers
            })
        except StoreException as e:
            self._handleStoreException(e)

    def handleDownload(self, args):
        if args.appId:
            self.appId = args.appId
        if args.appVerId:
            self.appVerId = args.appVerId

        if not self.appId:
            logger.fatal("appId not supplied!")
            return
        
        try:
            appleid = args.appleid
            Store = self._get_StoreClient(args)
            
            logger.info('Retriving download info for appId %s%s' % (self.appId, " with versionId %s" % self.appVerId if self.appVerId else ""))

            downResp = Store.download(self.appId, self.appVerId)
            
            if not downResp.songList:
                logger.fatal("failed to get app download info!")
                raise StoreException('download', downResp, 'no songList')
            downInfo = downResp.songList[0]

            appName = downInfo.metadata.bundleDisplayName
            appId = downInfo.songId
            appBundleId = downInfo.metadata.softwareVersionBundleId
            appVerId = downInfo.metadata.softwareVersionExternalIdentifier
            appVer = downInfo.metadata.bundleShortVersionString

            logger.info(f'Downloading app {appName} ({appBundleId}) with appId {appId} (version {appVer}, versionId {appVerId})')

            # if self.appInfo:
            filename = '%s-%s-%s-%s.ipa' % (appBundleId,
                                            appVer,
                                            appId,
                                            appVerId)
            # else:
            #     filename = '%s-%s.ipa' % (self.appId, appVerId)

            filepath = os.path.join(args.output_dir, filename)
            logger.info("Downloading ipa to %s" % filepath)
            downloadFile(downInfo.URL, filepath)
            with zipfile.ZipFile(filepath, 'a') as ipaFile:
                logger.info("Writing out iTunesMetadata.plist...")
                metadata = downInfo.metadata.as_dict()
                if appleid:
                    metadata["apple-id"] = appleid
                    metadata["userName"] = appleid
                ipaFile.writestr(zipfile.ZipInfo("iTunesMetadata.plist", get_zipinfo_datetime()), plistlib.dumps(metadata))

                appContentDir = [c for c in ipaFile.namelist() if c.startswith('Payload/') and len(c.strip('/').split('/')) == 2][0]
                appContentDir = appContentDir.rstrip('/')

                scManifestData = ipaFile.read(appContentDir + '/SC_Info/Manifest.plist')
                scManifest = plistlib.loads(scManifestData)

                sinfs = {c.id: c.sinf for c in downInfo.sinfs}
                for i, sinfPath in enumerate(scManifest['SinfPaths']):
                    ipaFile.writestr(appContentDir + '/' + sinfPath, sinfs[i])

            self._outputJson({
                "appName": appName,
                "appBundleId": appBundleId,
                "appVer": appVer,
                "appId": appId,
                "appVerId": appVerId,

                "downloadedIPA": filepath,
                "downloadedVerId": appVerId,
            })
        except StoreException as e:
            self._handleStoreException(e)

def main():
    tool = IPATool()

    tool.tool_main()

main()