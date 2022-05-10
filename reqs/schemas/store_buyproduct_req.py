from reprlib import repr as limitedRepr


class StoreBuyproductReq:

    _types_map = {
        "ageCheck": {"type": str, "subtype": None},
        "appExtVrsId": {"type": str, "subtype": None},
        "guid": {"type": str, "subtype": None},
        "hasBeenAuthedForBuy": {"type": str, "subtype": None},
        "isInApp": {"type": str, "subtype": None},
        "kbsync": {"type": str, "subtype": None},
        "machineName": {"type": str, "subtype": None},
        "mtApp": {"type": str, "subtype": None},
        "mtClientId": {"type": str, "subtype": None},
        "mtEventTime": {"type": str, "subtype": None},
        "mtPageId": {"type": str, "subtype": None},
        "mtPageType": {"type": str, "subtype": None},
        "mtPrevPage": {"type": str, "subtype": None},
        "mtRequestId": {"type": str, "subtype": None},
        "mtTopic": {"type": str, "subtype": None},
        "needDiv": {"type": str, "subtype": None},
        "pg": {"type": str, "subtype": None},
        "price": {"type": str, "subtype": None},
        "pricingParameters": {"type": str, "subtype": None},
        "productType": {"type": str, "subtype": None},
        "salableAdamId": {"type": str, "subtype": None},
        "hasAskedToFulfillPreorder": {"type": str, "subtype": None},
        "buyWithoutAuthorization": {"type": str, "subtype": None},
        "hasDoneAgeCheck": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "ageCheck": {
            "required": False,
        },
        "appExtVrsId": {
            "required": True,
        },
        "guid": {
            "required": True,
        },
        "hasBeenAuthedForBuy": {
            "required": False,
        },
        "isInApp": {
            "required": False,
        },
        "kbsync": {
            "required": True,
        },
        "machineName": {
            "required": False,
        },
        "mtApp": {
            "required": False,
        },
        "mtClientId": {
            "required": False,
        },
        "mtEventTime": {
            "required": False,
        },
        "mtPageId": {
            "required": False,
        },
        "mtPageType": {
            "required": False,
        },
        "mtPrevPage": {
            "required": False,
        },
        "mtRequestId": {
            "required": False,
        },
        "mtTopic": {
            "required": False,
        },
        "needDiv": {
            "required": False,
        },
        "pg": {
            "required": False,
        },
        "price": {
            "required": True,
        },
        "pricingParameters": {
            "required": True,
        },
        "productType": {
            "required": True,
        },
        "salableAdamId": {
            "required": True,
        },
        "hasAskedToFulfillPreorder": {
            "required": False,
        },
        "buyWithoutAuthorization": {
            "required": False,
        },
        "hasDoneAgeCheck": {
            "required": False,
        },
    }

    def __init__(
        self,
        ageCheck: str = None,
        appExtVrsId: str = None,
        guid: str = None,
        hasBeenAuthedForBuy: str = None,
        isInApp: str = None,
        kbsync: str = None,
        machineName: str = None,
        mtApp: str = None,
        mtClientId: str = None,
        mtEventTime: str = None,
        mtPageId: str = None,
        mtPageType: str = None,
        mtPrevPage: str = None,
        mtRequestId: str = None,
        mtTopic: str = None,
        needDiv: str = None,
        pg: str = None,
        price: str = None,
        pricingParameters: str = None,
        productType: str = None,
        salableAdamId: str = None,
        hasAskedToFulfillPreorder: str = None,
        buyWithoutAuthorization: str = None,
        hasDoneAgeCheck: str = None,
    ):
        pass
        self.__ageCheck = ageCheck
        self.__appExtVrsId = appExtVrsId
        self.__guid = guid
        self.__hasBeenAuthedForBuy = hasBeenAuthedForBuy
        self.__isInApp = isInApp
        self.__kbsync = kbsync
        self.__machineName = machineName
        self.__mtApp = mtApp
        self.__mtClientId = mtClientId
        self.__mtEventTime = mtEventTime
        self.__mtPageId = mtPageId
        self.__mtPageType = mtPageType
        self.__mtPrevPage = mtPrevPage
        self.__mtRequestId = mtRequestId
        self.__mtTopic = mtTopic
        self.__needDiv = needDiv
        self.__pg = pg
        self.__price = price
        self.__pricingParameters = pricingParameters
        self.__productType = productType
        self.__salableAdamId = salableAdamId
        self.__hasAskedToFulfillPreorder = hasAskedToFulfillPreorder
        self.__buyWithoutAuthorization = buyWithoutAuthorization
        self.__hasDoneAgeCheck = hasDoneAgeCheck

    def _get_ageCheck(self):
        return self.__ageCheck

    def _set_ageCheck(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("ageCheck must be str")

        self.__ageCheck = value

    ageCheck = property(_get_ageCheck, _set_ageCheck)

    def _get_appExtVrsId(self):
        return self.__appExtVrsId

    def _set_appExtVrsId(self, value):
        if not isinstance(value, str):
            raise TypeError("appExtVrsId must be str")

        self.__appExtVrsId = value

    appExtVrsId = property(_get_appExtVrsId, _set_appExtVrsId)

    def _get_guid(self):
        return self.__guid

    def _set_guid(self, value):
        if not isinstance(value, str):
            raise TypeError("guid must be str")

        self.__guid = value

    guid = property(_get_guid, _set_guid)

    def _get_hasBeenAuthedForBuy(self):
        return self.__hasBeenAuthedForBuy

    def _set_hasBeenAuthedForBuy(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("hasBeenAuthedForBuy must be str")

        self.__hasBeenAuthedForBuy = value

    hasBeenAuthedForBuy = property(_get_hasBeenAuthedForBuy, _set_hasBeenAuthedForBuy)

    def _get_isInApp(self):
        return self.__isInApp

    def _set_isInApp(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("isInApp must be str")

        self.__isInApp = value

    isInApp = property(_get_isInApp, _set_isInApp)

    def _get_kbsync(self):
        return self.__kbsync

    def _set_kbsync(self, value):
        if not isinstance(value, str):
            raise TypeError("kbsync must be str")

        self.__kbsync = value

    kbsync = property(_get_kbsync, _set_kbsync)

    def _get_machineName(self):
        return self.__machineName

    def _set_machineName(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("machineName must be str")

        self.__machineName = value

    machineName = property(_get_machineName, _set_machineName)

    def _get_mtApp(self):
        return self.__mtApp

    def _set_mtApp(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtApp must be str")

        self.__mtApp = value

    mtApp = property(_get_mtApp, _set_mtApp)

    def _get_mtClientId(self):
        return self.__mtClientId

    def _set_mtClientId(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtClientId must be str")

        self.__mtClientId = value

    mtClientId = property(_get_mtClientId, _set_mtClientId)

    def _get_mtEventTime(self):
        return self.__mtEventTime

    def _set_mtEventTime(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtEventTime must be str")

        self.__mtEventTime = value

    mtEventTime = property(_get_mtEventTime, _set_mtEventTime)

    def _get_mtPageId(self):
        return self.__mtPageId

    def _set_mtPageId(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtPageId must be str")

        self.__mtPageId = value

    mtPageId = property(_get_mtPageId, _set_mtPageId)

    def _get_mtPageType(self):
        return self.__mtPageType

    def _set_mtPageType(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtPageType must be str")

        self.__mtPageType = value

    mtPageType = property(_get_mtPageType, _set_mtPageType)

    def _get_mtPrevPage(self):
        return self.__mtPrevPage

    def _set_mtPrevPage(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtPrevPage must be str")

        self.__mtPrevPage = value

    mtPrevPage = property(_get_mtPrevPage, _set_mtPrevPage)

    def _get_mtRequestId(self):
        return self.__mtRequestId

    def _set_mtRequestId(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtRequestId must be str")

        self.__mtRequestId = value

    mtRequestId = property(_get_mtRequestId, _set_mtRequestId)

    def _get_mtTopic(self):
        return self.__mtTopic

    def _set_mtTopic(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("mtTopic must be str")

        self.__mtTopic = value

    mtTopic = property(_get_mtTopic, _set_mtTopic)

    def _get_needDiv(self):
        return self.__needDiv

    def _set_needDiv(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("needDiv must be str")

        self.__needDiv = value

    needDiv = property(_get_needDiv, _set_needDiv)

    def _get_pg(self):
        return self.__pg

    def _set_pg(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("pg must be str")

        self.__pg = value

    pg = property(_get_pg, _set_pg)

    def _get_price(self):
        return self.__price

    def _set_price(self, value):
        if not isinstance(value, str):
            raise TypeError("price must be str")

        self.__price = value

    price = property(_get_price, _set_price)

    def _get_pricingParameters(self):
        return self.__pricingParameters

    def _set_pricingParameters(self, value):
        if not isinstance(value, str):
            raise TypeError("pricingParameters must be str")

        self.__pricingParameters = value

    pricingParameters = property(_get_pricingParameters, _set_pricingParameters)

    def _get_productType(self):
        return self.__productType

    def _set_productType(self, value):
        if not isinstance(value, str):
            raise TypeError("productType must be str")

        self.__productType = value

    productType = property(_get_productType, _set_productType)

    def _get_salableAdamId(self):
        return self.__salableAdamId

    def _set_salableAdamId(self, value):
        if not isinstance(value, str):
            raise TypeError("salableAdamId must be str")

        self.__salableAdamId = value

    salableAdamId = property(_get_salableAdamId, _set_salableAdamId)

    def _get_hasAskedToFulfillPreorder(self):
        return self.__hasAskedToFulfillPreorder

    def _set_hasAskedToFulfillPreorder(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("hasAskedToFulfillPreorder must be str")

        self.__hasAskedToFulfillPreorder = value

    hasAskedToFulfillPreorder = property(
        _get_hasAskedToFulfillPreorder, _set_hasAskedToFulfillPreorder
    )

    def _get_buyWithoutAuthorization(self):
        return self.__buyWithoutAuthorization

    def _set_buyWithoutAuthorization(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("buyWithoutAuthorization must be str")

        self.__buyWithoutAuthorization = value

    buyWithoutAuthorization = property(
        _get_buyWithoutAuthorization, _set_buyWithoutAuthorization
    )

    def _get_hasDoneAgeCheck(self):
        return self.__hasDoneAgeCheck

    def _set_hasDoneAgeCheck(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("hasDoneAgeCheck must be str")

        self.__hasDoneAgeCheck = value

    hasDoneAgeCheck = property(_get_hasDoneAgeCheck, _set_hasDoneAgeCheck)

    @staticmethod
    def from_dict(d):
        v = {}
        if "ageCheck" in d:
            v["ageCheck"] = (
                str.from_dict(d["ageCheck"])
                if hasattr(str, "from_dict")
                else d["ageCheck"]
            )
        if "appExtVrsId" in d:
            v["appExtVrsId"] = (
                str.from_dict(d["appExtVrsId"])
                if hasattr(str, "from_dict")
                else d["appExtVrsId"]
            )
        if "guid" in d:
            v["guid"] = (
                str.from_dict(d["guid"]) if hasattr(str, "from_dict") else d["guid"]
            )
        if "hasBeenAuthedForBuy" in d:
            v["hasBeenAuthedForBuy"] = (
                str.from_dict(d["hasBeenAuthedForBuy"])
                if hasattr(str, "from_dict")
                else d["hasBeenAuthedForBuy"]
            )
        if "isInApp" in d:
            v["isInApp"] = (
                str.from_dict(d["isInApp"])
                if hasattr(str, "from_dict")
                else d["isInApp"]
            )
        if "kbsync" in d:
            v["kbsync"] = (
                str.from_dict(d["kbsync"]) if hasattr(str, "from_dict") else d["kbsync"]
            )
        if "machineName" in d:
            v["machineName"] = (
                str.from_dict(d["machineName"])
                if hasattr(str, "from_dict")
                else d["machineName"]
            )
        if "mtApp" in d:
            v["mtApp"] = (
                str.from_dict(d["mtApp"]) if hasattr(str, "from_dict") else d["mtApp"]
            )
        if "mtClientId" in d:
            v["mtClientId"] = (
                str.from_dict(d["mtClientId"])
                if hasattr(str, "from_dict")
                else d["mtClientId"]
            )
        if "mtEventTime" in d:
            v["mtEventTime"] = (
                str.from_dict(d["mtEventTime"])
                if hasattr(str, "from_dict")
                else d["mtEventTime"]
            )
        if "mtPageId" in d:
            v["mtPageId"] = (
                str.from_dict(d["mtPageId"])
                if hasattr(str, "from_dict")
                else d["mtPageId"]
            )
        if "mtPageType" in d:
            v["mtPageType"] = (
                str.from_dict(d["mtPageType"])
                if hasattr(str, "from_dict")
                else d["mtPageType"]
            )
        if "mtPrevPage" in d:
            v["mtPrevPage"] = (
                str.from_dict(d["mtPrevPage"])
                if hasattr(str, "from_dict")
                else d["mtPrevPage"]
            )
        if "mtRequestId" in d:
            v["mtRequestId"] = (
                str.from_dict(d["mtRequestId"])
                if hasattr(str, "from_dict")
                else d["mtRequestId"]
            )
        if "mtTopic" in d:
            v["mtTopic"] = (
                str.from_dict(d["mtTopic"])
                if hasattr(str, "from_dict")
                else d["mtTopic"]
            )
        if "needDiv" in d:
            v["needDiv"] = (
                str.from_dict(d["needDiv"])
                if hasattr(str, "from_dict")
                else d["needDiv"]
            )
        if "pg" in d:
            v["pg"] = str.from_dict(d["pg"]) if hasattr(str, "from_dict") else d["pg"]
        if "price" in d:
            v["price"] = (
                str.from_dict(d["price"]) if hasattr(str, "from_dict") else d["price"]
            )
        if "pricingParameters" in d:
            v["pricingParameters"] = (
                str.from_dict(d["pricingParameters"])
                if hasattr(str, "from_dict")
                else d["pricingParameters"]
            )
        if "productType" in d:
            v["productType"] = (
                str.from_dict(d["productType"])
                if hasattr(str, "from_dict")
                else d["productType"]
            )
        if "salableAdamId" in d:
            v["salableAdamId"] = (
                str.from_dict(d["salableAdamId"])
                if hasattr(str, "from_dict")
                else d["salableAdamId"]
            )
        if "hasAskedToFulfillPreorder" in d:
            v["hasAskedToFulfillPreorder"] = (
                str.from_dict(d["hasAskedToFulfillPreorder"])
                if hasattr(str, "from_dict")
                else d["hasAskedToFulfillPreorder"]
            )
        if "buyWithoutAuthorization" in d:
            v["buyWithoutAuthorization"] = (
                str.from_dict(d["buyWithoutAuthorization"])
                if hasattr(str, "from_dict")
                else d["buyWithoutAuthorization"]
            )
        if "hasDoneAgeCheck" in d:
            v["hasDoneAgeCheck"] = (
                str.from_dict(d["hasDoneAgeCheck"])
                if hasattr(str, "from_dict")
                else d["hasDoneAgeCheck"]
            )
        return StoreBuyproductReq(**v)

    def as_dict(self):
        d = {}
        if self.__ageCheck is not None:
            d["ageCheck"] = (
                self.__ageCheck.as_dict()
                if hasattr(self.__ageCheck, "as_dict")
                else self.__ageCheck
            )
        if self.__appExtVrsId is not None:
            d["appExtVrsId"] = (
                self.__appExtVrsId.as_dict()
                if hasattr(self.__appExtVrsId, "as_dict")
                else self.__appExtVrsId
            )
        if self.__guid is not None:
            d["guid"] = (
                self.__guid.as_dict()
                if hasattr(self.__guid, "as_dict")
                else self.__guid
            )
        if self.__hasBeenAuthedForBuy is not None:
            d["hasBeenAuthedForBuy"] = (
                self.__hasBeenAuthedForBuy.as_dict()
                if hasattr(self.__hasBeenAuthedForBuy, "as_dict")
                else self.__hasBeenAuthedForBuy
            )
        if self.__isInApp is not None:
            d["isInApp"] = (
                self.__isInApp.as_dict()
                if hasattr(self.__isInApp, "as_dict")
                else self.__isInApp
            )
        if self.__kbsync is not None:
            d["kbsync"] = (
                self.__kbsync.as_dict()
                if hasattr(self.__kbsync, "as_dict")
                else self.__kbsync
            )
        if self.__machineName is not None:
            d["machineName"] = (
                self.__machineName.as_dict()
                if hasattr(self.__machineName, "as_dict")
                else self.__machineName
            )
        if self.__mtApp is not None:
            d["mtApp"] = (
                self.__mtApp.as_dict()
                if hasattr(self.__mtApp, "as_dict")
                else self.__mtApp
            )
        if self.__mtClientId is not None:
            d["mtClientId"] = (
                self.__mtClientId.as_dict()
                if hasattr(self.__mtClientId, "as_dict")
                else self.__mtClientId
            )
        if self.__mtEventTime is not None:
            d["mtEventTime"] = (
                self.__mtEventTime.as_dict()
                if hasattr(self.__mtEventTime, "as_dict")
                else self.__mtEventTime
            )
        if self.__mtPageId is not None:
            d["mtPageId"] = (
                self.__mtPageId.as_dict()
                if hasattr(self.__mtPageId, "as_dict")
                else self.__mtPageId
            )
        if self.__mtPageType is not None:
            d["mtPageType"] = (
                self.__mtPageType.as_dict()
                if hasattr(self.__mtPageType, "as_dict")
                else self.__mtPageType
            )
        if self.__mtPrevPage is not None:
            d["mtPrevPage"] = (
                self.__mtPrevPage.as_dict()
                if hasattr(self.__mtPrevPage, "as_dict")
                else self.__mtPrevPage
            )
        if self.__mtRequestId is not None:
            d["mtRequestId"] = (
                self.__mtRequestId.as_dict()
                if hasattr(self.__mtRequestId, "as_dict")
                else self.__mtRequestId
            )
        if self.__mtTopic is not None:
            d["mtTopic"] = (
                self.__mtTopic.as_dict()
                if hasattr(self.__mtTopic, "as_dict")
                else self.__mtTopic
            )
        if self.__needDiv is not None:
            d["needDiv"] = (
                self.__needDiv.as_dict()
                if hasattr(self.__needDiv, "as_dict")
                else self.__needDiv
            )
        if self.__pg is not None:
            d["pg"] = (
                self.__pg.as_dict() if hasattr(self.__pg, "as_dict") else self.__pg
            )
        if self.__price is not None:
            d["price"] = (
                self.__price.as_dict()
                if hasattr(self.__price, "as_dict")
                else self.__price
            )
        if self.__pricingParameters is not None:
            d["pricingParameters"] = (
                self.__pricingParameters.as_dict()
                if hasattr(self.__pricingParameters, "as_dict")
                else self.__pricingParameters
            )
        if self.__productType is not None:
            d["productType"] = (
                self.__productType.as_dict()
                if hasattr(self.__productType, "as_dict")
                else self.__productType
            )
        if self.__salableAdamId is not None:
            d["salableAdamId"] = (
                self.__salableAdamId.as_dict()
                if hasattr(self.__salableAdamId, "as_dict")
                else self.__salableAdamId
            )
        if self.__hasAskedToFulfillPreorder is not None:
            d["hasAskedToFulfillPreorder"] = (
                self.__hasAskedToFulfillPreorder.as_dict()
                if hasattr(self.__hasAskedToFulfillPreorder, "as_dict")
                else self.__hasAskedToFulfillPreorder
            )
        if self.__buyWithoutAuthorization is not None:
            d["buyWithoutAuthorization"] = (
                self.__buyWithoutAuthorization.as_dict()
                if hasattr(self.__buyWithoutAuthorization, "as_dict")
                else self.__buyWithoutAuthorization
            )
        if self.__hasDoneAgeCheck is not None:
            d["hasDoneAgeCheck"] = (
                self.__hasDoneAgeCheck.as_dict()
                if hasattr(self.__hasDoneAgeCheck, "as_dict")
                else self.__hasDoneAgeCheck
            )
        return d

    def __repr__(self):
        return "<Class StoreBuyproductReq. ageCheck: {}, appExtVrsId: {}, guid: {}, hasBeenAuthedForBuy: {}, isInApp: {}, kbsync: {}, machineName: {}, mtApp: {}, mtClientId: {}, mtEventTime: {}, mtPageId: {}, mtPageType: {}, mtPrevPage: {}, mtRequestId: {}, mtTopic: {}, needDiv: {}, pg: {}, price: {}, pricingParameters: {}, productType: {}, salableAdamId: {}, hasAskedToFulfillPreorder: {}, buyWithoutAuthorization: {}, hasDoneAgeCheck: {}>".format(
            limitedRepr(
                self.__ageCheck[:20]
                if isinstance(self.__ageCheck, bytes)
                else self.__ageCheck
            ),
            limitedRepr(
                self.__appExtVrsId[:20]
                if isinstance(self.__appExtVrsId, bytes)
                else self.__appExtVrsId
            ),
            limitedRepr(
                self.__guid[:20] if isinstance(self.__guid, bytes) else self.__guid
            ),
            limitedRepr(
                self.__hasBeenAuthedForBuy[:20]
                if isinstance(self.__hasBeenAuthedForBuy, bytes)
                else self.__hasBeenAuthedForBuy
            ),
            limitedRepr(
                self.__isInApp[:20]
                if isinstance(self.__isInApp, bytes)
                else self.__isInApp
            ),
            limitedRepr(
                self.__kbsync[:20]
                if isinstance(self.__kbsync, bytes)
                else self.__kbsync
            ),
            limitedRepr(
                self.__machineName[:20]
                if isinstance(self.__machineName, bytes)
                else self.__machineName
            ),
            limitedRepr(
                self.__mtApp[:20] if isinstance(self.__mtApp, bytes) else self.__mtApp
            ),
            limitedRepr(
                self.__mtClientId[:20]
                if isinstance(self.__mtClientId, bytes)
                else self.__mtClientId
            ),
            limitedRepr(
                self.__mtEventTime[:20]
                if isinstance(self.__mtEventTime, bytes)
                else self.__mtEventTime
            ),
            limitedRepr(
                self.__mtPageId[:20]
                if isinstance(self.__mtPageId, bytes)
                else self.__mtPageId
            ),
            limitedRepr(
                self.__mtPageType[:20]
                if isinstance(self.__mtPageType, bytes)
                else self.__mtPageType
            ),
            limitedRepr(
                self.__mtPrevPage[:20]
                if isinstance(self.__mtPrevPage, bytes)
                else self.__mtPrevPage
            ),
            limitedRepr(
                self.__mtRequestId[:20]
                if isinstance(self.__mtRequestId, bytes)
                else self.__mtRequestId
            ),
            limitedRepr(
                self.__mtTopic[:20]
                if isinstance(self.__mtTopic, bytes)
                else self.__mtTopic
            ),
            limitedRepr(
                self.__needDiv[:20]
                if isinstance(self.__needDiv, bytes)
                else self.__needDiv
            ),
            limitedRepr(self.__pg[:20] if isinstance(self.__pg, bytes) else self.__pg),
            limitedRepr(
                self.__price[:20] if isinstance(self.__price, bytes) else self.__price
            ),
            limitedRepr(
                self.__pricingParameters[:20]
                if isinstance(self.__pricingParameters, bytes)
                else self.__pricingParameters
            ),
            limitedRepr(
                self.__productType[:20]
                if isinstance(self.__productType, bytes)
                else self.__productType
            ),
            limitedRepr(
                self.__salableAdamId[:20]
                if isinstance(self.__salableAdamId, bytes)
                else self.__salableAdamId
            ),
            limitedRepr(
                self.__hasAskedToFulfillPreorder[:20]
                if isinstance(self.__hasAskedToFulfillPreorder, bytes)
                else self.__hasAskedToFulfillPreorder
            ),
            limitedRepr(
                self.__buyWithoutAuthorization[:20]
                if isinstance(self.__buyWithoutAuthorization, bytes)
                else self.__buyWithoutAuthorization
            ),
            limitedRepr(
                self.__hasDoneAgeCheck[:20]
                if isinstance(self.__hasDoneAgeCheck, bytes)
                else self.__hasDoneAgeCheck
            ),
        )
