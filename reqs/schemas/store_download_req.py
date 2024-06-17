from reprlib import repr as limitedRepr





class StoreDownloadReq:



    _types_map = {
        'creditDisplay': {'type': str, 'subtype': None},
        'guid': {'type': str, 'subtype': None},
        'salableAdamId': {'type': str, 'subtype': None},
        'externalVersionId': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'creditDisplay': { 'required': True,},
        'guid': { 'required': True,},
        'salableAdamId': { 'required': True,},
        'externalVersionId': { 'required': False,},
    }

    def __init__(self
            , creditDisplay: str=None            , guid: str=None            , salableAdamId: str=None            , externalVersionId: str=None            ):
        pass
        self.__creditDisplay = creditDisplay
        self.__guid = guid
        self.__salableAdamId = salableAdamId
        self.__externalVersionId = externalVersionId
    
    def _get_creditDisplay(self):
        return self.__creditDisplay
    def _set_creditDisplay(self, value):
        if  not isinstance(value, str):
            raise TypeError("creditDisplay must be str")

        self.__creditDisplay = value
    creditDisplay = property(_get_creditDisplay, _set_creditDisplay)
    
    def _get_guid(self):
        return self.__guid
    def _set_guid(self, value):
        if  not isinstance(value, str):
            raise TypeError("guid must be str")

        self.__guid = value
    guid = property(_get_guid, _set_guid)
    
    def _get_salableAdamId(self):
        return self.__salableAdamId
    def _set_salableAdamId(self, value):
        if  not isinstance(value, str):
            raise TypeError("salableAdamId must be str")

        self.__salableAdamId = value
    salableAdamId = property(_get_salableAdamId, _set_salableAdamId)
    
    def _get_externalVersionId(self):
        return self.__externalVersionId
    def _set_externalVersionId(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("externalVersionId must be str")

        self.__externalVersionId = value
    externalVersionId = property(_get_externalVersionId, _set_externalVersionId)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "creditDisplay" in d:
            v["creditDisplay"] = str.from_dict(d["creditDisplay"]) if hasattr(str, 'from_dict') else d["creditDisplay"]
        if "guid" in d:
            v["guid"] = str.from_dict(d["guid"]) if hasattr(str, 'from_dict') else d["guid"]
        if "salableAdamId" in d:
            v["salableAdamId"] = str.from_dict(d["salableAdamId"]) if hasattr(str, 'from_dict') else d["salableAdamId"]
        if "externalVersionId" in d:
            v["externalVersionId"] = str.from_dict(d["externalVersionId"]) if hasattr(str, 'from_dict') else d["externalVersionId"]
        return StoreDownloadReq(**v)


    def as_dict(self):
        d = {}
        if self.__creditDisplay is not None:
            d['creditDisplay'] = self.__creditDisplay.as_dict() if hasattr(self.__creditDisplay, 'as_dict') else self.__creditDisplay
        if self.__guid is not None:
            d['guid'] = self.__guid.as_dict() if hasattr(self.__guid, 'as_dict') else self.__guid
        if self.__salableAdamId is not None:
            d['salableAdamId'] = self.__salableAdamId.as_dict() if hasattr(self.__salableAdamId, 'as_dict') else self.__salableAdamId
        if self.__externalVersionId is not None:
            d['externalVersionId'] = self.__externalVersionId.as_dict() if hasattr(self.__externalVersionId, 'as_dict') else self.__externalVersionId
        return d

    def __repr__(self):
        return "<Class StoreDownloadReq. creditDisplay: {}, guid: {}, salableAdamId: {}, externalVersionId: {}>".format(limitedRepr(self.__creditDisplay[:20] if isinstance(self.__creditDisplay, bytes) else self.__creditDisplay), limitedRepr(self.__guid[:20] if isinstance(self.__guid, bytes) else self.__guid), limitedRepr(self.__salableAdamId[:20] if isinstance(self.__salableAdamId, bytes) else self.__salableAdamId), limitedRepr(self.__externalVersionId[:20] if isinstance(self.__externalVersionId, bytes) else self.__externalVersionId))

