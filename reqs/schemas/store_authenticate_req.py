from reprlib import repr as limitedRepr


class StoreAuthenticateReq:

    _types_map = {
        "appleId": {"type": str, "subtype": None},
        "attempt": {"type": str, "subtype": None},
        "createSession": {"type": str, "subtype": None},
        "guid": {"type": str, "subtype": None},
        "password": {"type": str, "subtype": None},
        "rmp": {"type": str, "subtype": None},
        "why": {"type": str, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "appleId": {
            "required": True,
        },
        "attempt": {
            "required": True,
        },
        "createSession": {
            "required": True,
        },
        "guid": {
            "required": True,
        },
        "password": {
            "required": True,
        },
        "rmp": {
            "required": True,
        },
        "why": {
            "required": True,
        },
    }

    def __init__(
        self,
        appleId: str = None,
        attempt: str = None,
        createSession: str = None,
        guid: str = None,
        password: str = None,
        rmp: str = None,
        why: str = None,
    ):
        pass
        self.__appleId = appleId
        self.__attempt = attempt
        self.__createSession = createSession
        self.__guid = guid
        self.__password = password
        self.__rmp = rmp
        self.__why = why

    def _get_appleId(self):
        return self.__appleId

    def _set_appleId(self, value):
        if not isinstance(value, str):
            raise TypeError("appleId must be str")

        self.__appleId = value

    appleId = property(_get_appleId, _set_appleId)

    def _get_attempt(self):
        return self.__attempt

    def _set_attempt(self, value):
        if not isinstance(value, str):
            raise TypeError("attempt must be str")

        self.__attempt = value

    attempt = property(_get_attempt, _set_attempt)

    def _get_createSession(self):
        return self.__createSession

    def _set_createSession(self, value):
        if not isinstance(value, str):
            raise TypeError("createSession must be str")

        self.__createSession = value

    createSession = property(_get_createSession, _set_createSession)

    def _get_guid(self):
        return self.__guid

    def _set_guid(self, value):
        if not isinstance(value, str):
            raise TypeError("guid must be str")

        self.__guid = value

    guid = property(_get_guid, _set_guid)

    def _get_password(self):
        return self.__password

    def _set_password(self, value):
        if not isinstance(value, str):
            raise TypeError("password must be str")

        self.__password = value

    password = property(_get_password, _set_password)

    def _get_rmp(self):
        return self.__rmp

    def _set_rmp(self, value):
        if not isinstance(value, str):
            raise TypeError("rmp must be str")

        self.__rmp = value

    rmp = property(_get_rmp, _set_rmp)

    def _get_why(self):
        return self.__why

    def _set_why(self, value):
        if not isinstance(value, str):
            raise TypeError("why must be str")

        self.__why = value

    why = property(_get_why, _set_why)

    @staticmethod
    def from_dict(d):
        v = {}
        if "appleId" in d:
            v["appleId"] = (
                str.from_dict(d["appleId"])
                if hasattr(str, "from_dict")
                else d["appleId"]
            )
        if "attempt" in d:
            v["attempt"] = (
                str.from_dict(d["attempt"])
                if hasattr(str, "from_dict")
                else d["attempt"]
            )
        if "createSession" in d:
            v["createSession"] = (
                str.from_dict(d["createSession"])
                if hasattr(str, "from_dict")
                else d["createSession"]
            )
        if "guid" in d:
            v["guid"] = (
                str.from_dict(d["guid"]) if hasattr(str, "from_dict") else d["guid"]
            )
        if "password" in d:
            v["password"] = (
                str.from_dict(d["password"])
                if hasattr(str, "from_dict")
                else d["password"]
            )
        if "rmp" in d:
            v["rmp"] = (
                str.from_dict(d["rmp"]) if hasattr(str, "from_dict") else d["rmp"]
            )
        if "why" in d:
            v["why"] = (
                str.from_dict(d["why"]) if hasattr(str, "from_dict") else d["why"]
            )
        return StoreAuthenticateReq(**v)

    def as_dict(self):
        d = {}
        if self.__appleId is not None:
            d["appleId"] = (
                self.__appleId.as_dict()
                if hasattr(self.__appleId, "as_dict")
                else self.__appleId
            )
        if self.__attempt is not None:
            d["attempt"] = (
                self.__attempt.as_dict()
                if hasattr(self.__attempt, "as_dict")
                else self.__attempt
            )
        if self.__createSession is not None:
            d["createSession"] = (
                self.__createSession.as_dict()
                if hasattr(self.__createSession, "as_dict")
                else self.__createSession
            )
        if self.__guid is not None:
            d["guid"] = (
                self.__guid.as_dict()
                if hasattr(self.__guid, "as_dict")
                else self.__guid
            )
        if self.__password is not None:
            d["password"] = (
                self.__password.as_dict()
                if hasattr(self.__password, "as_dict")
                else self.__password
            )
        if self.__rmp is not None:
            d["rmp"] = (
                self.__rmp.as_dict() if hasattr(self.__rmp, "as_dict") else self.__rmp
            )
        if self.__why is not None:
            d["why"] = (
                self.__why.as_dict() if hasattr(self.__why, "as_dict") else self.__why
            )
        return d

    def __repr__(self):
        return "<Class StoreAuthenticateReq. appleId: {}, attempt: {}, createSession: {}, guid: {}, password: {}, rmp: {}, why: {}>".format(
            limitedRepr(
                self.__appleId[:20]
                if isinstance(self.__appleId, bytes)
                else self.__appleId
            ),
            limitedRepr(
                self.__attempt[:20]
                if isinstance(self.__attempt, bytes)
                else self.__attempt
            ),
            limitedRepr(
                self.__createSession[:20]
                if isinstance(self.__createSession, bytes)
                else self.__createSession
            ),
            limitedRepr(
                self.__guid[:20] if isinstance(self.__guid, bytes) else self.__guid
            ),
            limitedRepr(
                self.__password[:20]
                if isinstance(self.__password, bytes)
                else self.__password
            ),
            limitedRepr(
                self.__rmp[:20] if isinstance(self.__rmp, bytes) else self.__rmp
            ),
            limitedRepr(
                self.__why[:20] if isinstance(self.__why, bytes) else self.__why
            ),
        )
