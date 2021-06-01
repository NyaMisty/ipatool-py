__all__ = ['iTunesClient']
from reqs.schemas.itunes_lookup_resp import ItunesLookupResp
import requests

class iTunesClient(object):
    def __init__(self, sess: requests.Session):
        self.sess = sess

    # curl -k -X GET \
    # -H "Content-Type: application/x-www-form-urlencoded" \
    # https://itunes.apple.com/lookup?bundleId=com.touchingapp.potatsolite&limit=1&media=software
    def lookup(self, bundleId=None, term=None, country="US", limit=1, media="software") -> ItunesLookupResp:
        r = self.sess.get("https://itunes.apple.com/lookup?",
                    params={
                        "bundleId": bundleId,
                        "term": term,
                        "country": country,
                        "limit": limit,
                        "media": media,
                    },
                    headers={
                         "Content-Type": "application/x-www-form-urlencoded",
                    })
        return ItunesLookupResp.from_dict(r.json())