#!/usr/bin/python3
import os
import pickle
import sys
import time
import zipfile

from requests.adapters import HTTPAdapter
from urllib3 import Retry

from reqs.itunes import *
from reqs.store import *
import reprlib

reprlib.aRepr.maxstring = 200

import argparse

import logging
from rich.logging import RichHandler
from rich.console import Console
import rich

rich.get_console().file = sys.stderr
if rich.get_console().width < 100:
    rich.get_console().width = 100

logging_handler = RichHandler(rich_tracebacks=True)
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[logging_handler]
)
logging.getLogger('urllib3').setLevel(logging.WARNING)
retryLogger = logging.getLogger('urllib3.util.retry')
retryLogger.setLevel(logging.DEBUG)
retryLogger.handlers = [logging_handler]
retryLogger.propagate = False

logger = logging.getLogger('main')

import requests

def get_zipinfo_datetime(timestamp=None):
    # Some applications need reproducible .whl files, but they can't do this without forcing
    # the timestamp of the individual ZipInfo objects. See issue #143.
    timestamp = int(timestamp or time.time())
    return time.gmtime(timestamp)[0:6]

def downloadFile(url, outfile, retries=10):
    for retry in range(retries):
        try:
            _downloadFile(url, outfile)
            break
        except Exception as e:
            logger.info("Error during downloading %s (retry %d/%d), error %s", url, retry, retries, e)
            os.remove(outfile)
    logger.info("Download success in retry %d", retry)

download_sess = requests.Session()
download_sess.headers = {"User-Agent": CONFIGURATOR_UA}
DOWNLOAD_READ_TIMEOUT = 25.0
def _downloadFile(url, outfile):
    with download_sess.get(url, stream=True, timeout=DOWNLOAD_READ_TIMEOUT) as r:
        if not r.headers.get('Content-Length'):
            raise Exception("server is not returning Content-Length!")
        totalLen = int(r.headers.get('Content-Length', '0'))
        downLen = 0
        r.raise_for_status()
        try:
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
        finally:
            if downLen != totalLen: # ensure no partial downloaded files exists
                os.unlink(outfile)
        if downLen != totalLen:
            raise Exception("failed to completely download the IPA file")

    return outfile

class IPATool(object):
    def __init__(self):
        self.sess = requests.Session()

        retry_strategy = Retry(
            connect=4,
            read=4,
            # total=8,
            status=20,
            allowed_methods=None,
            status_forcelist=[429, 502, 503],
            backoff_factor=1.0,
            respect_retry_after_header=False,
        )
        self.sess.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        self.sess.mount("http://", HTTPAdapter(max_retries=retry_strategy))
        IPATOOL_PROXY = os.getenv("IPATOOL_PROXY")
        if IPATOOL_PROXY is not None:
            self.sess.proxies.update(
                {'http': IPATOOL_PROXY, 'https': IPATOOL_PROXY})
            # self.sess.headers = {}
            self.sess.headers = {"Connection": "close"}
            self.sess.keep_alive = False

        self.appId = None
        # self.appInfo = None
        self.appVerId = None
        self.appVerIds = None
        
        self.jsonOut = None
    
    def tool_main(self):
        commparser = argparse.ArgumentParser(description='IPATool-Python Commands.', add_help=False)
        subp = commparser.add_subparsers(dest='command', required=True)
        lookup_p = subp.add_parser('lookup')
        id_group = lookup_p.add_mutually_exclusive_group(required=True)
        id_group.add_argument('--bundle-id', '-b', dest='bundle_id')
        id_group.add_argument('--appId', '-i', dest='appId')
        lookup_p.add_argument('--country', '-c', dest='country', required=True)
        lookup_p.add_argument('--get-verid', dest='get_verid', action='store_true')
        lookup_p.set_defaults(func=self.handleLookup)

        def add_auth_options(p):
            auth_p = p.add_argument_group('Auth Options', 'Must specify either Apple ID & Password, or iTunes Server URL')
            appleid = auth_p.add_argument('--appleid', '-e')
            passwd = auth_p.add_argument('--password', '-p')
            sessdir = auth_p.add_argument('--session-dir', dest='session_dir', default=None)

            itunessrv = auth_p.add_argument('--itunes-server', '-s', dest='itunes_server')

            ## Multiple hack here just to achieve (appleid & password) || itunes_server
            # p._optionals.conflict_handler = 'ignore'
            # p._optionals._handle_conflict_ignore = lambda *args: None
            auth_p = p.add_mutually_exclusive_group(required=True)
            auth_p._group_actions.append(appleid)
            auth_p._group_actions.append(itunessrv)
            # auth_p._group_actions.append(sessdir)

            auth_p = p.add_mutually_exclusive_group(required=True)
            auth_p._group_actions.append(passwd)
            auth_p._group_actions.append(itunessrv)

        purchase_p = subp.add_parser('purchase')
        add_auth_options(purchase_p)
        purchase_p.add_argument('--appId', '-i', dest='appId')
        purchase_p.set_defaults(func=self.handlePurchase)

        down_p = subp.add_parser('download')
        add_auth_options(down_p)
        down_p.add_argument('--appId', '-i', dest='appId')
        down_p.add_argument('--appVerId', dest='appVerId')
        down_p.add_argument('--purchase', action='store_true')
        down_p.add_argument('--downloadAllVersion', action='store_true')
        down_p.add_argument('--output-dir', '-o', dest='output_dir', default='.')
        down_p.set_defaults(func=self.handleDownload)

        his_p = subp.add_parser('historyver')
        his_p.add_argument('--appId', '-i', dest='appId')
        his_p.add_argument('--purchase', action='store_true')
        his_p.add_argument('--output-dir', '-o', dest='output_dir', default='.')
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
        if args.bundle_id:
            s = 'BundleID %s' % args.bundle_id
        else:
            s = 'AppID %s' % args.appId
        logger.info('Looking up app in country %s with BundleID %s' % (args.country, s))
        iTunes = iTunesClient(self.sess)
        appInfos = iTunes.lookup(bundleId=args.bundle_id, appId=args.appId, country=args.country)
        if appInfos.resultCount != 1:
            logger.fatal("Failed to find app in country %s with %s" % (args.country, s))
            return
        appInfo = appInfos.results[0]
        logger.info("Found app:\n\tName: %s\n\tVersion: %s\n\tbundleId: %s\n\tappId: %s" % (appInfo.trackName, appInfo.version, appInfo.bundleId, appInfo.trackId))
        self.appId = appInfo.trackId
        # self.appInfo = appInfo

        ret = {
            "name": appInfo.trackName,
            "version": appInfo.version,
            "appId": appInfo.trackId,
            "bundleId": appInfo.bundleId,
        }

        if args.get_verid:
            logger.info("Retrieving verId using iTunes webpage...")
            verId = iTunes.getAppVerId(self.appId, args.country)
            logger.info("Got current verId using iTunes webpage: %s" % verId)
            ret["appVerId"] = verId

        self._outputJson(ret)

    storeClientCache = {}
    def _get_StoreClient(self, args):
        for k, v in self.storeClientCache.items():
            if time.time() - v < 30.0:
                return k
            else:
                del self.storeClientCache[k]

        newSess = pickle.loads(pickle.dumps(self.sess))
        Store = StoreClient(newSess)

        if args.itunes_server:
            logger.info("Using iTunes interface %s to download app!" % args.itunes_server)
            servUrl = args.itunes_server
            def handle_iTunes_provider(url):
                startTime = time.time()
                r = requests.get(servUrl, params={
                    'url': url
                })
                logger.debug("got itunes header in %.2f seconds", time.time() - startTime)

                ret = r.json()
                kbsync = bytes.fromhex(ret.pop('kbsync'))
                guid = ret.pop('guid')
                retHdrs = ret.pop('headers')
                handled = {
                    'headers': retHdrs,
                    'kbsync': kbsync,
                    'guid': guid,
                }
                if 'sbsync' in ret:
                    handled['sbsync'] = bytes.fromhex(ret.pop('sbsync'))
                if 'afds' in ret:
                    handled['afds'] = ret.pop('afds')
                return handled
            Store.iTunes_provider = handle_iTunes_provider
        else:
            appleid = args.appleid
            applepass = args.password

            needLogin = True
            session_cache = os.path.join(args.session_dir, args.appleid) if args.session_dir else None
            if session_cache and os.path.exists(session_cache):
                needLogin = False
                try:
                    # inside try in case the file format changed
                    with open(session_cache, "r") as f:
                        content = f.read()
                    Store.authenticate_load_session(content)
                except Exception as e:
                    logger.warning(f"Error loading session {session_cache}")
                    os.unlink(session_cache)
                    needLogin = True
                else:
                    logger.info('Loaded session for %s' % (str(Store.authInfo)))
            if needLogin:
                logger.info("Logging into iTunes as %s ..." % appleid)

                Store.authenticate(appleid, applepass)
                logger.info('Logged in as %s' % (str(Store.authInfo)))

                if session_cache:
                    with open(session_cache, "w") as f:
                        f.write(Store.authenticate_save_session())

            def authedPost(*args, **kwargs):
                if 'MZFinance.woa/wa/authenticate' in args[0]:
                    return Store.sess.original_post(*args, **kwargs)
                for i in range(3):
                    r = Store.sess.original_post(*args, **kwargs)
                    isAuthFail = False
                    try:
                        d = plistlib.loads(r.content)
                        if str(d['failureType']) in ("2034", "1008"):
                            isAuthFail = True
                    except:
                        return r
                    if not isAuthFail:
                        return r
                    Store.authenticate(appleid, applepass)
                    if session_cache:
                        with open(session_cache, "w") as f:
                            f.write(Store.authenticate_save_session())
                    continue
            Store.sess.original_post = Store.sess.post
            Store.sess.post = authedPost

        self.storeClientCache[Store] = time.time()
        return Store

    def _handleStoreException(self, _e):
        e = _e # type: StoreException
        logger.fatal("Store %s failed! Message: %s%s" % (e.req, e.errMsg, " (errorType %s)" % e.errType if e.errType else ''))
        logger.fatal("    Raw Response: %s" % (e.resp))

    def handlePurchase(self, args):
        Store = self._get_StoreClient(args)
        logger.info('Try to purchase appId %s' % (self.appId))
        try:
            Store.purchase(self.appId)
        except StoreException as e:
            if e.errMsg == 'purchased_before':
                logger.warning('You have already purchased appId %s before' % (self.appId))
            else:
                raise

    def handleHistoryVersion(self, args, caches=True):
        if args.appId:
            self.appId = args.appId

        if not self.appId:
            logger.fatal("appId not supplied!")
            return

        versionsJsonPath = args.output_dir + f"/historyver_{self.appId}.json"
        if caches:
            if os.path.exists(versionsJsonPath):
                cacheContent = None
                try:
                    with open(versionsJsonPath) as f:
                        cacheContent = json.load(f)
                except:
                    pass
                if cacheContent is not None:
                    logger.info('Loaded history version cache for appId %s' % self.appId)
                    self.appVerIds = cacheContent['appVerIds']
                    return

        logger.info('Retrieving history version for appId %s' % self.appId)

        try:
            Store = self._get_StoreClient(args)

            logger.info('Retrieving download info for appId %s' % (self.appId))
            if args.purchase:
                logger.info('Purchasing appId %s' % (self.appId))
                # We have already successfully purchased, so don't purchase again :)
                self.handlePurchase(args)
                args.purchase = False

            downResp = Store.download(self.appId, '', isRedownload=not args.purchase)
            logger.debug('Got download info: %s', downResp)
            if args.purchase:
                # We have already successfully purchased, so don't purchase again :)
                args.purchase = False

            if not downResp.songList:
                logger.fatal("failed to get app download info!")
                raise StoreException('download', downResp, 'no songList')
            downInfo = downResp.songList[0]
            logger.info('Got available version ids %s', downInfo.metadata.softwareVersionExternalIdentifiers)
            self._outputJson({
                "appVerIds": downInfo.metadata.softwareVersionExternalIdentifiers
            })
            self.appVerIds = downInfo.metadata.softwareVersionExternalIdentifiers
            if caches:
                with open(versionsJsonPath, 'w') as f:
                    json.dump({
                        'appVerIds': self.appVerIds,
                    }, f)
        except StoreException as e:
            self._handleStoreException(e)
            if not e.errMsg.startswith('http error status') and not e.errMsg.startswith(
                    'We are temporarily unable to process your request') and not e.errMsg.startswith(
                    "License not found"):
                # this error is persistent (e.g. app deleted)
                self.appVerIds = []
                if caches:
                    with open(versionsJsonPath, 'w') as f:
                        json.dump({
                            'appVerIds': self.appVerIds,
                            'error': str(e),
                            'errorResp': str(e.resp),
                        }, f)

    def handleDownload(self, args):
        os.makedirs(args.output_dir, exist_ok=True)
        if args.downloadAllVersion:
            if os.path.exists(args.output_dir + "/all_done"):
                logger.info('Already fully finished, skipping!')
                return
            self.handleHistoryVersion(args, caches=True)
            if not self.appVerIds:
                logger.fatal('failed to retrive history versions for appId %s', args.appId)
                return
            everything_succ = True
            for appVerId in self.appVerIds:
                self.jsonOut = None
                stateFile = args.output_dir + '/' + str(appVerId) + '.finish'
                if os.path.exists(stateFile):
                    logger.info('Skipping already downloaded')
                    continue
                try:
                    self.appVerId = appVerId
                    self.downloadOne(args)
                    if args.out_json and self.jsonOut:
                        print(json.dumps(self.jsonOut, ensure_ascii=False))
                    if self.jsonOut is not None:  # successfully finished
                        with open(stateFile, 'w') as f:
                            f.write('1')
                except Exception as e:
                    logger.fatal("error during downloading appVerId %s", appVerId, exc_info=1)
                    everything_succ = False
                finally:
                    self.jsonOut = None
            if everything_succ:
                with open(args.output_dir + "/all_done", 'w') as f:
                    f.write("1")
        else:
            self.downloadOne(args)

    def downloadOne(self, args):
        if args.appId:
            self.appId = args.appId
        if args.appVerId:
            self.appVerId = args.appVerId

        if not self.appId:
            logger.fatal("appId not supplied!")
            return
    
        logger.info("Downloading appId %s appVerId %s", self.appId, self.appVerId)
        try:
            appleid = args.appleid
            Store = self._get_StoreClient(args)

            if args.purchase:
                self.handlePurchase(args)
            
            logger.info('Retrieving download info for appId %s%s' % (self.appId, " with versionId %s" % self.appVerId if self.appVerId else ""))

            downResp = Store.download(self.appId, self.appVerId, isRedownload=not args.purchase)
            logger.debug('Got download info: %s', downResp.as_dict())
            
            if not downResp.songList:
                logger.fatal("failed to get app download info!")
                raise StoreException('download', downResp, 'no songList')
            downInfo = downResp.songList[0]

            appName = downInfo.metadata.bundleDisplayName
            appId = downInfo.songId
            appBundleId = downInfo.metadata.softwareVersionBundleId
            appVerId = downInfo.metadata.softwareVersionExternalIdentifier
            # when downloading history versions, bundleShortVersionString will always give a wrong version number (the newest one)
            # should use bundleVersion in these cases
            appVer = downInfo.metadata.bundleShortVersionString if not self.appVerId else downInfo.metadata.bundleVersion

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
            metadata = downInfo.metadata.as_dict()
            if appleid:
                metadata["apple-id"] = appleid
                metadata["userName"] = appleid
            logger.info("Writing out iTunesMetadata.plist...")
            if zipfile.is_zipfile(filepath):
                with zipfile.ZipFile(filepath, 'a') as ipaFile:
                    logger.debug("Writing iTunesMetadata.plist")
                    ipaFile.writestr(zipfile.ZipInfo("iTunesMetadata.plist", get_zipinfo_datetime()), plistlib.dumps(metadata))
                    logger.debug("Writing IPAToolInfo.plist")
                    ipaFile.writestr(zipfile.ZipInfo("IPAToolInfo.plist", get_zipinfo_datetime()), plistlib.dumps(downResp.as_dict()))

                    def findAppContentPath(c):
                        if not c.startswith('Payload/'):
                            return False
                        pathparts = c.strip('/').split('/')
                        if len(pathparts) != 2:
                            return False
                        if not pathparts[1].endswith(".app"):
                            return False
                        return True
                    appContentDirChoices = [c for c in ipaFile.namelist() if findAppContentPath(c)]
                    if len(appContentDirChoices) != 1:
                        raise Exception("failed to find appContentDir, choices %s", appContentDirChoices)
                    appContentDir = appContentDirChoices[0].rstrip('/')

                    processedSinf = False
                    if (appContentDir + '/SC_Info/Manifest.plist') in ipaFile.namelist():
                        #Try to get the Manifest.plist file, since it doesn't always exist.
                        scManifestData = ipaFile.read(appContentDir + '/SC_Info/Manifest.plist')
                        logger.debug("Got SC_Info/Manifest.plist: %s", scManifestData)
                        scManifest = plistlib.loads(scManifestData)
                        sinfs = {c.id: c.sinf for c in downInfo.sinfs}
                        if 'SinfPaths' in scManifest:
                            for i, sinfPath in enumerate(scManifest['SinfPaths']):
                                logger.debug("Writing sinf to %s", sinfPath)
                                ipaFile.writestr(appContentDir + '/' + sinfPath, sinfs[i])
                            processedSinf = True
                    if not processedSinf:
                        logger.info('Manifest.plist does not exist! Assuming it is an old app without one...')
                        infoListData = ipaFile.read(appContentDir + '/Info.plist') #Is this not loaded anywhere yet?
                        infoList = plistlib.loads(infoListData)
                        sinfPath = appContentDir + '/SC_Info/'+infoList['CFBundleExecutable']+".sinf"
                        logger.debug("Writing sinf to %s", sinfPath)
                        #Assuming there is only one .sinf file, hence the 0
                        ipaFile.writestr(sinfPath, downInfo.sinfs[0].sinf)
                        processedSinf = True

                logger.info("Downloaded ipa to %s" % filename)
            else:
                plist = filepath[:-4]+".info.plist"
                with open(plist, "wb") as f:
                    f.write(plistlib.dumps(downResp.as_dict()))
                plist = filepath[:-4]+".plist"
                with open(plist, "wb") as f:
                    f.write(plistlib.dumps(metadata))
                logger.info("Downloaded ipa to %s and plist to %s" % (filename, plist))

            self._outputJson({
                "appName": appName,
                "appBundleId": appBundleId,
                "appVer": appVer,
                "appId": appId,
                "appVerId": appVerId,

                "downloadedIPA": filepath,
                "downloadedVerId": appVerId,
                "downloadURL": downInfo.URL,
            })
        except StoreException as e:
            self._handleStoreException(e)

def main():
    tool = IPATool()
    tool.tool_main()

if __name__ == '__main__':
    main()