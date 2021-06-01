import plistlib
import requests
from reqs.schemas.store_authenticate_req import StoreAuthenticateReq
from reqs.schemas.store_authenticate_resp import StoreAuthenticateResp
from reqs.schemas.store_download_req import StoreDownloadReq
from reqs.schemas.store_download_resp import StoreDownloadResp

class StoreException(Exception):
    def __init__(self, req, errMsg, errType=None):
        self.req = req
        self.errMsg = errMsg
        self.errType = errType
        super().__init__(
            "Store %s error: %s" % (self.req, self.errMsg) if not self.errType else
            "Store %s error: %s, errorType: %s" % (self.req, self.errMsg, self.errType)
        )

class StoreClient(object):
    def __init__(self, sess: requests.Session, guid: str = '000C2941396B'):
        self.sess = sess
        self.guid = guid
        self.dsid = None
        self.storeFront = None
        self.accountName = None

    def authenticate(self, appleId, password):
        req = StoreAuthenticateReq(appleId=appleId, password=password, attempt='4', createSession="true", guid=self.guid, rmp='0', why='signIn')
        url = "https://p46-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/authenticate?guid=%s" % self.guid
        while True:
            r = self.sess.post(url,
                      headers={
                          "Accept": "*/*",
                          "Content-Type": "application/x-www-form-urlencoded",
                          "User-Agent": "Configurator/2.0 (Macintosh; OS X 10.12.6; 16G29) AppleWebKit/2603.3.8",
                      }, data=plistlib.dumps(req.as_dict()), allow_redirects=False)
            if r.status_code == 302:
                url = r.headers['Location']
                continue
            break
        resp = StoreAuthenticateResp.from_dict(plistlib.loads(r.content))
        if not resp.m_allowed:
            raise StoreException("authenticate", resp.customerMessage, resp.failureType)
        self.dsid = str(resp.download_queue_info.dsid)
        self.storeFront = r.headers.get('x-set-apple-store-front')
        self.accountName = resp.accountInfo.address.firstName + " " + resp.accountInfo.address.lastName
        return resp

    # ==> 🛠   [Verbose] Performing request: curl -k -X POST \
    # -H "iCloud-DSID: 12263680861" \
    # -H "Content-Type: application/x-www-form-urlencoded" \
    # -H "User-Agent: Configurator/2.0 (Macintosh; OS X 10.12.6; 16G29) AppleWebKit/2603.3.8" \
    # -H "X-Dsid: 12263680861" \
    # -d '<?xml version="1.0" encoding="UTF-8"?>
    # <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    # <plist version="1.0">
    # <dict>
    #         <key>creditDisplay</key>
    #         <string></string>
    #         <key>guid</key>
    #         <string>000C2941396B</string>
    #         <key>salableAdamId</key>
    #         <string>1239860606</string>
    # </dict>
    # </plist>
    # ' \
    # https://p25-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/volumeStoreDownloadProduct?guid=000C2941396Bk
    def download(self, appId, appVerId=""):
        req = StoreDownloadReq(creditDisplay="", guid=self.guid, salableAdamId=appId, appExtVrsId=appVerId)
        r = self.sess.post("https://p25-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/volumeStoreDownloadProduct",
                           params={
                               "guid": self.guid
                           },
                           headers={
                               "iCloud-DSID": self.dsid,
                               "Content-Type": "application/x-www-form-urlencoded",
                               "User-Agent": "Configurator/2.0 (Macintosh; OS X 10.12.6; 16G29) AppleWebKit/2603.3.8",
                               "X-Dsid": self.dsid,
                           }, data=plistlib.dumps(req.as_dict()))

        resp = StoreDownloadResp.from_dict(plistlib.loads(r.content))
        if resp.cancel_purchase_batch:
            raise StoreException("download", resp.customerMessage, resp.failureType)
        return resp