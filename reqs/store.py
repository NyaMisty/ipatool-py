import hashlib
import plistlib
import requests
from reqs.schemas.store_authenticate_req import StoreAuthenticateReq
from reqs.schemas.store_authenticate_resp import StoreAuthenticateResp
from reqs.schemas.store_buyproduct_req import StoreBuyproductReq
from reqs.schemas.store_buyproduct_resp import StoreBuyproductResp
from reqs.schemas.store_download_req import StoreDownloadReq
from reqs.schemas.store_download_resp import StoreDownloadResp

class StoreException(Exception):
    def __init__(self, req, resp, errMsg, errType=None):
        self.req = req
        self.resp = resp # type: StoreDownloadResp
        self.errMsg = errMsg
        self.errType = errType
        super().__init__(
            "Store %s error: %s" % (self.req, self.errMsg) if not self.errType else
            "Store %s error: %s, errorType: %s" % (self.req, self.errMsg, self.errType)
        )

#CONFIGURATOR_UA = "Configurator/2.0 (Macintosh; OS X 10.12.6; 16G29) AppleWebKit/2603.3.8"
CONFIGURATOR_UA = 'Configurator/2.0 (Macintosh; OS X 10.12.6; 16G29) AppleWebKit/2603.3.8 iOS/14.2 hwp/t8020'

class StoreClient(object):
    def __init__(self, sess: requests.Session, guid: str = None):
        self.sess = sess
        self.guid = guid # the guid will not be used in itunes server mode
        self.accountName = None
        self.iTunes_provider = None
        self.authHeaders = None

    def _generateGuid(self, appleId):
        '''
        Derive a GUID for an appleId. For each appleId, the GUID will always remain the same
        :param appleId:
        :return:
        '''
        DEFAULT_GUID = '000C2941396B'  # this GUID is blocked
        # number of chars to use from DEFAULT_GUID as prefix (0..12)
        GUID_DEFAULT_PREFIX = 2
        # something unique
        GUID_SEED = 'CAFEBABE'
        # something between 0 and 30
        GUID_POS = 10

        # generate a unique guid out of the appleId
        h = hashlib.sha1((GUID_SEED + appleId + GUID_SEED).encode("utf-8")).hexdigest()
        defaultPart = DEFAULT_GUID[:GUID_DEFAULT_PREFIX]
        hashPart = h[GUID_POS: GUID_POS + (len(DEFAULT_GUID) - GUID_DEFAULT_PREFIX)]
        guid = (defaultPart + hashPart).upper()
        return guid

    def authenticate(self, appleId, password):
        if not self.guid:
            self.guid = self._generateGuid(appleId)
        req = StoreAuthenticateReq(appleId=appleId, password=password, attempt='4', createSession="true", guid=self.guid, rmp='0', why='signIn')
        url = "https://p46-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/authenticate?guid=%s" % self.guid
        while True:
            r = self.sess.post(url,
                      headers={
                          "Accept": "*/*",
                          "Content-Type": "application/x-www-form-urlencoded",
                          "User-Agent": CONFIGURATOR_UA,
                      }, data=plistlib.dumps(req.as_dict()), allow_redirects=False)
            if r.status_code == 302:
                url = r.headers['Location']
                continue
            break
        d = plistlib.loads(r.content)
        resp = StoreAuthenticateResp.from_dict(d)
        if not resp.m_allowed:
            raise StoreException("authenticate", d, resp.customerMessage, resp.failureType)

        self.authHeaders = {}
        self.authHeaders['X-Dsid'] = self.sess.headers['iCloud-Dsid'] = str(resp.download_queue_info.dsid)
        self.authHeaders['X-Apple-Store-Front'] = r.headers.get('x-set-apple-store-front')
        self.authHeaders['X-Token'] = resp.passwordToken
        
        self.sess.headers = dict(self.authHeaders)
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
    def volumeStoreDownloadProduct(self, appId, appVerId=""):
        req = StoreDownloadReq(creditDisplay="", guid=self.guid, salableAdamId=appId, appExtVrsId=appVerId)
        hdrs = {
               "Content-Type": "application/x-www-form-urlencoded",
               "User-Agent": CONFIGURATOR_UA,
           }
        url = "https://p25-buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/volumeStoreDownloadProduct?guid=%s" % self.guid
        payload = req.as_dict()
        r = self.sess.post(url,
                           headers=hdrs,
                           data=plistlib.dumps(payload))
        d = plistlib.loads(r.content)
        resp = StoreDownloadResp.from_dict(d)
        if resp.cancel_purchase_batch:
            raise StoreException("volumeStoreDownloadProduct", d, resp.customerMessage, '%s-%s' % (resp.failureType, resp.metrics))
        return resp

    def buyProduct(self, appId, appVer='', productType='C', pricingParameters='STDQ'):
        # STDQ - buy, STDRDL - redownload, SWUPD - update
        url = "https://p25-buy.itunes.apple.com/WebObjects/MZBuy.woa/wa/buyProduct"
        
        itunes_internal = self.iTunes_provider(url)
        hdrs = itunes_internal.pop('headers')
        guid = itunes_internal.pop('guid')
        kbsync = itunes_internal.pop('kbsync')

        if not appVer:
            from reqs.itunes import iTunesClient
            iTunes = iTunesClient(self.sess)
            appVer = iTunes.getAppVerId(appId, hdrs['X-Apple-Store-Front'])

        req = StoreBuyproductReq(
            guid=guid,
            salableAdamId=str(appId),
            appExtVrsId=str(appVer) if appVer else None,
            
            price='0',
            productType=productType,
            pricingParameters=pricingParameters,
            
            # ageCheck='true',
            # hasBeenAuthedForBuy='true',
            # isInApp='false',
        )
        payload = req.as_dict()
        # kbsync is bytes, but json schema does not support it, so we have to assign it
        payload['kbsync'] = kbsync

        hdrs = dict(hdrs)
        hdrs["Content-Type"] = "application/x-apple-plist"

        r = self.sess.post(url,
                        headers=hdrs, 
                        data=plistlib.dumps(payload)
                        )

        d = plistlib.loads(r.content)
        resp = StoreBuyproductResp.from_dict(d)
        if resp.cancel_purchase_batch:
            raise StoreException("buyProduct", d, resp.customerMessage, '%s-%s' % (resp.failureType, resp.metrics))
        return resp

    def buyProduct_purchase(self, appId, productType='C'):
        url = "https://buy.itunes.apple.com/WebObjects/MZBuy.woa/wa/buyProduct"
        req = StoreBuyproductReq(
            guid=self.guid,
            salableAdamId=str(appId),
            appExtVrsId='0',

            price='0',
            productType=productType,
            pricingParameters='STDQ',

            hasAskedToFulfillPreorder='true',
            buyWithoutAuthorization='true',
            hasDoneAgeCheck='true',
        )
        payload = req.as_dict()

        r = self.sess.post(url,
                           headers={
                               "Content-Type": "application/x-apple-plist",
                               "User-Agent": "Configurator/2.15 (Macintosh; OS X 11.0.0; 16G29) AppleWebKit/2603.3.8",
                           },
                           data=plistlib.dumps(payload))

        if r.status_code == 500:
            raise StoreException("buyProduct_purchase", None, 'purchased_before')

        d = plistlib.loads(r.content)
        resp = StoreBuyproductResp.from_dict(d)
        if resp.status != 0 or resp.jingleDocType != 'purchaseSuccess':
            raise StoreException("buyProduct_purchase", d, resp.customerMessage,
                                 '%s-%s' % (resp.status, resp.jingleDocType))
        return resp

    def purchase(self, appId):
        if self.iTunes_provider:
            return None # iTunes mode will automatically purchase the app if not purchased
        else:
            return self.buyProduct_purchase(appId)

    def download(self, appId, appVer='', isRedownload=True):
        if self.iTunes_provider:
            return self.buyProduct(appId, appVer, pricingParameters='STDRDL' if isRedownload else 'STDQ')
        else:
            return self.volumeStoreDownloadProduct(appId, appVer)