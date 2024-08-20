from reprlib import repr as limitedRepr


from typing import List


class ItunesLookupResp:
    class _results:

        _types_map = {
            "appletvScreenshotUrls": {"type": list, "subtype": float},
            "screenshotUrls": {"type": list, "subtype": str},
            "ipadScreenshotUrls": {"type": list, "subtype": str},
            "artworkUrl60": {"type": str, "subtype": None},
            "artworkUrl512": {"type": str, "subtype": None},
            "artworkUrl100": {"type": str, "subtype": None},
            "artistViewUrl": {"type": str, "subtype": None},
            "supportedDevices": {"type": list, "subtype": str},
            "advisories": {"type": list, "subtype": float},
            "isGameCenterEnabled": {"type": bool, "subtype": None},
            "kind": {"type": str, "subtype": None},
            "features": {"type": list, "subtype": str},
            "minimumOsVersion": {"type": str, "subtype": None},
            "trackCensoredName": {"type": str, "subtype": None},
            "languageCodesISO2A": {"type": list, "subtype": str},
            "fileSizeBytes": {"type": str, "subtype": None},
            "formattedPrice": {"type": str, "subtype": None},
            "contentAdvisoryRating": {"type": str, "subtype": None},
            "averageUserRatingForCurrentVersion": {"type": float, "subtype": None},
            "userRatingCountForCurrentVersion": {"type": int, "subtype": None},
            "averageUserRating": {"type": float, "subtype": None},
            "trackViewUrl": {"type": str, "subtype": None},
            "trackContentRating": {"type": str, "subtype": None},
            "releaseDate": {"type": str, "subtype": None},
            "genreIds": {"type": list, "subtype": str},
            "primaryGenreName": {"type": str, "subtype": None},
            "trackId": {"type": int, "subtype": None},
            "trackName": {"type": str, "subtype": None},
            "sellerName": {"type": str, "subtype": None},
            "isVppDeviceBasedLicensingEnabled": {"type": bool, "subtype": None},
            "currentVersionReleaseDate": {"type": str, "subtype": None},
            "releaseNotes": {"type": str, "subtype": None},
            "primaryGenreId": {"type": int, "subtype": None},
            "currency": {"type": str, "subtype": None},
            "version": {"type": str, "subtype": None},
            "wrapperType": {"type": str, "subtype": None},
            "artistId": {"type": int, "subtype": None},
            "artistName": {"type": str, "subtype": None},
            "genres": {"type": list, "subtype": str},
            "price": {"type": float, "subtype": None},
            "description": {"type": str, "subtype": None},
            "bundleId": {"type": str, "subtype": None},
            "userRatingCount": {"type": int, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "appletvScreenshotUrls": {
                "required": True,
            },
            "screenshotUrls": {
                "required": True,
            },
            "ipadScreenshotUrls": {
                "required": True,
            },
            "artworkUrl60": {
                "required": True,
            },
            "artworkUrl512": {
                "required": True,
            },
            "artworkUrl100": {
                "required": True,
            },
            "artistViewUrl": {
                "required": True,
            },
            "supportedDevices": {
                "required": True,
            },
            "advisories": {
                "required": True,
            },
            "isGameCenterEnabled": {
                "required": True,
            },
            "kind": {
                "required": True,
            },
            "features": {
                "required": True,
            },
            "minimumOsVersion": {
                "required": True,
            },
            "trackCensoredName": {
                "required": True,
            },
            "languageCodesISO2A": {
                "required": True,
            },
            "fileSizeBytes": {
                "required": True,
            },
            "formattedPrice": {
                "required": True,
            },
            "contentAdvisoryRating": {
                "required": True,
            },
            "averageUserRatingForCurrentVersion": {
                "required": True,
            },
            "userRatingCountForCurrentVersion": {
                "required": True,
            },
            "averageUserRating": {
                "required": True,
            },
            "trackViewUrl": {
                "required": True,
            },
            "trackContentRating": {
                "required": True,
            },
            "releaseDate": {
                "required": True,
            },
            "genreIds": {
                "required": True,
            },
            "primaryGenreName": {
                "required": True,
            },
            "trackId": {
                "required": True,
            },
            "trackName": {
                "required": True,
            },
            "sellerName": {
                "required": True,
            },
            "isVppDeviceBasedLicensingEnabled": {
                "required": True,
            },
            "currentVersionReleaseDate": {
                "required": True,
            },
            "releaseNotes": {
                "required": True,
            },
            "primaryGenreId": {
                "required": True,
            },
            "currency": {
                "required": True,
            },
            "version": {
                "required": True,
            },
            "wrapperType": {
                "required": True,
            },
            "artistId": {
                "required": True,
            },
            "artistName": {
                "required": True,
            },
            "genres": {
                "required": True,
            },
            "price": {
                "required": True,
            },
            "description": {
                "required": True,
            },
            "bundleId": {
                "required": True,
            },
            "userRatingCount": {
                "required": True,
            },
        }

        def __init__(
            self,
            appletvScreenshotUrls: List[float] = None,
            screenshotUrls: List[str] = None,
            ipadScreenshotUrls: List[str] = None,
            artworkUrl60: str = None,
            artworkUrl512: str = None,
            artworkUrl100: str = None,
            artistViewUrl: str = None,
            supportedDevices: List[str] = None,
            advisories: List[float] = None,
            isGameCenterEnabled: bool = None,
            kind: str = None,
            features: List[str] = None,
            minimumOsVersion: str = None,
            trackCensoredName: str = None,
            languageCodesISO2A: List[str] = None,
            fileSizeBytes: str = None,
            formattedPrice: str = None,
            contentAdvisoryRating: str = None,
            averageUserRatingForCurrentVersion: float = None,
            userRatingCountForCurrentVersion: int = None,
            averageUserRating: float = None,
            trackViewUrl: str = None,
            trackContentRating: str = None,
            releaseDate: str = None,
            genreIds: List[str] = None,
            primaryGenreName: str = None,
            trackId: int = None,
            trackName: str = None,
            sellerName: str = None,
            isVppDeviceBasedLicensingEnabled: bool = None,
            currentVersionReleaseDate: str = None,
            releaseNotes: str = None,
            primaryGenreId: int = None,
            currency: str = None,
            version: str = None,
            wrapperType: str = None,
            artistId: int = None,
            artistName: str = None,
            genres: List[str] = None,
            price: float = None,
            description: str = None,
            bundleId: str = None,
            userRatingCount: int = None,
        ):
            pass
            self.__appletvScreenshotUrls = appletvScreenshotUrls
            self.__screenshotUrls = screenshotUrls
            self.__ipadScreenshotUrls = ipadScreenshotUrls
            self.__artworkUrl60 = artworkUrl60
            self.__artworkUrl512 = artworkUrl512
            self.__artworkUrl100 = artworkUrl100
            self.__artistViewUrl = artistViewUrl
            self.__supportedDevices = supportedDevices
            self.__advisories = advisories
            self.__isGameCenterEnabled = isGameCenterEnabled
            self.__kind = kind
            self.__features = features
            self.__minimumOsVersion = minimumOsVersion
            self.__trackCensoredName = trackCensoredName
            self.__languageCodesISO2A = languageCodesISO2A
            self.__fileSizeBytes = fileSizeBytes
            self.__formattedPrice = formattedPrice
            self.__contentAdvisoryRating = contentAdvisoryRating
            self.__averageUserRatingForCurrentVersion = (
                averageUserRatingForCurrentVersion
            )
            self.__userRatingCountForCurrentVersion = userRatingCountForCurrentVersion
            self.__averageUserRating = averageUserRating
            self.__trackViewUrl = trackViewUrl
            self.__trackContentRating = trackContentRating
            self.__releaseDate = releaseDate
            self.__genreIds = genreIds
            self.__primaryGenreName = primaryGenreName
            self.__trackId = trackId
            self.__trackName = trackName
            self.__sellerName = sellerName
            self.__isVppDeviceBasedLicensingEnabled = isVppDeviceBasedLicensingEnabled
            self.__currentVersionReleaseDate = currentVersionReleaseDate
            self.__releaseNotes = releaseNotes
            self.__primaryGenreId = primaryGenreId
            self.__currency = currency
            self.__version = version
            self.__wrapperType = wrapperType
            self.__artistId = artistId
            self.__artistName = artistName
            self.__genres = genres
            self.__price = price
            self.__description = description
            self.__bundleId = bundleId
            self.__userRatingCount = userRatingCount

        def _get_appletvScreenshotUrls(self):
            return self.__appletvScreenshotUrls

        def _set_appletvScreenshotUrls(self, value):
            if not isinstance(value, list):
                raise TypeError("appletvScreenshotUrls must be list")
            if not all(isinstance(i, float) for i in value):
                raise TypeError("appletvScreenshotUrls list values must be float")

            self.__appletvScreenshotUrls = value

        appletvScreenshotUrls = property(
            _get_appletvScreenshotUrls, _set_appletvScreenshotUrls
        )

        def _get_screenshotUrls(self):
            return self.__screenshotUrls

        def _set_screenshotUrls(self, value):
            if not isinstance(value, list):
                raise TypeError("screenshotUrls must be list")
            if not all(isinstance(i, str) for i in value):
                raise TypeError("screenshotUrls list values must be str")

            self.__screenshotUrls = value

        screenshotUrls = property(_get_screenshotUrls, _set_screenshotUrls)

        def _get_ipadScreenshotUrls(self):
            return self.__ipadScreenshotUrls

        def _set_ipadScreenshotUrls(self, value):
            if not isinstance(value, list):
                raise TypeError("ipadScreenshotUrls must be list")
            if not all(isinstance(i, str) for i in value):
                raise TypeError("ipadScreenshotUrls list values must be str")

            self.__ipadScreenshotUrls = value

        ipadScreenshotUrls = property(_get_ipadScreenshotUrls, _set_ipadScreenshotUrls)

        def _get_artworkUrl60(self):
            return self.__artworkUrl60

        def _set_artworkUrl60(self, value):
            if not isinstance(value, str):
                raise TypeError("artworkUrl60 must be str")

            self.__artworkUrl60 = value

        artworkUrl60 = property(_get_artworkUrl60, _set_artworkUrl60)

        def _get_artworkUrl512(self):
            return self.__artworkUrl512

        def _set_artworkUrl512(self, value):
            if not isinstance(value, str):
                raise TypeError("artworkUrl512 must be str")

            self.__artworkUrl512 = value

        artworkUrl512 = property(_get_artworkUrl512, _set_artworkUrl512)

        def _get_artworkUrl100(self):
            return self.__artworkUrl100

        def _set_artworkUrl100(self, value):
            if not isinstance(value, str):
                raise TypeError("artworkUrl100 must be str")

            self.__artworkUrl100 = value

        artworkUrl100 = property(_get_artworkUrl100, _set_artworkUrl100)

        def _get_artistViewUrl(self):
            return self.__artistViewUrl

        def _set_artistViewUrl(self, value):
            if not isinstance(value, str):
                raise TypeError("artistViewUrl must be str")

            self.__artistViewUrl = value

        artistViewUrl = property(_get_artistViewUrl, _set_artistViewUrl)

        def _get_supportedDevices(self):
            return self.__supportedDevices

        def _set_supportedDevices(self, value):
            if not isinstance(value, list):
                raise TypeError("supportedDevices must be list")
            if not all(isinstance(i, str) for i in value):
                raise TypeError("supportedDevices list values must be str")

            self.__supportedDevices = value

        supportedDevices = property(_get_supportedDevices, _set_supportedDevices)

        def _get_advisories(self):
            return self.__advisories

        def _set_advisories(self, value):
            if not isinstance(value, list):
                raise TypeError("advisories must be list")
            if not all(isinstance(i, float) for i in value):
                raise TypeError("advisories list values must be float")

            self.__advisories = value

        advisories = property(_get_advisories, _set_advisories)

        def _get_isGameCenterEnabled(self):
            return self.__isGameCenterEnabled

        def _set_isGameCenterEnabled(self, value):
            if not isinstance(value, bool):
                raise TypeError("isGameCenterEnabled must be bool")

            self.__isGameCenterEnabled = value

        isGameCenterEnabled = property(
            _get_isGameCenterEnabled, _set_isGameCenterEnabled
        )

        def _get_kind(self):
            return self.__kind

        def _set_kind(self, value):
            if not isinstance(value, str):
                raise TypeError("kind must be str")

            self.__kind = value

        kind = property(_get_kind, _set_kind)

        def _get_features(self):
            return self.__features

        def _set_features(self, value):
            if not isinstance(value, list):
                raise TypeError("features must be list")
            if not all(isinstance(i, str) for i in value):
                raise TypeError("features list values must be str")

            self.__features = value

        features = property(_get_features, _set_features)

        def _get_minimumOsVersion(self):
            return self.__minimumOsVersion

        def _set_minimumOsVersion(self, value):
            if not isinstance(value, str):
                raise TypeError("minimumOsVersion must be str")

            self.__minimumOsVersion = value

        minimumOsVersion = property(_get_minimumOsVersion, _set_minimumOsVersion)

        def _get_trackCensoredName(self):
            return self.__trackCensoredName

        def _set_trackCensoredName(self, value):
            if not isinstance(value, str):
                raise TypeError("trackCensoredName must be str")

            self.__trackCensoredName = value

        trackCensoredName = property(_get_trackCensoredName, _set_trackCensoredName)

        def _get_languageCodesISO2A(self):
            return self.__languageCodesISO2A

        def _set_languageCodesISO2A(self, value):
            if not isinstance(value, list):
                raise TypeError("languageCodesISO2A must be list")
            if not all(isinstance(i, str) for i in value):
                raise TypeError("languageCodesISO2A list values must be str")

            self.__languageCodesISO2A = value

        languageCodesISO2A = property(_get_languageCodesISO2A, _set_languageCodesISO2A)

        def _get_fileSizeBytes(self):
            return self.__fileSizeBytes

        def _set_fileSizeBytes(self, value):
            if not isinstance(value, str):
                raise TypeError("fileSizeBytes must be str")

            self.__fileSizeBytes = value

        fileSizeBytes = property(_get_fileSizeBytes, _set_fileSizeBytes)

        def _get_formattedPrice(self):
            return self.__formattedPrice

        def _set_formattedPrice(self, value):
            if not isinstance(value, str):
                raise TypeError("formattedPrice must be str")

            self.__formattedPrice = value

        formattedPrice = property(_get_formattedPrice, _set_formattedPrice)

        def _get_contentAdvisoryRating(self):
            return self.__contentAdvisoryRating

        def _set_contentAdvisoryRating(self, value):
            if not isinstance(value, str):
                raise TypeError("contentAdvisoryRating must be str")

            self.__contentAdvisoryRating = value

        contentAdvisoryRating = property(
            _get_contentAdvisoryRating, _set_contentAdvisoryRating
        )

        def _get_averageUserRatingForCurrentVersion(self):
            return self.__averageUserRatingForCurrentVersion

        def _set_averageUserRatingForCurrentVersion(self, value):
            if not isinstance(value, float):
                raise TypeError("averageUserRatingForCurrentVersion must be float")

            self.__averageUserRatingForCurrentVersion = value

        averageUserRatingForCurrentVersion = property(
            _get_averageUserRatingForCurrentVersion,
            _set_averageUserRatingForCurrentVersion,
        )

        def _get_userRatingCountForCurrentVersion(self):
            return self.__userRatingCountForCurrentVersion

        def _set_userRatingCountForCurrentVersion(self, value):
            if not isinstance(value, int):
                raise TypeError("userRatingCountForCurrentVersion must be int")

            self.__userRatingCountForCurrentVersion = value

        userRatingCountForCurrentVersion = property(
            _get_userRatingCountForCurrentVersion, _set_userRatingCountForCurrentVersion
        )

        def _get_averageUserRating(self):
            return self.__averageUserRating

        def _set_averageUserRating(self, value):
            if not isinstance(value, float):
                raise TypeError("averageUserRating must be float")

            self.__averageUserRating = value

        averageUserRating = property(_get_averageUserRating, _set_averageUserRating)

        def _get_trackViewUrl(self):
            return self.__trackViewUrl

        def _set_trackViewUrl(self, value):
            if not isinstance(value, str):
                raise TypeError("trackViewUrl must be str")

            self.__trackViewUrl = value

        trackViewUrl = property(_get_trackViewUrl, _set_trackViewUrl)

        def _get_trackContentRating(self):
            return self.__trackContentRating

        def _set_trackContentRating(self, value):
            if not isinstance(value, str):
                raise TypeError("trackContentRating must be str")

            self.__trackContentRating = value

        trackContentRating = property(_get_trackContentRating, _set_trackContentRating)

        def _get_releaseDate(self):
            return self.__releaseDate

        def _set_releaseDate(self, value):
            if not isinstance(value, str):
                raise TypeError("releaseDate must be str")

            self.__releaseDate = value

        releaseDate = property(_get_releaseDate, _set_releaseDate)

        def _get_genreIds(self):
            return self.__genreIds

        def _set_genreIds(self, value):
            if not isinstance(value, list):
                raise TypeError("genreIds must be list")
            if not all(isinstance(i, str) for i in value):
                raise TypeError("genreIds list values must be str")

            self.__genreIds = value

        genreIds = property(_get_genreIds, _set_genreIds)

        def _get_primaryGenreName(self):
            return self.__primaryGenreName

        def _set_primaryGenreName(self, value):
            if not isinstance(value, str):
                raise TypeError("primaryGenreName must be str")

            self.__primaryGenreName = value

        primaryGenreName = property(_get_primaryGenreName, _set_primaryGenreName)

        def _get_trackId(self):
            return self.__trackId

        def _set_trackId(self, value):
            if not isinstance(value, int):
                raise TypeError("trackId must be int")

            self.__trackId = value

        trackId = property(_get_trackId, _set_trackId)

        def _get_trackName(self):
            return self.__trackName

        def _set_trackName(self, value):
            if not isinstance(value, str):
                raise TypeError("trackName must be str")

            self.__trackName = value

        trackName = property(_get_trackName, _set_trackName)

        def _get_sellerName(self):
            return self.__sellerName

        def _set_sellerName(self, value):
            if not isinstance(value, str):
                raise TypeError("sellerName must be str")

            self.__sellerName = value

        sellerName = property(_get_sellerName, _set_sellerName)

        def _get_isVppDeviceBasedLicensingEnabled(self):
            return self.__isVppDeviceBasedLicensingEnabled

        def _set_isVppDeviceBasedLicensingEnabled(self, value):
            if not isinstance(value, bool):
                raise TypeError("isVppDeviceBasedLicensingEnabled must be bool")

            self.__isVppDeviceBasedLicensingEnabled = value

        isVppDeviceBasedLicensingEnabled = property(
            _get_isVppDeviceBasedLicensingEnabled, _set_isVppDeviceBasedLicensingEnabled
        )

        def _get_currentVersionReleaseDate(self):
            return self.__currentVersionReleaseDate

        def _set_currentVersionReleaseDate(self, value):
            if not isinstance(value, str):
                raise TypeError("currentVersionReleaseDate must be str")

            self.__currentVersionReleaseDate = value

        currentVersionReleaseDate = property(
            _get_currentVersionReleaseDate, _set_currentVersionReleaseDate
        )

        def _get_releaseNotes(self):
            return self.__releaseNotes

        def _set_releaseNotes(self, value):
            if not isinstance(value, str):
                raise TypeError("releaseNotes must be str")

            self.__releaseNotes = value

        releaseNotes = property(_get_releaseNotes, _set_releaseNotes)

        def _get_primaryGenreId(self):
            return self.__primaryGenreId

        def _set_primaryGenreId(self, value):
            if not isinstance(value, int):
                raise TypeError("primaryGenreId must be int")

            self.__primaryGenreId = value

        primaryGenreId = property(_get_primaryGenreId, _set_primaryGenreId)

        def _get_currency(self):
            return self.__currency

        def _set_currency(self, value):
            if not isinstance(value, str):
                raise TypeError("currency must be str")

            self.__currency = value

        currency = property(_get_currency, _set_currency)

        def _get_version(self):
            return self.__version

        def _set_version(self, value):
            if not isinstance(value, str):
                raise TypeError("version must be str")

            self.__version = value

        version = property(_get_version, _set_version)

        def _get_wrapperType(self):
            return self.__wrapperType

        def _set_wrapperType(self, value):
            if not isinstance(value, str):
                raise TypeError("wrapperType must be str")

            self.__wrapperType = value

        wrapperType = property(_get_wrapperType, _set_wrapperType)

        def _get_artistId(self):
            return self.__artistId

        def _set_artistId(self, value):
            if not isinstance(value, int):
                raise TypeError("artistId must be int")

            self.__artistId = value

        artistId = property(_get_artistId, _set_artistId)

        def _get_artistName(self):
            return self.__artistName

        def _set_artistName(self, value):
            if not isinstance(value, str):
                raise TypeError("artistName must be str")

            self.__artistName = value

        artistName = property(_get_artistName, _set_artistName)

        def _get_genres(self):
            return self.__genres

        def _set_genres(self, value):
            if not isinstance(value, list):
                raise TypeError("genres must be list")
            if not all(isinstance(i, str) for i in value):
                raise TypeError("genres list values must be str")

            self.__genres = value

        genres = property(_get_genres, _set_genres)

        def _get_price(self):
            return self.__price

        def _set_price(self, value):
            if not isinstance(value, float):
                raise TypeError("price must be float")

            self.__price = value

        price = property(_get_price, _set_price)

        def _get_description(self):
            return self.__description

        def _set_description(self, value):
            if not isinstance(value, str):
                raise TypeError("description must be str")

            self.__description = value

        description = property(_get_description, _set_description)

        def _get_bundleId(self):
            return self.__bundleId

        def _set_bundleId(self, value):
            if not isinstance(value, str):
                raise TypeError("bundleId must be str")

            self.__bundleId = value

        bundleId = property(_get_bundleId, _set_bundleId)

        def _get_userRatingCount(self):
            return self.__userRatingCount

        def _set_userRatingCount(self, value):
            if not isinstance(value, int):
                raise TypeError("userRatingCount must be int")

            self.__userRatingCount = value

        userRatingCount = property(_get_userRatingCount, _set_userRatingCount)

        @staticmethod
        def from_dict(d):
            v = {}
            if "appletvScreenshotUrls" in d:
                v["appletvScreenshotUrls"] = [
                    float.from_dict(p) if hasattr(float, "from_dict") else p
                    for p in d["appletvScreenshotUrls"]
                ]
            if "screenshotUrls" in d:
                v["screenshotUrls"] = [
                    str.from_dict(p) if hasattr(str, "from_dict") else p
                    for p in d["screenshotUrls"]
                ]
            if "ipadScreenshotUrls" in d:
                v["ipadScreenshotUrls"] = [
                    str.from_dict(p) if hasattr(str, "from_dict") else p
                    for p in d["ipadScreenshotUrls"]
                ]
            if "artworkUrl60" in d:
                v["artworkUrl60"] = (
                    str.from_dict(d["artworkUrl60"])
                    if hasattr(str, "from_dict")
                    else d["artworkUrl60"]
                )
            if "artworkUrl512" in d:
                v["artworkUrl512"] = (
                    str.from_dict(d["artworkUrl512"])
                    if hasattr(str, "from_dict")
                    else d["artworkUrl512"]
                )
            if "artworkUrl100" in d:
                v["artworkUrl100"] = (
                    str.from_dict(d["artworkUrl100"])
                    if hasattr(str, "from_dict")
                    else d["artworkUrl100"]
                )
            if "artistViewUrl" in d:
                v["artistViewUrl"] = (
                    str.from_dict(d["artistViewUrl"])
                    if hasattr(str, "from_dict")
                    else d["artistViewUrl"]
                )
            if "supportedDevices" in d:
                v["supportedDevices"] = [
                    str.from_dict(p) if hasattr(str, "from_dict") else p
                    for p in d["supportedDevices"]
                ]
            if "advisories" in d:
                v["advisories"] = [
                    float.from_dict(p) if hasattr(float, "from_dict") else p
                    for p in d["advisories"]
                ]
            if "isGameCenterEnabled" in d:
                v["isGameCenterEnabled"] = (
                    bool.from_dict(d["isGameCenterEnabled"])
                    if hasattr(bool, "from_dict")
                    else d["isGameCenterEnabled"]
                )
            if "kind" in d:
                v["kind"] = (
                    str.from_dict(d["kind"]) if hasattr(str, "from_dict") else d["kind"]
                )
            if "features" in d:
                v["features"] = [
                    str.from_dict(p) if hasattr(str, "from_dict") else p
                    for p in d["features"]
                ]
            if "minimumOsVersion" in d:
                v["minimumOsVersion"] = (
                    str.from_dict(d["minimumOsVersion"])
                    if hasattr(str, "from_dict")
                    else d["minimumOsVersion"]
                )
            if "trackCensoredName" in d:
                v["trackCensoredName"] = (
                    str.from_dict(d["trackCensoredName"])
                    if hasattr(str, "from_dict")
                    else d["trackCensoredName"]
                )
            if "languageCodesISO2A" in d:
                v["languageCodesISO2A"] = [
                    str.from_dict(p) if hasattr(str, "from_dict") else p
                    for p in d["languageCodesISO2A"]
                ]
            if "fileSizeBytes" in d:
                v["fileSizeBytes"] = (
                    str.from_dict(d["fileSizeBytes"])
                    if hasattr(str, "from_dict")
                    else d["fileSizeBytes"]
                )
            if "formattedPrice" in d:
                v["formattedPrice"] = (
                    str.from_dict(d["formattedPrice"])
                    if hasattr(str, "from_dict")
                    else d["formattedPrice"]
                )
            if "contentAdvisoryRating" in d:
                v["contentAdvisoryRating"] = (
                    str.from_dict(d["contentAdvisoryRating"])
                    if hasattr(str, "from_dict")
                    else d["contentAdvisoryRating"]
                )
            if "averageUserRatingForCurrentVersion" in d:
                v["averageUserRatingForCurrentVersion"] = (
                    float.from_dict(d["averageUserRatingForCurrentVersion"])
                    if hasattr(float, "from_dict")
                    else d["averageUserRatingForCurrentVersion"]
                )
            if "userRatingCountForCurrentVersion" in d:
                v["userRatingCountForCurrentVersion"] = (
                    int.from_dict(d["userRatingCountForCurrentVersion"])
                    if hasattr(int, "from_dict")
                    else d["userRatingCountForCurrentVersion"]
                )
            if "averageUserRating" in d:
                v["averageUserRating"] = (
                    float.from_dict(d["averageUserRating"])
                    if hasattr(float, "from_dict")
                    else d["averageUserRating"]
                )
            if "trackViewUrl" in d:
                v["trackViewUrl"] = (
                    str.from_dict(d["trackViewUrl"])
                    if hasattr(str, "from_dict")
                    else d["trackViewUrl"]
                )
            if "trackContentRating" in d:
                v["trackContentRating"] = (
                    str.from_dict(d["trackContentRating"])
                    if hasattr(str, "from_dict")
                    else d["trackContentRating"]
                )
            if "releaseDate" in d:
                v["releaseDate"] = (
                    str.from_dict(d["releaseDate"])
                    if hasattr(str, "from_dict")
                    else d["releaseDate"]
                )
            if "genreIds" in d:
                v["genreIds"] = [
                    str.from_dict(p) if hasattr(str, "from_dict") else p
                    for p in d["genreIds"]
                ]
            if "primaryGenreName" in d:
                v["primaryGenreName"] = (
                    str.from_dict(d["primaryGenreName"])
                    if hasattr(str, "from_dict")
                    else d["primaryGenreName"]
                )
            if "trackId" in d:
                v["trackId"] = (
                    int.from_dict(d["trackId"])
                    if hasattr(int, "from_dict")
                    else d["trackId"]
                )
            if "trackName" in d:
                v["trackName"] = (
                    str.from_dict(d["trackName"])
                    if hasattr(str, "from_dict")
                    else d["trackName"]
                )
            if "sellerName" in d:
                v["sellerName"] = (
                    str.from_dict(d["sellerName"])
                    if hasattr(str, "from_dict")
                    else d["sellerName"]
                )
            if "isVppDeviceBasedLicensingEnabled" in d:
                v["isVppDeviceBasedLicensingEnabled"] = (
                    bool.from_dict(d["isVppDeviceBasedLicensingEnabled"])
                    if hasattr(bool, "from_dict")
                    else d["isVppDeviceBasedLicensingEnabled"]
                )
            if "currentVersionReleaseDate" in d:
                v["currentVersionReleaseDate"] = (
                    str.from_dict(d["currentVersionReleaseDate"])
                    if hasattr(str, "from_dict")
                    else d["currentVersionReleaseDate"]
                )
            if "releaseNotes" in d:
                v["releaseNotes"] = (
                    str.from_dict(d["releaseNotes"])
                    if hasattr(str, "from_dict")
                    else d["releaseNotes"]
                )
            if "primaryGenreId" in d:
                v["primaryGenreId"] = (
                    int.from_dict(d["primaryGenreId"])
                    if hasattr(int, "from_dict")
                    else d["primaryGenreId"]
                )
            if "currency" in d:
                v["currency"] = (
                    str.from_dict(d["currency"])
                    if hasattr(str, "from_dict")
                    else d["currency"]
                )
            if "version" in d:
                v["version"] = (
                    str.from_dict(d["version"])
                    if hasattr(str, "from_dict")
                    else d["version"]
                )
            if "wrapperType" in d:
                v["wrapperType"] = (
                    str.from_dict(d["wrapperType"])
                    if hasattr(str, "from_dict")
                    else d["wrapperType"]
                )
            if "artistId" in d:
                v["artistId"] = (
                    int.from_dict(d["artistId"])
                    if hasattr(int, "from_dict")
                    else d["artistId"]
                )
            if "artistName" in d:
                v["artistName"] = (
                    str.from_dict(d["artistName"])
                    if hasattr(str, "from_dict")
                    else d["artistName"]
                )
            if "genres" in d:
                v["genres"] = [
                    str.from_dict(p) if hasattr(str, "from_dict") else p
                    for p in d["genres"]
                ]
            if "price" in d:
                v["price"] = (
                    float.from_dict(d["price"])
                    if hasattr(float, "from_dict")
                    else d["price"]
                )
            if "description" in d:
                v["description"] = (
                    str.from_dict(d["description"])
                    if hasattr(str, "from_dict")
                    else d["description"]
                )
            if "bundleId" in d:
                v["bundleId"] = (
                    str.from_dict(d["bundleId"])
                    if hasattr(str, "from_dict")
                    else d["bundleId"]
                )
            if "userRatingCount" in d:
                v["userRatingCount"] = (
                    int.from_dict(d["userRatingCount"])
                    if hasattr(int, "from_dict")
                    else d["userRatingCount"]
                )
            return ItunesLookupResp._results(**v)

        def as_dict(self):
            d = {}
            if self.__appletvScreenshotUrls is not None:
                d["appletvScreenshotUrls"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p
                    for p in self.__appletvScreenshotUrls
                ]
            if self.__screenshotUrls is not None:
                d["screenshotUrls"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p
                    for p in self.__screenshotUrls
                ]
            if self.__ipadScreenshotUrls is not None:
                d["ipadScreenshotUrls"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p
                    for p in self.__ipadScreenshotUrls
                ]
            if self.__artworkUrl60 is not None:
                d["artworkUrl60"] = (
                    self.__artworkUrl60.as_dict()
                    if hasattr(self.__artworkUrl60, "as_dict")
                    else self.__artworkUrl60
                )
            if self.__artworkUrl512 is not None:
                d["artworkUrl512"] = (
                    self.__artworkUrl512.as_dict()
                    if hasattr(self.__artworkUrl512, "as_dict")
                    else self.__artworkUrl512
                )
            if self.__artworkUrl100 is not None:
                d["artworkUrl100"] = (
                    self.__artworkUrl100.as_dict()
                    if hasattr(self.__artworkUrl100, "as_dict")
                    else self.__artworkUrl100
                )
            if self.__artistViewUrl is not None:
                d["artistViewUrl"] = (
                    self.__artistViewUrl.as_dict()
                    if hasattr(self.__artistViewUrl, "as_dict")
                    else self.__artistViewUrl
                )
            if self.__supportedDevices is not None:
                d["supportedDevices"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p
                    for p in self.__supportedDevices
                ]
            if self.__advisories is not None:
                d["advisories"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p
                    for p in self.__advisories
                ]
            if self.__isGameCenterEnabled is not None:
                d["isGameCenterEnabled"] = (
                    self.__isGameCenterEnabled.as_dict()
                    if hasattr(self.__isGameCenterEnabled, "as_dict")
                    else self.__isGameCenterEnabled
                )
            if self.__kind is not None:
                d["kind"] = (
                    self.__kind.as_dict()
                    if hasattr(self.__kind, "as_dict")
                    else self.__kind
                )
            if self.__features is not None:
                d["features"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p for p in self.__features
                ]
            if self.__minimumOsVersion is not None:
                d["minimumOsVersion"] = (
                    self.__minimumOsVersion.as_dict()
                    if hasattr(self.__minimumOsVersion, "as_dict")
                    else self.__minimumOsVersion
                )
            if self.__trackCensoredName is not None:
                d["trackCensoredName"] = (
                    self.__trackCensoredName.as_dict()
                    if hasattr(self.__trackCensoredName, "as_dict")
                    else self.__trackCensoredName
                )
            if self.__languageCodesISO2A is not None:
                d["languageCodesISO2A"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p
                    for p in self.__languageCodesISO2A
                ]
            if self.__fileSizeBytes is not None:
                d["fileSizeBytes"] = (
                    self.__fileSizeBytes.as_dict()
                    if hasattr(self.__fileSizeBytes, "as_dict")
                    else self.__fileSizeBytes
                )
            if self.__formattedPrice is not None:
                d["formattedPrice"] = (
                    self.__formattedPrice.as_dict()
                    if hasattr(self.__formattedPrice, "as_dict")
                    else self.__formattedPrice
                )
            if self.__contentAdvisoryRating is not None:
                d["contentAdvisoryRating"] = (
                    self.__contentAdvisoryRating.as_dict()
                    if hasattr(self.__contentAdvisoryRating, "as_dict")
                    else self.__contentAdvisoryRating
                )
            if self.__averageUserRatingForCurrentVersion is not None:
                d["averageUserRatingForCurrentVersion"] = (
                    self.__averageUserRatingForCurrentVersion.as_dict()
                    if hasattr(self.__averageUserRatingForCurrentVersion, "as_dict")
                    else self.__averageUserRatingForCurrentVersion
                )
            if self.__userRatingCountForCurrentVersion is not None:
                d["userRatingCountForCurrentVersion"] = (
                    self.__userRatingCountForCurrentVersion.as_dict()
                    if hasattr(self.__userRatingCountForCurrentVersion, "as_dict")
                    else self.__userRatingCountForCurrentVersion
                )
            if self.__averageUserRating is not None:
                d["averageUserRating"] = (
                    self.__averageUserRating.as_dict()
                    if hasattr(self.__averageUserRating, "as_dict")
                    else self.__averageUserRating
                )
            if self.__trackViewUrl is not None:
                d["trackViewUrl"] = (
                    self.__trackViewUrl.as_dict()
                    if hasattr(self.__trackViewUrl, "as_dict")
                    else self.__trackViewUrl
                )
            if self.__trackContentRating is not None:
                d["trackContentRating"] = (
                    self.__trackContentRating.as_dict()
                    if hasattr(self.__trackContentRating, "as_dict")
                    else self.__trackContentRating
                )
            if self.__releaseDate is not None:
                d["releaseDate"] = (
                    self.__releaseDate.as_dict()
                    if hasattr(self.__releaseDate, "as_dict")
                    else self.__releaseDate
                )
            if self.__genreIds is not None:
                d["genreIds"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p for p in self.__genreIds
                ]
            if self.__primaryGenreName is not None:
                d["primaryGenreName"] = (
                    self.__primaryGenreName.as_dict()
                    if hasattr(self.__primaryGenreName, "as_dict")
                    else self.__primaryGenreName
                )
            if self.__trackId is not None:
                d["trackId"] = (
                    self.__trackId.as_dict()
                    if hasattr(self.__trackId, "as_dict")
                    else self.__trackId
                )
            if self.__trackName is not None:
                d["trackName"] = (
                    self.__trackName.as_dict()
                    if hasattr(self.__trackName, "as_dict")
                    else self.__trackName
                )
            if self.__sellerName is not None:
                d["sellerName"] = (
                    self.__sellerName.as_dict()
                    if hasattr(self.__sellerName, "as_dict")
                    else self.__sellerName
                )
            if self.__isVppDeviceBasedLicensingEnabled is not None:
                d["isVppDeviceBasedLicensingEnabled"] = (
                    self.__isVppDeviceBasedLicensingEnabled.as_dict()
                    if hasattr(self.__isVppDeviceBasedLicensingEnabled, "as_dict")
                    else self.__isVppDeviceBasedLicensingEnabled
                )
            if self.__currentVersionReleaseDate is not None:
                d["currentVersionReleaseDate"] = (
                    self.__currentVersionReleaseDate.as_dict()
                    if hasattr(self.__currentVersionReleaseDate, "as_dict")
                    else self.__currentVersionReleaseDate
                )
            if self.__releaseNotes is not None:
                d["releaseNotes"] = (
                    self.__releaseNotes.as_dict()
                    if hasattr(self.__releaseNotes, "as_dict")
                    else self.__releaseNotes
                )
            if self.__primaryGenreId is not None:
                d["primaryGenreId"] = (
                    self.__primaryGenreId.as_dict()
                    if hasattr(self.__primaryGenreId, "as_dict")
                    else self.__primaryGenreId
                )
            if self.__currency is not None:
                d["currency"] = (
                    self.__currency.as_dict()
                    if hasattr(self.__currency, "as_dict")
                    else self.__currency
                )
            if self.__version is not None:
                d["version"] = (
                    self.__version.as_dict()
                    if hasattr(self.__version, "as_dict")
                    else self.__version
                )
            if self.__wrapperType is not None:
                d["wrapperType"] = (
                    self.__wrapperType.as_dict()
                    if hasattr(self.__wrapperType, "as_dict")
                    else self.__wrapperType
                )
            if self.__artistId is not None:
                d["artistId"] = (
                    self.__artistId.as_dict()
                    if hasattr(self.__artistId, "as_dict")
                    else self.__artistId
                )
            if self.__artistName is not None:
                d["artistName"] = (
                    self.__artistName.as_dict()
                    if hasattr(self.__artistName, "as_dict")
                    else self.__artistName
                )
            if self.__genres is not None:
                d["genres"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p for p in self.__genres
                ]
            if self.__price is not None:
                d["price"] = (
                    self.__price.as_dict()
                    if hasattr(self.__price, "as_dict")
                    else self.__price
                )
            if self.__description is not None:
                d["description"] = (
                    self.__description.as_dict()
                    if hasattr(self.__description, "as_dict")
                    else self.__description
                )
            if self.__bundleId is not None:
                d["bundleId"] = (
                    self.__bundleId.as_dict()
                    if hasattr(self.__bundleId, "as_dict")
                    else self.__bundleId
                )
            if self.__userRatingCount is not None:
                d["userRatingCount"] = (
                    self.__userRatingCount.as_dict()
                    if hasattr(self.__userRatingCount, "as_dict")
                    else self.__userRatingCount
                )
            return d

        def __repr__(self):
            return "<Class _results. appletvScreenshotUrls: {}, screenshotUrls: {}, ipadScreenshotUrls: {}, artworkUrl60: {}, artworkUrl512: {}, artworkUrl100: {}, artistViewUrl: {}, supportedDevices: {}, advisories: {}, isGameCenterEnabled: {}, kind: {}, features: {}, minimumOsVersion: {}, trackCensoredName: {}, languageCodesISO2A: {}, fileSizeBytes: {}, formattedPrice: {}, contentAdvisoryRating: {}, averageUserRatingForCurrentVersion: {}, userRatingCountForCurrentVersion: {}, averageUserRating: {}, trackViewUrl: {}, trackContentRating: {}, releaseDate: {}, genreIds: {}, primaryGenreName: {}, trackId: {}, trackName: {}, sellerName: {}, isVppDeviceBasedLicensingEnabled: {}, currentVersionReleaseDate: {}, releaseNotes: {}, primaryGenreId: {}, currency: {}, version: {}, wrapperType: {}, artistId: {}, artistName: {}, genres: {}, price: {}, description: {}, bundleId: {}, userRatingCount: {}>".format(
                limitedRepr(
                    self.__appletvScreenshotUrls[:20]
                    if isinstance(self.__appletvScreenshotUrls, bytes)
                    else self.__appletvScreenshotUrls
                ),
                limitedRepr(
                    self.__screenshotUrls[:20]
                    if isinstance(self.__screenshotUrls, bytes)
                    else self.__screenshotUrls
                ),
                limitedRepr(
                    self.__ipadScreenshotUrls[:20]
                    if isinstance(self.__ipadScreenshotUrls, bytes)
                    else self.__ipadScreenshotUrls
                ),
                limitedRepr(
                    self.__artworkUrl60[:20]
                    if isinstance(self.__artworkUrl60, bytes)
                    else self.__artworkUrl60
                ),
                limitedRepr(
                    self.__artworkUrl512[:20]
                    if isinstance(self.__artworkUrl512, bytes)
                    else self.__artworkUrl512
                ),
                limitedRepr(
                    self.__artworkUrl100[:20]
                    if isinstance(self.__artworkUrl100, bytes)
                    else self.__artworkUrl100
                ),
                limitedRepr(
                    self.__artistViewUrl[:20]
                    if isinstance(self.__artistViewUrl, bytes)
                    else self.__artistViewUrl
                ),
                limitedRepr(
                    self.__supportedDevices[:20]
                    if isinstance(self.__supportedDevices, bytes)
                    else self.__supportedDevices
                ),
                limitedRepr(
                    self.__advisories[:20]
                    if isinstance(self.__advisories, bytes)
                    else self.__advisories
                ),
                limitedRepr(
                    self.__isGameCenterEnabled[:20]
                    if isinstance(self.__isGameCenterEnabled, bytes)
                    else self.__isGameCenterEnabled
                ),
                limitedRepr(
                    self.__kind[:20] if isinstance(self.__kind, bytes) else self.__kind
                ),
                limitedRepr(
                    self.__features[:20]
                    if isinstance(self.__features, bytes)
                    else self.__features
                ),
                limitedRepr(
                    self.__minimumOsVersion[:20]
                    if isinstance(self.__minimumOsVersion, bytes)
                    else self.__minimumOsVersion
                ),
                limitedRepr(
                    self.__trackCensoredName[:20]
                    if isinstance(self.__trackCensoredName, bytes)
                    else self.__trackCensoredName
                ),
                limitedRepr(
                    self.__languageCodesISO2A[:20]
                    if isinstance(self.__languageCodesISO2A, bytes)
                    else self.__languageCodesISO2A
                ),
                limitedRepr(
                    self.__fileSizeBytes[:20]
                    if isinstance(self.__fileSizeBytes, bytes)
                    else self.__fileSizeBytes
                ),
                limitedRepr(
                    self.__formattedPrice[:20]
                    if isinstance(self.__formattedPrice, bytes)
                    else self.__formattedPrice
                ),
                limitedRepr(
                    self.__contentAdvisoryRating[:20]
                    if isinstance(self.__contentAdvisoryRating, bytes)
                    else self.__contentAdvisoryRating
                ),
                limitedRepr(
                    self.__averageUserRatingForCurrentVersion[:20]
                    if isinstance(self.__averageUserRatingForCurrentVersion, bytes)
                    else self.__averageUserRatingForCurrentVersion
                ),
                limitedRepr(
                    self.__userRatingCountForCurrentVersion[:20]
                    if isinstance(self.__userRatingCountForCurrentVersion, bytes)
                    else self.__userRatingCountForCurrentVersion
                ),
                limitedRepr(
                    self.__averageUserRating[:20]
                    if isinstance(self.__averageUserRating, bytes)
                    else self.__averageUserRating
                ),
                limitedRepr(
                    self.__trackViewUrl[:20]
                    if isinstance(self.__trackViewUrl, bytes)
                    else self.__trackViewUrl
                ),
                limitedRepr(
                    self.__trackContentRating[:20]
                    if isinstance(self.__trackContentRating, bytes)
                    else self.__trackContentRating
                ),
                limitedRepr(
                    self.__releaseDate[:20]
                    if isinstance(self.__releaseDate, bytes)
                    else self.__releaseDate
                ),
                limitedRepr(
                    self.__genreIds[:20]
                    if isinstance(self.__genreIds, bytes)
                    else self.__genreIds
                ),
                limitedRepr(
                    self.__primaryGenreName[:20]
                    if isinstance(self.__primaryGenreName, bytes)
                    else self.__primaryGenreName
                ),
                limitedRepr(
                    self.__trackId[:20]
                    if isinstance(self.__trackId, bytes)
                    else self.__trackId
                ),
                limitedRepr(
                    self.__trackName[:20]
                    if isinstance(self.__trackName, bytes)
                    else self.__trackName
                ),
                limitedRepr(
                    self.__sellerName[:20]
                    if isinstance(self.__sellerName, bytes)
                    else self.__sellerName
                ),
                limitedRepr(
                    self.__isVppDeviceBasedLicensingEnabled[:20]
                    if isinstance(self.__isVppDeviceBasedLicensingEnabled, bytes)
                    else self.__isVppDeviceBasedLicensingEnabled
                ),
                limitedRepr(
                    self.__currentVersionReleaseDate[:20]
                    if isinstance(self.__currentVersionReleaseDate, bytes)
                    else self.__currentVersionReleaseDate
                ),
                limitedRepr(
                    self.__releaseNotes[:20]
                    if isinstance(self.__releaseNotes, bytes)
                    else self.__releaseNotes
                ),
                limitedRepr(
                    self.__primaryGenreId[:20]
                    if isinstance(self.__primaryGenreId, bytes)
                    else self.__primaryGenreId
                ),
                limitedRepr(
                    self.__currency[:20]
                    if isinstance(self.__currency, bytes)
                    else self.__currency
                ),
                limitedRepr(
                    self.__version[:20]
                    if isinstance(self.__version, bytes)
                    else self.__version
                ),
                limitedRepr(
                    self.__wrapperType[:20]
                    if isinstance(self.__wrapperType, bytes)
                    else self.__wrapperType
                ),
                limitedRepr(
                    self.__artistId[:20]
                    if isinstance(self.__artistId, bytes)
                    else self.__artistId
                ),
                limitedRepr(
                    self.__artistName[:20]
                    if isinstance(self.__artistName, bytes)
                    else self.__artistName
                ),
                limitedRepr(
                    self.__genres[:20]
                    if isinstance(self.__genres, bytes)
                    else self.__genres
                ),
                limitedRepr(
                    self.__price[:20]
                    if isinstance(self.__price, bytes)
                    else self.__price
                ),
                limitedRepr(
                    self.__description[:20]
                    if isinstance(self.__description, bytes)
                    else self.__description
                ),
                limitedRepr(
                    self.__bundleId[:20]
                    if isinstance(self.__bundleId, bytes)
                    else self.__bundleId
                ),
                limitedRepr(
                    self.__userRatingCount[:20]
                    if isinstance(self.__userRatingCount, bytes)
                    else self.__userRatingCount
                ),
            )

    _types_map = {
        "resultCount": {"type": int, "subtype": None},
        "results": {"type": list, "subtype": _results},
    }
    _formats_map = {}
    _validations_map = {
        "resultCount": {
            "required": True,
        },
        "results": {
            "required": True,
        },
    }

    def __init__(self, resultCount: int = None, results: List[_results] = None):
        pass
        self.__resultCount = resultCount
        self.__results = results

    def _get_resultCount(self):
        return self.__resultCount

    def _set_resultCount(self, value):
        if not isinstance(value, int):
            raise TypeError("resultCount must be int")

        self.__resultCount = value

    resultCount = property(_get_resultCount, _set_resultCount)

    def _get_results(self):
        return self.__results

    def _set_results(self, value):
        if not isinstance(value, list):
            raise TypeError("results must be list")
        if not all(isinstance(i, ItunesLookupResp._results) for i in value):
            raise TypeError("results list values must be ItunesLookupResp._results")

        self.__results = value

    results = property(_get_results, _set_results)

    @staticmethod
    def from_dict(d):
        v = {}
        if "resultCount" in d:
            v["resultCount"] = (
                int.from_dict(d["resultCount"])
                if hasattr(int, "from_dict")
                else d["resultCount"]
            )
        if "results" in d:
            v["results"] = [
                ItunesLookupResp._results.from_dict(p)
                if hasattr(ItunesLookupResp._results, "from_dict")
                else p
                for p in d["results"]
            ]
        return ItunesLookupResp(**v)

    def as_dict(self):
        d = {}
        if self.__resultCount is not None:
            d["resultCount"] = (
                self.__resultCount.as_dict()
                if hasattr(self.__resultCount, "as_dict")
                else self.__resultCount
            )
        if self.__results is not None:
            d["results"] = [
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__results
            ]
        return d

    def __repr__(self):
        return "<Class ItunesLookupResp. resultCount: {}, results: {}>".format(
            limitedRepr(
                self.__resultCount[:20]
                if isinstance(self.__resultCount, bytes)
                else self.__resultCount
            ),
            limitedRepr(
                self.__results[:20]
                if isinstance(self.__results, bytes)
                else self.__results
            ),
        )
