from reprlib import repr as limitedRepr


from typing import List


class StoreAuthenticateResp:
    class _subscriptionStatus:
        class _terms:

            _types_map = {
                "type": {"type": str, "subtype": None},
                "latestTerms": {"type": int, "subtype": None},
                "agreedToTerms": {"type": int, "subtype": None},
                "source": {"type": str, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "type": {
                    "required": True,
                },
                "latestTerms": {
                    "required": True,
                },
                "agreedToTerms": {
                    "required": True,
                },
                "source": {
                    "required": True,
                },
            }

            def __init__(
                self,
                type: str = None,
                latestTerms: int = None,
                agreedToTerms: int = None,
                source: str = None,
            ):
                pass
                self.__type = type
                self.__latestTerms = latestTerms
                self.__agreedToTerms = agreedToTerms
                self.__source = source

            def _get_type(self):
                return self.__type

            def _set_type(self, value):
                if not isinstance(value, str):
                    raise TypeError("type must be str")

                self.__type = value

            type = property(_get_type, _set_type)

            def _get_latestTerms(self):
                return self.__latestTerms

            def _set_latestTerms(self, value):
                if not isinstance(value, int):
                    raise TypeError("latestTerms must be int")

                self.__latestTerms = value

            latestTerms = property(_get_latestTerms, _set_latestTerms)

            def _get_agreedToTerms(self):
                return self.__agreedToTerms

            def _set_agreedToTerms(self, value):
                if not isinstance(value, int):
                    raise TypeError("agreedToTerms must be int")

                self.__agreedToTerms = value

            agreedToTerms = property(_get_agreedToTerms, _set_agreedToTerms)

            def _get_source(self):
                return self.__source

            def _set_source(self, value):
                if not isinstance(value, str):
                    raise TypeError("source must be str")

                self.__source = value

            source = property(_get_source, _set_source)

            @staticmethod
            def from_dict(d):
                v = {}
                if "type" in d:
                    v["type"] = (
                        str.from_dict(d["type"])
                        if hasattr(str, "from_dict")
                        else d["type"]
                    )
                if "latestTerms" in d:
                    v["latestTerms"] = (
                        int.from_dict(d["latestTerms"])
                        if hasattr(int, "from_dict")
                        else d["latestTerms"]
                    )
                if "agreedToTerms" in d:
                    v["agreedToTerms"] = (
                        int.from_dict(d["agreedToTerms"])
                        if hasattr(int, "from_dict")
                        else d["agreedToTerms"]
                    )
                if "source" in d:
                    v["source"] = (
                        str.from_dict(d["source"])
                        if hasattr(str, "from_dict")
                        else d["source"]
                    )
                return StoreAuthenticateResp._subscriptionStatus._terms(**v)

            def as_dict(self):
                d = {}
                if self.__type is not None:
                    d["type"] = (
                        self.__type.as_dict()
                        if hasattr(self.__type, "as_dict")
                        else self.__type
                    )
                if self.__latestTerms is not None:
                    d["latestTerms"] = (
                        self.__latestTerms.as_dict()
                        if hasattr(self.__latestTerms, "as_dict")
                        else self.__latestTerms
                    )
                if self.__agreedToTerms is not None:
                    d["agreedToTerms"] = (
                        self.__agreedToTerms.as_dict()
                        if hasattr(self.__agreedToTerms, "as_dict")
                        else self.__agreedToTerms
                    )
                if self.__source is not None:
                    d["source"] = (
                        self.__source.as_dict()
                        if hasattr(self.__source, "as_dict")
                        else self.__source
                    )
                return d

            def __repr__(self):
                return "<Class _terms. type: {}, latestTerms: {}, agreedToTerms: {}, source: {}>".format(
                    limitedRepr(
                        self.__type[:20]
                        if isinstance(self.__type, bytes)
                        else self.__type
                    ),
                    limitedRepr(
                        self.__latestTerms[:20]
                        if isinstance(self.__latestTerms, bytes)
                        else self.__latestTerms
                    ),
                    limitedRepr(
                        self.__agreedToTerms[:20]
                        if isinstance(self.__agreedToTerms, bytes)
                        else self.__agreedToTerms
                    ),
                    limitedRepr(
                        self.__source[:20]
                        if isinstance(self.__source, bytes)
                        else self.__source
                    ),
                )

        class _account:

            _types_map = {
                "isMinor": {"type": bool, "subtype": None},
                "suspectUnderage": {"type": bool, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "isMinor": {
                    "required": True,
                },
                "suspectUnderage": {
                    "required": True,
                },
            }

            def __init__(self, isMinor: bool = None, suspectUnderage: bool = None):
                pass
                self.__isMinor = isMinor
                self.__suspectUnderage = suspectUnderage

            def _get_isMinor(self):
                return self.__isMinor

            def _set_isMinor(self, value):
                if not isinstance(value, bool):
                    raise TypeError("isMinor must be bool")

                self.__isMinor = value

            isMinor = property(_get_isMinor, _set_isMinor)

            def _get_suspectUnderage(self):
                return self.__suspectUnderage

            def _set_suspectUnderage(self, value):
                if not isinstance(value, bool):
                    raise TypeError("suspectUnderage must be bool")

                self.__suspectUnderage = value

            suspectUnderage = property(_get_suspectUnderage, _set_suspectUnderage)

            @staticmethod
            def from_dict(d):
                v = {}
                if "isMinor" in d:
                    v["isMinor"] = (
                        bool.from_dict(d["isMinor"])
                        if hasattr(bool, "from_dict")
                        else d["isMinor"]
                    )
                if "suspectUnderage" in d:
                    v["suspectUnderage"] = (
                        bool.from_dict(d["suspectUnderage"])
                        if hasattr(bool, "from_dict")
                        else d["suspectUnderage"]
                    )
                return StoreAuthenticateResp._subscriptionStatus._account(**v)

            def as_dict(self):
                d = {}
                if self.__isMinor is not None:
                    d["isMinor"] = (
                        self.__isMinor.as_dict()
                        if hasattr(self.__isMinor, "as_dict")
                        else self.__isMinor
                    )
                if self.__suspectUnderage is not None:
                    d["suspectUnderage"] = (
                        self.__suspectUnderage.as_dict()
                        if hasattr(self.__suspectUnderage, "as_dict")
                        else self.__suspectUnderage
                    )
                return d

            def __repr__(self):
                return "<Class _account. isMinor: {}, suspectUnderage: {}>".format(
                    limitedRepr(
                        self.__isMinor[:20]
                        if isinstance(self.__isMinor, bytes)
                        else self.__isMinor
                    ),
                    limitedRepr(
                        self.__suspectUnderage[:20]
                        if isinstance(self.__suspectUnderage, bytes)
                        else self.__suspectUnderage
                    ),
                )

        class _family:

            _types_map = {
                "hasFamily": {"type": bool, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "hasFamily": {
                    "required": True,
                },
            }

            def __init__(self, hasFamily: bool = None):
                pass
                self.__hasFamily = hasFamily

            def _get_hasFamily(self):
                return self.__hasFamily

            def _set_hasFamily(self, value):
                if not isinstance(value, bool):
                    raise TypeError("hasFamily must be bool")

                self.__hasFamily = value

            hasFamily = property(_get_hasFamily, _set_hasFamily)

            @staticmethod
            def from_dict(d):
                v = {}
                if "hasFamily" in d:
                    v["hasFamily"] = (
                        bool.from_dict(d["hasFamily"])
                        if hasattr(bool, "from_dict")
                        else d["hasFamily"]
                    )
                return StoreAuthenticateResp._subscriptionStatus._family(**v)

            def as_dict(self):
                d = {}
                if self.__hasFamily is not None:
                    d["hasFamily"] = (
                        self.__hasFamily.as_dict()
                        if hasattr(self.__hasFamily, "as_dict")
                        else self.__hasFamily
                    )
                return d

            def __repr__(self):
                return "<Class _family. hasFamily: {}>".format(
                    limitedRepr(
                        self.__hasFamily[:20]
                        if isinstance(self.__hasFamily, bytes)
                        else self.__hasFamily
                    )
                )

        _types_map = {
            "terms": {"type": list, "subtype": _terms},
            "account": {"type": _account, "subtype": None},
            "family": {"type": _family, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "terms": {
                "required": True,
            },
            "account": {
                "required": True,
            },
            "family": {
                "required": True,
            },
        }

        def __init__(
            self,
            terms: List[_terms] = None,
            account: _account = None,
            family: _family = None,
        ):
            pass
            self.__terms = terms
            self.__account = account
            self.__family = family

        def _get_terms(self):
            return self.__terms

        def _set_terms(self, value):
            if not isinstance(value, list):
                raise TypeError("terms must be list")
            if not all(
                isinstance(i, StoreAuthenticateResp._subscriptionStatus._terms)
                for i in value
            ):
                raise TypeError(
                    "terms list values must be StoreAuthenticateResp._subscriptionStatus._terms"
                )

            self.__terms = value

        terms = property(_get_terms, _set_terms)

        def _get_account(self):
            return self.__account

        def _set_account(self, value):
            if not isinstance(
                value, StoreAuthenticateResp._subscriptionStatus._account
            ):
                raise TypeError(
                    "account must be StoreAuthenticateResp._subscriptionStatus._account"
                )

            self.__account = value

        account = property(_get_account, _set_account)

        def _get_family(self):
            return self.__family

        def _set_family(self, value):
            if not isinstance(value, StoreAuthenticateResp._subscriptionStatus._family):
                raise TypeError(
                    "family must be StoreAuthenticateResp._subscriptionStatus._family"
                )

            self.__family = value

        family = property(_get_family, _set_family)

        @staticmethod
        def from_dict(d):
            v = {}
            if "terms" in d:
                v["terms"] = [
                    StoreAuthenticateResp._subscriptionStatus._terms.from_dict(p)
                    if hasattr(
                        StoreAuthenticateResp._subscriptionStatus._terms, "from_dict"
                    )
                    else p
                    for p in d["terms"]
                ]
            if "account" in d:
                v["account"] = (
                    StoreAuthenticateResp._subscriptionStatus._account.from_dict(
                        d["account"]
                    )
                    if hasattr(
                        StoreAuthenticateResp._subscriptionStatus._account, "from_dict"
                    )
                    else d["account"]
                )
            if "family" in d:
                v["family"] = (
                    StoreAuthenticateResp._subscriptionStatus._family.from_dict(
                        d["family"]
                    )
                    if hasattr(
                        StoreAuthenticateResp._subscriptionStatus._family, "from_dict"
                    )
                    else d["family"]
                )
            return StoreAuthenticateResp._subscriptionStatus(**v)

        def as_dict(self):
            d = {}
            if self.__terms is not None:
                d["terms"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p for p in self.__terms
                ]
            if self.__account is not None:
                d["account"] = (
                    self.__account.as_dict()
                    if hasattr(self.__account, "as_dict")
                    else self.__account
                )
            if self.__family is not None:
                d["family"] = (
                    self.__family.as_dict()
                    if hasattr(self.__family, "as_dict")
                    else self.__family
                )
            return d

        def __repr__(self):
            return "<Class _subscriptionStatus. terms: {}, account: {}, family: {}>".format(
                limitedRepr(
                    self.__terms[:20]
                    if isinstance(self.__terms, bytes)
                    else self.__terms
                ),
                limitedRepr(
                    self.__account[:20]
                    if isinstance(self.__account, bytes)
                    else self.__account
                ),
                limitedRepr(
                    self.__family[:20]
                    if isinstance(self.__family, bytes)
                    else self.__family
                ),
            )

    class _download_queue_info:

        _types_map = {
            "download_queue_item_count": {"type": int, "subtype": None},
            "dsid": {"type": int, "subtype": None},
            "is_auto_download_machine": {"type": bool, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "download_queue_item_count": {
                "required": True,
            },
            "dsid": {
                "required": True,
            },
            "is_auto_download_machine": {
                "required": True,
            },
        }

        def __init__(
            self,
            download_queue_item_count: int = None,
            dsid: int = None,
            is_auto_download_machine: bool = None,
        ):
            pass
            self.__download_queue_item_count = download_queue_item_count
            self.__dsid = dsid
            self.__is_auto_download_machine = is_auto_download_machine

        def _get_download_queue_item_count(self):
            return self.__download_queue_item_count

        def _set_download_queue_item_count(self, value):
            if not isinstance(value, int):
                raise TypeError("download_queue_item_count must be int")

            self.__download_queue_item_count = value

        download_queue_item_count = property(
            _get_download_queue_item_count, _set_download_queue_item_count
        )

        def _get_dsid(self):
            return self.__dsid

        def _set_dsid(self, value):
            if not isinstance(value, int):
                raise TypeError("dsid must be int")

            self.__dsid = value

        dsid = property(_get_dsid, _set_dsid)

        def _get_is_auto_download_machine(self):
            return self.__is_auto_download_machine

        def _set_is_auto_download_machine(self, value):
            if not isinstance(value, bool):
                raise TypeError("is_auto_download_machine must be bool")

            self.__is_auto_download_machine = value

        is_auto_download_machine = property(
            _get_is_auto_download_machine, _set_is_auto_download_machine
        )

        @staticmethod
        def from_dict(d):
            v = {}
            if "download-queue-item-count" in d:
                v["download_queue_item_count"] = (
                    int.from_dict(d["download-queue-item-count"])
                    if hasattr(int, "from_dict")
                    else d["download-queue-item-count"]
                )
            if "dsid" in d:
                v["dsid"] = (
                    int.from_dict(d["dsid"]) if hasattr(int, "from_dict") else d["dsid"]
                )
            if "is-auto-download-machine" in d:
                v["is_auto_download_machine"] = (
                    bool.from_dict(d["is-auto-download-machine"])
                    if hasattr(bool, "from_dict")
                    else d["is-auto-download-machine"]
                )
            return StoreAuthenticateResp._download_queue_info(**v)

        def as_dict(self):
            d = {}
            if self.__download_queue_item_count is not None:
                d["download-queue-item-count"] = (
                    self.__download_queue_item_count.as_dict()
                    if hasattr(self.__download_queue_item_count, "as_dict")
                    else self.__download_queue_item_count
                )
            if self.__dsid is not None:
                d["dsid"] = (
                    self.__dsid.as_dict()
                    if hasattr(self.__dsid, "as_dict")
                    else self.__dsid
                )
            if self.__is_auto_download_machine is not None:
                d["is-auto-download-machine"] = (
                    self.__is_auto_download_machine.as_dict()
                    if hasattr(self.__is_auto_download_machine, "as_dict")
                    else self.__is_auto_download_machine
                )
            return d

        def __repr__(self):
            return "<Class _download_queue_info. download_queue_item_count: {}, dsid: {}, is_auto_download_machine: {}>".format(
                limitedRepr(
                    self.__download_queue_item_count[:20]
                    if isinstance(self.__download_queue_item_count, bytes)
                    else self.__download_queue_item_count
                ),
                limitedRepr(
                    self.__dsid[:20] if isinstance(self.__dsid, bytes) else self.__dsid
                ),
                limitedRepr(
                    self.__is_auto_download_machine[:20]
                    if isinstance(self.__is_auto_download_machine, bytes)
                    else self.__is_auto_download_machine
                ),
            )

    class _dialog:

        _types_map = {
            "m_allowed": {"type": bool, "subtype": None},
            "message": {"type": str, "subtype": None},
            "explanation": {"type": str, "subtype": None},
            "defaultButton": {"type": str, "subtype": None},
            "okButtonString": {"type": str, "subtype": None},
            "initialCheckboxValue": {"type": bool, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "m_allowed": {
                "required": True,
            },
            "message": {
                "required": True,
            },
            "explanation": {
                "required": True,
            },
            "defaultButton": {
                "required": True,
            },
            "okButtonString": {
                "required": True,
            },
            "initialCheckboxValue": {
                "required": True,
            },
        }

        def __init__(
            self,
            m_allowed: bool = None,
            message: str = None,
            explanation: str = None,
            defaultButton: str = None,
            okButtonString: str = None,
            initialCheckboxValue: bool = None,
        ):
            pass
            self.__m_allowed = m_allowed
            self.__message = message
            self.__explanation = explanation
            self.__defaultButton = defaultButton
            self.__okButtonString = okButtonString
            self.__initialCheckboxValue = initialCheckboxValue

        def _get_m_allowed(self):
            return self.__m_allowed

        def _set_m_allowed(self, value):
            if not isinstance(value, bool):
                raise TypeError("m_allowed must be bool")

            self.__m_allowed = value

        m_allowed = property(_get_m_allowed, _set_m_allowed)

        def _get_message(self):
            return self.__message

        def _set_message(self, value):
            if not isinstance(value, str):
                raise TypeError("message must be str")

            self.__message = value

        message = property(_get_message, _set_message)

        def _get_explanation(self):
            return self.__explanation

        def _set_explanation(self, value):
            if not isinstance(value, str):
                raise TypeError("explanation must be str")

            self.__explanation = value

        explanation = property(_get_explanation, _set_explanation)

        def _get_defaultButton(self):
            return self.__defaultButton

        def _set_defaultButton(self, value):
            if not isinstance(value, str):
                raise TypeError("defaultButton must be str")

            self.__defaultButton = value

        defaultButton = property(_get_defaultButton, _set_defaultButton)

        def _get_okButtonString(self):
            return self.__okButtonString

        def _set_okButtonString(self, value):
            if not isinstance(value, str):
                raise TypeError("okButtonString must be str")

            self.__okButtonString = value

        okButtonString = property(_get_okButtonString, _set_okButtonString)

        def _get_initialCheckboxValue(self):
            return self.__initialCheckboxValue

        def _set_initialCheckboxValue(self, value):
            if not isinstance(value, bool):
                raise TypeError("initialCheckboxValue must be bool")

            self.__initialCheckboxValue = value

        initialCheckboxValue = property(
            _get_initialCheckboxValue, _set_initialCheckboxValue
        )

        @staticmethod
        def from_dict(d):
            v = {}
            if "m-allowed" in d:
                v["m_allowed"] = (
                    bool.from_dict(d["m-allowed"])
                    if hasattr(bool, "from_dict")
                    else d["m-allowed"]
                )
            if "message" in d:
                v["message"] = (
                    str.from_dict(d["message"])
                    if hasattr(str, "from_dict")
                    else d["message"]
                )
            if "explanation" in d:
                v["explanation"] = (
                    str.from_dict(d["explanation"])
                    if hasattr(str, "from_dict")
                    else d["explanation"]
                )
            if "defaultButton" in d:
                v["defaultButton"] = (
                    str.from_dict(d["defaultButton"])
                    if hasattr(str, "from_dict")
                    else d["defaultButton"]
                )
            if "okButtonString" in d:
                v["okButtonString"] = (
                    str.from_dict(d["okButtonString"])
                    if hasattr(str, "from_dict")
                    else d["okButtonString"]
                )
            if "initialCheckboxValue" in d:
                v["initialCheckboxValue"] = (
                    bool.from_dict(d["initialCheckboxValue"])
                    if hasattr(bool, "from_dict")
                    else d["initialCheckboxValue"]
                )
            return StoreAuthenticateResp._dialog(**v)

        def as_dict(self):
            d = {}
            if self.__m_allowed is not None:
                d["m-allowed"] = (
                    self.__m_allowed.as_dict()
                    if hasattr(self.__m_allowed, "as_dict")
                    else self.__m_allowed
                )
            if self.__message is not None:
                d["message"] = (
                    self.__message.as_dict()
                    if hasattr(self.__message, "as_dict")
                    else self.__message
                )
            if self.__explanation is not None:
                d["explanation"] = (
                    self.__explanation.as_dict()
                    if hasattr(self.__explanation, "as_dict")
                    else self.__explanation
                )
            if self.__defaultButton is not None:
                d["defaultButton"] = (
                    self.__defaultButton.as_dict()
                    if hasattr(self.__defaultButton, "as_dict")
                    else self.__defaultButton
                )
            if self.__okButtonString is not None:
                d["okButtonString"] = (
                    self.__okButtonString.as_dict()
                    if hasattr(self.__okButtonString, "as_dict")
                    else self.__okButtonString
                )
            if self.__initialCheckboxValue is not None:
                d["initialCheckboxValue"] = (
                    self.__initialCheckboxValue.as_dict()
                    if hasattr(self.__initialCheckboxValue, "as_dict")
                    else self.__initialCheckboxValue
                )
            return d

        def __repr__(self):
            return "<Class _dialog. m_allowed: {}, message: {}, explanation: {}, defaultButton: {}, okButtonString: {}, initialCheckboxValue: {}>".format(
                limitedRepr(
                    self.__m_allowed[:20]
                    if isinstance(self.__m_allowed, bytes)
                    else self.__m_allowed
                ),
                limitedRepr(
                    self.__message[:20]
                    if isinstance(self.__message, bytes)
                    else self.__message
                ),
                limitedRepr(
                    self.__explanation[:20]
                    if isinstance(self.__explanation, bytes)
                    else self.__explanation
                ),
                limitedRepr(
                    self.__defaultButton[:20]
                    if isinstance(self.__defaultButton, bytes)
                    else self.__defaultButton
                ),
                limitedRepr(
                    self.__okButtonString[:20]
                    if isinstance(self.__okButtonString, bytes)
                    else self.__okButtonString
                ),
                limitedRepr(
                    self.__initialCheckboxValue[:20]
                    if isinstance(self.__initialCheckboxValue, bytes)
                    else self.__initialCheckboxValue
                ),
            )

    class _privacyAcknowledgement:

        _types_map = {
            "com_apple_onboarding_appstore": {"type": int, "subtype": None},
            "com_apple_onboarding_applemusic": {"type": int, "subtype": None},
            "com_apple_onboarding_videos": {"type": int, "subtype": None},
            "com_apple_onboarding_itunesstore": {"type": int, "subtype": None},
            "com_apple_onboarding_itunesu": {"type": int, "subtype": None},
            "com_apple_onboarding_applearcade": {"type": int, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "com_apple_onboarding_appstore": {
                "required": True,
            },
            "com_apple_onboarding_applemusic": {
                "required": True,
            },
            "com_apple_onboarding_videos": {
                "required": True,
            },
            "com_apple_onboarding_itunesstore": {
                "required": True,
            },
            "com_apple_onboarding_itunesu": {
                "required": True,
            },
            "com_apple_onboarding_applearcade": {
                "required": True,
            },
        }

        def __init__(
            self,
            com_apple_onboarding_appstore: int = None,
            com_apple_onboarding_applemusic: int = None,
            com_apple_onboarding_videos: int = None,
            com_apple_onboarding_itunesstore: int = None,
            com_apple_onboarding_itunesu: int = None,
            com_apple_onboarding_applearcade: int = None,
        ):
            pass
            self.__com_apple_onboarding_appstore = com_apple_onboarding_appstore
            self.__com_apple_onboarding_applemusic = com_apple_onboarding_applemusic
            self.__com_apple_onboarding_videos = com_apple_onboarding_videos
            self.__com_apple_onboarding_itunesstore = com_apple_onboarding_itunesstore
            self.__com_apple_onboarding_itunesu = com_apple_onboarding_itunesu
            self.__com_apple_onboarding_applearcade = com_apple_onboarding_applearcade

        def _get_com_apple_onboarding_appstore(self):
            return self.__com_apple_onboarding_appstore

        def _set_com_apple_onboarding_appstore(self, value):
            if not isinstance(value, int):
                raise TypeError("com_apple_onboarding_appstore must be int")

            self.__com_apple_onboarding_appstore = value

        com_apple_onboarding_appstore = property(
            _get_com_apple_onboarding_appstore, _set_com_apple_onboarding_appstore
        )

        def _get_com_apple_onboarding_applemusic(self):
            return self.__com_apple_onboarding_applemusic

        def _set_com_apple_onboarding_applemusic(self, value):
            if not isinstance(value, int):
                raise TypeError("com_apple_onboarding_applemusic must be int")

            self.__com_apple_onboarding_applemusic = value

        com_apple_onboarding_applemusic = property(
            _get_com_apple_onboarding_applemusic, _set_com_apple_onboarding_applemusic
        )

        def _get_com_apple_onboarding_videos(self):
            return self.__com_apple_onboarding_videos

        def _set_com_apple_onboarding_videos(self, value):
            if not isinstance(value, int):
                raise TypeError("com_apple_onboarding_videos must be int")

            self.__com_apple_onboarding_videos = value

        com_apple_onboarding_videos = property(
            _get_com_apple_onboarding_videos, _set_com_apple_onboarding_videos
        )

        def _get_com_apple_onboarding_itunesstore(self):
            return self.__com_apple_onboarding_itunesstore

        def _set_com_apple_onboarding_itunesstore(self, value):
            if not isinstance(value, int):
                raise TypeError("com_apple_onboarding_itunesstore must be int")

            self.__com_apple_onboarding_itunesstore = value

        com_apple_onboarding_itunesstore = property(
            _get_com_apple_onboarding_itunesstore, _set_com_apple_onboarding_itunesstore
        )

        def _get_com_apple_onboarding_itunesu(self):
            return self.__com_apple_onboarding_itunesu

        def _set_com_apple_onboarding_itunesu(self, value):
            if not isinstance(value, int):
                raise TypeError("com_apple_onboarding_itunesu must be int")

            self.__com_apple_onboarding_itunesu = value

        com_apple_onboarding_itunesu = property(
            _get_com_apple_onboarding_itunesu, _set_com_apple_onboarding_itunesu
        )

        def _get_com_apple_onboarding_applearcade(self):
            return self.__com_apple_onboarding_applearcade

        def _set_com_apple_onboarding_applearcade(self, value):
            if not isinstance(value, int):
                raise TypeError("com_apple_onboarding_applearcade must be int")

            self.__com_apple_onboarding_applearcade = value

        com_apple_onboarding_applearcade = property(
            _get_com_apple_onboarding_applearcade, _set_com_apple_onboarding_applearcade
        )

        @staticmethod
        def from_dict(d):
            v = {}
            if "com.apple.onboarding.appstore" in d:
                v["com_apple_onboarding_appstore"] = (
                    int.from_dict(d["com.apple.onboarding.appstore"])
                    if hasattr(int, "from_dict")
                    else d["com.apple.onboarding.appstore"]
                )
            if "com.apple.onboarding.applemusic" in d:
                v["com_apple_onboarding_applemusic"] = (
                    int.from_dict(d["com.apple.onboarding.applemusic"])
                    if hasattr(int, "from_dict")
                    else d["com.apple.onboarding.applemusic"]
                )
            if "com.apple.onboarding.videos" in d:
                v["com_apple_onboarding_videos"] = (
                    int.from_dict(d["com.apple.onboarding.videos"])
                    if hasattr(int, "from_dict")
                    else d["com.apple.onboarding.videos"]
                )
            if "com.apple.onboarding.itunesstore" in d:
                v["com_apple_onboarding_itunesstore"] = (
                    int.from_dict(d["com.apple.onboarding.itunesstore"])
                    if hasattr(int, "from_dict")
                    else d["com.apple.onboarding.itunesstore"]
                )
            if "com.apple.onboarding.itunesu" in d:
                v["com_apple_onboarding_itunesu"] = (
                    int.from_dict(d["com.apple.onboarding.itunesu"])
                    if hasattr(int, "from_dict")
                    else d["com.apple.onboarding.itunesu"]
                )
            if "com.apple.onboarding.applearcade" in d:
                v["com_apple_onboarding_applearcade"] = (
                    int.from_dict(d["com.apple.onboarding.applearcade"])
                    if hasattr(int, "from_dict")
                    else d["com.apple.onboarding.applearcade"]
                )
            return StoreAuthenticateResp._privacyAcknowledgement(**v)

        def as_dict(self):
            d = {}
            if self.__com_apple_onboarding_appstore is not None:
                d["com.apple.onboarding.appstore"] = (
                    self.__com_apple_onboarding_appstore.as_dict()
                    if hasattr(self.__com_apple_onboarding_appstore, "as_dict")
                    else self.__com_apple_onboarding_appstore
                )
            if self.__com_apple_onboarding_applemusic is not None:
                d["com.apple.onboarding.applemusic"] = (
                    self.__com_apple_onboarding_applemusic.as_dict()
                    if hasattr(self.__com_apple_onboarding_applemusic, "as_dict")
                    else self.__com_apple_onboarding_applemusic
                )
            if self.__com_apple_onboarding_videos is not None:
                d["com.apple.onboarding.videos"] = (
                    self.__com_apple_onboarding_videos.as_dict()
                    if hasattr(self.__com_apple_onboarding_videos, "as_dict")
                    else self.__com_apple_onboarding_videos
                )
            if self.__com_apple_onboarding_itunesstore is not None:
                d["com.apple.onboarding.itunesstore"] = (
                    self.__com_apple_onboarding_itunesstore.as_dict()
                    if hasattr(self.__com_apple_onboarding_itunesstore, "as_dict")
                    else self.__com_apple_onboarding_itunesstore
                )
            if self.__com_apple_onboarding_itunesu is not None:
                d["com.apple.onboarding.itunesu"] = (
                    self.__com_apple_onboarding_itunesu.as_dict()
                    if hasattr(self.__com_apple_onboarding_itunesu, "as_dict")
                    else self.__com_apple_onboarding_itunesu
                )
            if self.__com_apple_onboarding_applearcade is not None:
                d["com.apple.onboarding.applearcade"] = (
                    self.__com_apple_onboarding_applearcade.as_dict()
                    if hasattr(self.__com_apple_onboarding_applearcade, "as_dict")
                    else self.__com_apple_onboarding_applearcade
                )
            return d

        def __repr__(self):
            return "<Class _privacyAcknowledgement. com_apple_onboarding_appstore: {}, com_apple_onboarding_applemusic: {}, com_apple_onboarding_videos: {}, com_apple_onboarding_itunesstore: {}, com_apple_onboarding_itunesu: {}, com_apple_onboarding_applearcade: {}>".format(
                limitedRepr(
                    self.__com_apple_onboarding_appstore[:20]
                    if isinstance(self.__com_apple_onboarding_appstore, bytes)
                    else self.__com_apple_onboarding_appstore
                ),
                limitedRepr(
                    self.__com_apple_onboarding_applemusic[:20]
                    if isinstance(self.__com_apple_onboarding_applemusic, bytes)
                    else self.__com_apple_onboarding_applemusic
                ),
                limitedRepr(
                    self.__com_apple_onboarding_videos[:20]
                    if isinstance(self.__com_apple_onboarding_videos, bytes)
                    else self.__com_apple_onboarding_videos
                ),
                limitedRepr(
                    self.__com_apple_onboarding_itunesstore[:20]
                    if isinstance(self.__com_apple_onboarding_itunesstore, bytes)
                    else self.__com_apple_onboarding_itunesstore
                ),
                limitedRepr(
                    self.__com_apple_onboarding_itunesu[:20]
                    if isinstance(self.__com_apple_onboarding_itunesu, bytes)
                    else self.__com_apple_onboarding_itunesu
                ),
                limitedRepr(
                    self.__com_apple_onboarding_applearcade[:20]
                    if isinstance(self.__com_apple_onboarding_applearcade, bytes)
                    else self.__com_apple_onboarding_applearcade
                ),
            )

    class _action:

        _types_map = {
            "kind": {"type": str, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "kind": {
                "required": True,
            },
        }

        def __init__(self, kind: str = None):
            pass
            self.__kind = kind

        def _get_kind(self):
            return self.__kind

        def _set_kind(self, value):
            if not isinstance(value, str):
                raise TypeError("kind must be str")

            self.__kind = value

        kind = property(_get_kind, _set_kind)

        @staticmethod
        def from_dict(d):
            v = {}
            if "kind" in d:
                v["kind"] = (
                    str.from_dict(d["kind"]) if hasattr(str, "from_dict") else d["kind"]
                )
            return StoreAuthenticateResp._action(**v)

        def as_dict(self):
            d = {}
            if self.__kind is not None:
                d["kind"] = (
                    self.__kind.as_dict()
                    if hasattr(self.__kind, "as_dict")
                    else self.__kind
                )
            return d

        def __repr__(self):
            return "<Class _action. kind: {}>".format(
                limitedRepr(
                    self.__kind[:20] if isinstance(self.__kind, bytes) else self.__kind
                )
            )

    class _accountInfo:
        class _address:

            _types_map = {
                "firstName": {"type": str, "subtype": None},
                "lastName": {"type": str, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "firstName": {
                    "required": True,
                },
                "lastName": {
                    "required": True,
                },
            }

            def __init__(self, firstName: str = None, lastName: str = None):
                pass
                self.__firstName = firstName
                self.__lastName = lastName

            def _get_firstName(self):
                return self.__firstName

            def _set_firstName(self, value):
                if not isinstance(value, str):
                    raise TypeError("firstName must be str")

                self.__firstName = value

            firstName = property(_get_firstName, _set_firstName)

            def _get_lastName(self):
                return self.__lastName

            def _set_lastName(self, value):
                if not isinstance(value, str):
                    raise TypeError("lastName must be str")

                self.__lastName = value

            lastName = property(_get_lastName, _set_lastName)

            @staticmethod
            def from_dict(d):
                v = {}
                if "firstName" in d:
                    v["firstName"] = (
                        str.from_dict(d["firstName"])
                        if hasattr(str, "from_dict")
                        else d["firstName"]
                    )
                if "lastName" in d:
                    v["lastName"] = (
                        str.from_dict(d["lastName"])
                        if hasattr(str, "from_dict")
                        else d["lastName"]
                    )
                return StoreAuthenticateResp._accountInfo._address(**v)

            def as_dict(self):
                d = {}
                if self.__firstName is not None:
                    d["firstName"] = (
                        self.__firstName.as_dict()
                        if hasattr(self.__firstName, "as_dict")
                        else self.__firstName
                    )
                if self.__lastName is not None:
                    d["lastName"] = (
                        self.__lastName.as_dict()
                        if hasattr(self.__lastName, "as_dict")
                        else self.__lastName
                    )
                return d

            def __repr__(self):
                return "<Class _address. firstName: {}, lastName: {}>".format(
                    limitedRepr(
                        self.__firstName[:20]
                        if isinstance(self.__firstName, bytes)
                        else self.__firstName
                    ),
                    limitedRepr(
                        self.__lastName[:20]
                        if isinstance(self.__lastName, bytes)
                        else self.__lastName
                    ),
                )

        _types_map = {
            "appleId": {"type": str, "subtype": None},
            "address": {"type": _address, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "appleId": {
                "required": True,
            },
            "address": {
                "required": True,
            },
        }

        def __init__(self, appleId: str = None, address: _address = None):
            pass
            self.__appleId = appleId
            self.__address = address

        def _get_appleId(self):
            return self.__appleId

        def _set_appleId(self, value):
            if not isinstance(value, str):
                raise TypeError("appleId must be str")

            self.__appleId = value

        appleId = property(_get_appleId, _set_appleId)

        def _get_address(self):
            return self.__address

        def _set_address(self, value):
            if not isinstance(value, StoreAuthenticateResp._accountInfo._address):
                raise TypeError(
                    "address must be StoreAuthenticateResp._accountInfo._address"
                )

            self.__address = value

        address = property(_get_address, _set_address)

        @staticmethod
        def from_dict(d):
            v = {}
            if "appleId" in d:
                v["appleId"] = (
                    str.from_dict(d["appleId"])
                    if hasattr(str, "from_dict")
                    else d["appleId"]
                )
            if "address" in d:
                v["address"] = (
                    StoreAuthenticateResp._accountInfo._address.from_dict(d["address"])
                    if hasattr(StoreAuthenticateResp._accountInfo._address, "from_dict")
                    else d["address"]
                )
            return StoreAuthenticateResp._accountInfo(**v)

        def as_dict(self):
            d = {}
            if self.__appleId is not None:
                d["appleId"] = (
                    self.__appleId.as_dict()
                    if hasattr(self.__appleId, "as_dict")
                    else self.__appleId
                )
            if self.__address is not None:
                d["address"] = (
                    self.__address.as_dict()
                    if hasattr(self.__address, "as_dict")
                    else self.__address
                )
            return d

        def __repr__(self):
            return "<Class _accountInfo. appleId: {}, address: {}>".format(
                limitedRepr(
                    self.__appleId[:20]
                    if isinstance(self.__appleId, bytes)
                    else self.__appleId
                ),
                limitedRepr(
                    self.__address[:20]
                    if isinstance(self.__address, bytes)
                    else self.__address
                ),
            )

    class _accountFlags:

        _types_map = {
            "personalization": {"type": bool, "subtype": None},
            "underThirteen": {"type": bool, "subtype": None},
            "identityLastVerified": {"type": int, "subtype": None},
            "verifiedExpirationDate": {"type": int, "subtype": None},
            "retailDemo": {"type": bool, "subtype": None},
            "autoPlay": {"type": bool, "subtype": None},
            "isDisabledAccount": {"type": bool, "subtype": None},
            "isRestrictedAccount": {"type": bool, "subtype": None},
            "isManagedAccount": {"type": bool, "subtype": None},
            "isInRestrictedRegion": {"type": bool, "subtype": None},
            "accountFlagsVersion": {"type": int, "subtype": None},
            "hasAgreedToTerms": {"type": bool, "subtype": None},
            "hasAgreedToAppClipTerms": {"type": bool, "subtype": None},
            "hasWatchHardwareOffer": {"type": bool, "subtype": None},
            "isInFamily": {"type": bool, "subtype": None},
            "hasSubscriptionFamilySharingEnabled": {"type": bool, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "personalization": {
                "required": True,
            },
            "underThirteen": {
                "required": True,
            },
            "identityLastVerified": {
                "required": True,
            },
            "verifiedExpirationDate": {
                "required": True,
            },
            "retailDemo": {
                "required": True,
            },
            "autoPlay": {
                "required": True,
            },
            "isDisabledAccount": {
                "required": True,
            },
            "isRestrictedAccount": {
                "required": True,
            },
            "isManagedAccount": {
                "required": True,
            },
            "isInRestrictedRegion": {
                "required": True,
            },
            "accountFlagsVersion": {
                "required": True,
            },
            "hasAgreedToTerms": {
                "required": True,
            },
            "hasAgreedToAppClipTerms": {
                "required": True,
            },
            "hasWatchHardwareOffer": {
                "required": True,
            },
            "isInFamily": {
                "required": True,
            },
            "hasSubscriptionFamilySharingEnabled": {
                "required": True,
            },
        }

        def __init__(
            self,
            personalization: bool = None,
            underThirteen: bool = None,
            identityLastVerified: int = None,
            verifiedExpirationDate: int = None,
            retailDemo: bool = None,
            autoPlay: bool = None,
            isDisabledAccount: bool = None,
            isRestrictedAccount: bool = None,
            isManagedAccount: bool = None,
            isInRestrictedRegion: bool = None,
            accountFlagsVersion: int = None,
            hasAgreedToTerms: bool = None,
            hasAgreedToAppClipTerms: bool = None,
            hasWatchHardwareOffer: bool = None,
            isInFamily: bool = None,
            hasSubscriptionFamilySharingEnabled: bool = None,
        ):
            pass
            self.__personalization = personalization
            self.__underThirteen = underThirteen
            self.__identityLastVerified = identityLastVerified
            self.__verifiedExpirationDate = verifiedExpirationDate
            self.__retailDemo = retailDemo
            self.__autoPlay = autoPlay
            self.__isDisabledAccount = isDisabledAccount
            self.__isRestrictedAccount = isRestrictedAccount
            self.__isManagedAccount = isManagedAccount
            self.__isInRestrictedRegion = isInRestrictedRegion
            self.__accountFlagsVersion = accountFlagsVersion
            self.__hasAgreedToTerms = hasAgreedToTerms
            self.__hasAgreedToAppClipTerms = hasAgreedToAppClipTerms
            self.__hasWatchHardwareOffer = hasWatchHardwareOffer
            self.__isInFamily = isInFamily
            self.__hasSubscriptionFamilySharingEnabled = (
                hasSubscriptionFamilySharingEnabled
            )

        def _get_personalization(self):
            return self.__personalization

        def _set_personalization(self, value):
            if not isinstance(value, bool):
                raise TypeError("personalization must be bool")

            self.__personalization = value

        personalization = property(_get_personalization, _set_personalization)

        def _get_underThirteen(self):
            return self.__underThirteen

        def _set_underThirteen(self, value):
            if not isinstance(value, bool):
                raise TypeError("underThirteen must be bool")

            self.__underThirteen = value

        underThirteen = property(_get_underThirteen, _set_underThirteen)

        def _get_identityLastVerified(self):
            return self.__identityLastVerified

        def _set_identityLastVerified(self, value):
            if not isinstance(value, int):
                raise TypeError("identityLastVerified must be int")

            self.__identityLastVerified = value

        identityLastVerified = property(
            _get_identityLastVerified, _set_identityLastVerified
        )

        def _get_verifiedExpirationDate(self):
            return self.__verifiedExpirationDate

        def _set_verifiedExpirationDate(self, value):
            if not isinstance(value, int):
                raise TypeError("verifiedExpirationDate must be int")

            self.__verifiedExpirationDate = value

        verifiedExpirationDate = property(
            _get_verifiedExpirationDate, _set_verifiedExpirationDate
        )

        def _get_retailDemo(self):
            return self.__retailDemo

        def _set_retailDemo(self, value):
            if not isinstance(value, bool):
                raise TypeError("retailDemo must be bool")

            self.__retailDemo = value

        retailDemo = property(_get_retailDemo, _set_retailDemo)

        def _get_autoPlay(self):
            return self.__autoPlay

        def _set_autoPlay(self, value):
            if not isinstance(value, bool):
                raise TypeError("autoPlay must be bool")

            self.__autoPlay = value

        autoPlay = property(_get_autoPlay, _set_autoPlay)

        def _get_isDisabledAccount(self):
            return self.__isDisabledAccount

        def _set_isDisabledAccount(self, value):
            if not isinstance(value, bool):
                raise TypeError("isDisabledAccount must be bool")

            self.__isDisabledAccount = value

        isDisabledAccount = property(_get_isDisabledAccount, _set_isDisabledAccount)

        def _get_isRestrictedAccount(self):
            return self.__isRestrictedAccount

        def _set_isRestrictedAccount(self, value):
            if not isinstance(value, bool):
                raise TypeError("isRestrictedAccount must be bool")

            self.__isRestrictedAccount = value

        isRestrictedAccount = property(
            _get_isRestrictedAccount, _set_isRestrictedAccount
        )

        def _get_isManagedAccount(self):
            return self.__isManagedAccount

        def _set_isManagedAccount(self, value):
            if not isinstance(value, bool):
                raise TypeError("isManagedAccount must be bool")

            self.__isManagedAccount = value

        isManagedAccount = property(_get_isManagedAccount, _set_isManagedAccount)

        def _get_isInRestrictedRegion(self):
            return self.__isInRestrictedRegion

        def _set_isInRestrictedRegion(self, value):
            if not isinstance(value, bool):
                raise TypeError("isInRestrictedRegion must be bool")

            self.__isInRestrictedRegion = value

        isInRestrictedRegion = property(
            _get_isInRestrictedRegion, _set_isInRestrictedRegion
        )

        def _get_accountFlagsVersion(self):
            return self.__accountFlagsVersion

        def _set_accountFlagsVersion(self, value):
            if not isinstance(value, int):
                raise TypeError("accountFlagsVersion must be int")

            self.__accountFlagsVersion = value

        accountFlagsVersion = property(
            _get_accountFlagsVersion, _set_accountFlagsVersion
        )

        def _get_hasAgreedToTerms(self):
            return self.__hasAgreedToTerms

        def _set_hasAgreedToTerms(self, value):
            if not isinstance(value, bool):
                raise TypeError("hasAgreedToTerms must be bool")

            self.__hasAgreedToTerms = value

        hasAgreedToTerms = property(_get_hasAgreedToTerms, _set_hasAgreedToTerms)

        def _get_hasAgreedToAppClipTerms(self):
            return self.__hasAgreedToAppClipTerms

        def _set_hasAgreedToAppClipTerms(self, value):
            if not isinstance(value, bool):
                raise TypeError("hasAgreedToAppClipTerms must be bool")

            self.__hasAgreedToAppClipTerms = value

        hasAgreedToAppClipTerms = property(
            _get_hasAgreedToAppClipTerms, _set_hasAgreedToAppClipTerms
        )

        def _get_hasWatchHardwareOffer(self):
            return self.__hasWatchHardwareOffer

        def _set_hasWatchHardwareOffer(self, value):
            if not isinstance(value, bool):
                raise TypeError("hasWatchHardwareOffer must be bool")

            self.__hasWatchHardwareOffer = value

        hasWatchHardwareOffer = property(
            _get_hasWatchHardwareOffer, _set_hasWatchHardwareOffer
        )

        def _get_isInFamily(self):
            return self.__isInFamily

        def _set_isInFamily(self, value):
            if not isinstance(value, bool):
                raise TypeError("isInFamily must be bool")

            self.__isInFamily = value

        isInFamily = property(_get_isInFamily, _set_isInFamily)

        def _get_hasSubscriptionFamilySharingEnabled(self):
            return self.__hasSubscriptionFamilySharingEnabled

        def _set_hasSubscriptionFamilySharingEnabled(self, value):
            if not isinstance(value, bool):
                raise TypeError("hasSubscriptionFamilySharingEnabled must be bool")

            self.__hasSubscriptionFamilySharingEnabled = value

        hasSubscriptionFamilySharingEnabled = property(
            _get_hasSubscriptionFamilySharingEnabled,
            _set_hasSubscriptionFamilySharingEnabled,
        )

        @staticmethod
        def from_dict(d):
            v = {}
            if "personalization" in d:
                v["personalization"] = (
                    bool.from_dict(d["personalization"])
                    if hasattr(bool, "from_dict")
                    else d["personalization"]
                )
            if "underThirteen" in d:
                v["underThirteen"] = (
                    bool.from_dict(d["underThirteen"])
                    if hasattr(bool, "from_dict")
                    else d["underThirteen"]
                )
            if "identityLastVerified" in d:
                v["identityLastVerified"] = (
                    int.from_dict(d["identityLastVerified"])
                    if hasattr(int, "from_dict")
                    else d["identityLastVerified"]
                )
            if "verifiedExpirationDate" in d:
                v["verifiedExpirationDate"] = (
                    int.from_dict(d["verifiedExpirationDate"])
                    if hasattr(int, "from_dict")
                    else d["verifiedExpirationDate"]
                )
            if "retailDemo" in d:
                v["retailDemo"] = (
                    bool.from_dict(d["retailDemo"])
                    if hasattr(bool, "from_dict")
                    else d["retailDemo"]
                )
            if "autoPlay" in d:
                v["autoPlay"] = (
                    bool.from_dict(d["autoPlay"])
                    if hasattr(bool, "from_dict")
                    else d["autoPlay"]
                )
            if "isDisabledAccount" in d:
                v["isDisabledAccount"] = (
                    bool.from_dict(d["isDisabledAccount"])
                    if hasattr(bool, "from_dict")
                    else d["isDisabledAccount"]
                )
            if "isRestrictedAccount" in d:
                v["isRestrictedAccount"] = (
                    bool.from_dict(d["isRestrictedAccount"])
                    if hasattr(bool, "from_dict")
                    else d["isRestrictedAccount"]
                )
            if "isManagedAccount" in d:
                v["isManagedAccount"] = (
                    bool.from_dict(d["isManagedAccount"])
                    if hasattr(bool, "from_dict")
                    else d["isManagedAccount"]
                )
            if "isInRestrictedRegion" in d:
                v["isInRestrictedRegion"] = (
                    bool.from_dict(d["isInRestrictedRegion"])
                    if hasattr(bool, "from_dict")
                    else d["isInRestrictedRegion"]
                )
            if "accountFlagsVersion" in d:
                v["accountFlagsVersion"] = (
                    int.from_dict(d["accountFlagsVersion"])
                    if hasattr(int, "from_dict")
                    else d["accountFlagsVersion"]
                )
            if "hasAgreedToTerms" in d:
                v["hasAgreedToTerms"] = (
                    bool.from_dict(d["hasAgreedToTerms"])
                    if hasattr(bool, "from_dict")
                    else d["hasAgreedToTerms"]
                )
            if "hasAgreedToAppClipTerms" in d:
                v["hasAgreedToAppClipTerms"] = (
                    bool.from_dict(d["hasAgreedToAppClipTerms"])
                    if hasattr(bool, "from_dict")
                    else d["hasAgreedToAppClipTerms"]
                )
            if "hasWatchHardwareOffer" in d:
                v["hasWatchHardwareOffer"] = (
                    bool.from_dict(d["hasWatchHardwareOffer"])
                    if hasattr(bool, "from_dict")
                    else d["hasWatchHardwareOffer"]
                )
            if "isInFamily" in d:
                v["isInFamily"] = (
                    bool.from_dict(d["isInFamily"])
                    if hasattr(bool, "from_dict")
                    else d["isInFamily"]
                )
            if "hasSubscriptionFamilySharingEnabled" in d:
                v["hasSubscriptionFamilySharingEnabled"] = (
                    bool.from_dict(d["hasSubscriptionFamilySharingEnabled"])
                    if hasattr(bool, "from_dict")
                    else d["hasSubscriptionFamilySharingEnabled"]
                )
            return StoreAuthenticateResp._accountFlags(**v)

        def as_dict(self):
            d = {}
            if self.__personalization is not None:
                d["personalization"] = (
                    self.__personalization.as_dict()
                    if hasattr(self.__personalization, "as_dict")
                    else self.__personalization
                )
            if self.__underThirteen is not None:
                d["underThirteen"] = (
                    self.__underThirteen.as_dict()
                    if hasattr(self.__underThirteen, "as_dict")
                    else self.__underThirteen
                )
            if self.__identityLastVerified is not None:
                d["identityLastVerified"] = (
                    self.__identityLastVerified.as_dict()
                    if hasattr(self.__identityLastVerified, "as_dict")
                    else self.__identityLastVerified
                )
            if self.__verifiedExpirationDate is not None:
                d["verifiedExpirationDate"] = (
                    self.__verifiedExpirationDate.as_dict()
                    if hasattr(self.__verifiedExpirationDate, "as_dict")
                    else self.__verifiedExpirationDate
                )
            if self.__retailDemo is not None:
                d["retailDemo"] = (
                    self.__retailDemo.as_dict()
                    if hasattr(self.__retailDemo, "as_dict")
                    else self.__retailDemo
                )
            if self.__autoPlay is not None:
                d["autoPlay"] = (
                    self.__autoPlay.as_dict()
                    if hasattr(self.__autoPlay, "as_dict")
                    else self.__autoPlay
                )
            if self.__isDisabledAccount is not None:
                d["isDisabledAccount"] = (
                    self.__isDisabledAccount.as_dict()
                    if hasattr(self.__isDisabledAccount, "as_dict")
                    else self.__isDisabledAccount
                )
            if self.__isRestrictedAccount is not None:
                d["isRestrictedAccount"] = (
                    self.__isRestrictedAccount.as_dict()
                    if hasattr(self.__isRestrictedAccount, "as_dict")
                    else self.__isRestrictedAccount
                )
            if self.__isManagedAccount is not None:
                d["isManagedAccount"] = (
                    self.__isManagedAccount.as_dict()
                    if hasattr(self.__isManagedAccount, "as_dict")
                    else self.__isManagedAccount
                )
            if self.__isInRestrictedRegion is not None:
                d["isInRestrictedRegion"] = (
                    self.__isInRestrictedRegion.as_dict()
                    if hasattr(self.__isInRestrictedRegion, "as_dict")
                    else self.__isInRestrictedRegion
                )
            if self.__accountFlagsVersion is not None:
                d["accountFlagsVersion"] = (
                    self.__accountFlagsVersion.as_dict()
                    if hasattr(self.__accountFlagsVersion, "as_dict")
                    else self.__accountFlagsVersion
                )
            if self.__hasAgreedToTerms is not None:
                d["hasAgreedToTerms"] = (
                    self.__hasAgreedToTerms.as_dict()
                    if hasattr(self.__hasAgreedToTerms, "as_dict")
                    else self.__hasAgreedToTerms
                )
            if self.__hasAgreedToAppClipTerms is not None:
                d["hasAgreedToAppClipTerms"] = (
                    self.__hasAgreedToAppClipTerms.as_dict()
                    if hasattr(self.__hasAgreedToAppClipTerms, "as_dict")
                    else self.__hasAgreedToAppClipTerms
                )
            if self.__hasWatchHardwareOffer is not None:
                d["hasWatchHardwareOffer"] = (
                    self.__hasWatchHardwareOffer.as_dict()
                    if hasattr(self.__hasWatchHardwareOffer, "as_dict")
                    else self.__hasWatchHardwareOffer
                )
            if self.__isInFamily is not None:
                d["isInFamily"] = (
                    self.__isInFamily.as_dict()
                    if hasattr(self.__isInFamily, "as_dict")
                    else self.__isInFamily
                )
            if self.__hasSubscriptionFamilySharingEnabled is not None:
                d["hasSubscriptionFamilySharingEnabled"] = (
                    self.__hasSubscriptionFamilySharingEnabled.as_dict()
                    if hasattr(self.__hasSubscriptionFamilySharingEnabled, "as_dict")
                    else self.__hasSubscriptionFamilySharingEnabled
                )
            return d

        def __repr__(self):
            return "<Class _accountFlags. personalization: {}, underThirteen: {}, identityLastVerified: {}, verifiedExpirationDate: {}, retailDemo: {}, autoPlay: {}, isDisabledAccount: {}, isRestrictedAccount: {}, isManagedAccount: {}, isInRestrictedRegion: {}, accountFlagsVersion: {}, hasAgreedToTerms: {}, hasAgreedToAppClipTerms: {}, hasWatchHardwareOffer: {}, isInFamily: {}, hasSubscriptionFamilySharingEnabled: {}>".format(
                limitedRepr(
                    self.__personalization[:20]
                    if isinstance(self.__personalization, bytes)
                    else self.__personalization
                ),
                limitedRepr(
                    self.__underThirteen[:20]
                    if isinstance(self.__underThirteen, bytes)
                    else self.__underThirteen
                ),
                limitedRepr(
                    self.__identityLastVerified[:20]
                    if isinstance(self.__identityLastVerified, bytes)
                    else self.__identityLastVerified
                ),
                limitedRepr(
                    self.__verifiedExpirationDate[:20]
                    if isinstance(self.__verifiedExpirationDate, bytes)
                    else self.__verifiedExpirationDate
                ),
                limitedRepr(
                    self.__retailDemo[:20]
                    if isinstance(self.__retailDemo, bytes)
                    else self.__retailDemo
                ),
                limitedRepr(
                    self.__autoPlay[:20]
                    if isinstance(self.__autoPlay, bytes)
                    else self.__autoPlay
                ),
                limitedRepr(
                    self.__isDisabledAccount[:20]
                    if isinstance(self.__isDisabledAccount, bytes)
                    else self.__isDisabledAccount
                ),
                limitedRepr(
                    self.__isRestrictedAccount[:20]
                    if isinstance(self.__isRestrictedAccount, bytes)
                    else self.__isRestrictedAccount
                ),
                limitedRepr(
                    self.__isManagedAccount[:20]
                    if isinstance(self.__isManagedAccount, bytes)
                    else self.__isManagedAccount
                ),
                limitedRepr(
                    self.__isInRestrictedRegion[:20]
                    if isinstance(self.__isInRestrictedRegion, bytes)
                    else self.__isInRestrictedRegion
                ),
                limitedRepr(
                    self.__accountFlagsVersion[:20]
                    if isinstance(self.__accountFlagsVersion, bytes)
                    else self.__accountFlagsVersion
                ),
                limitedRepr(
                    self.__hasAgreedToTerms[:20]
                    if isinstance(self.__hasAgreedToTerms, bytes)
                    else self.__hasAgreedToTerms
                ),
                limitedRepr(
                    self.__hasAgreedToAppClipTerms[:20]
                    if isinstance(self.__hasAgreedToAppClipTerms, bytes)
                    else self.__hasAgreedToAppClipTerms
                ),
                limitedRepr(
                    self.__hasWatchHardwareOffer[:20]
                    if isinstance(self.__hasWatchHardwareOffer, bytes)
                    else self.__hasWatchHardwareOffer
                ),
                limitedRepr(
                    self.__isInFamily[:20]
                    if isinstance(self.__isInFamily, bytes)
                    else self.__isInFamily
                ),
                limitedRepr(
                    self.__hasSubscriptionFamilySharingEnabled[:20]
                    if isinstance(self.__hasSubscriptionFamilySharingEnabled, bytes)
                    else self.__hasSubscriptionFamilySharingEnabled
                ),
            )

    _types_map = {
        "pings": {"type": list, "subtype": float},
        "cancel_purchase_batch": {"type": bool, "subtype": None},
        "customerMessage": {"type": str, "subtype": None},
        "failureType": {"type": str, "subtype": None},
        "accountInfo": {"type": _accountInfo, "subtype": None},
        "passwordToken": {"type": str, "subtype": None},
        "clearToken": {"type": str, "subtype": None},
        "m_allowed": {"type": bool, "subtype": None},
        "is_cloud_enabled": {"type": str, "subtype": None},
        "dsPersonId": {"type": str, "subtype": None},
        "creditDisplay": {"type": str, "subtype": None},
        "creditBalance": {"type": str, "subtype": None},
        "freeSongBalance": {"type": str, "subtype": None},
        "isManagedStudent": {"type": bool, "subtype": None},
        "action": {"type": _action, "subtype": None},
        "subscriptionStatus": {"type": _subscriptionStatus, "subtype": None},
        "accountFlags": {"type": _accountFlags, "subtype": None},
        "status": {"type": int, "subtype": None},
        "download_queue_info": {"type": _download_queue_info, "subtype": None},
        "privacyAcknowledgement": {"type": _privacyAcknowledgement, "subtype": None},
        "dialog": {"type": _dialog, "subtype": None},
    }
    _formats_map = {}
    _validations_map = {
        "pings": {
            "required": True,
        },
        "cancel_purchase_batch": {
            "required": False,
        },
        "customerMessage": {
            "required": False,
        },
        "failureType": {
            "required": False,
        },
        "accountInfo": {
            "required": True,
        },
        "passwordToken": {
            "required": True,
        },
        "clearToken": {
            "required": True,
        },
        "m_allowed": {
            "required": True,
        },
        "is_cloud_enabled": {
            "required": True,
        },
        "dsPersonId": {
            "required": True,
        },
        "creditDisplay": {
            "required": True,
        },
        "creditBalance": {
            "required": True,
        },
        "freeSongBalance": {
            "required": True,
        },
        "isManagedStudent": {
            "required": True,
        },
        "action": {
            "required": True,
        },
        "subscriptionStatus": {
            "required": True,
        },
        "accountFlags": {
            "required": True,
        },
        "status": {
            "required": True,
        },
        "download_queue_info": {
            "required": True,
        },
        "privacyAcknowledgement": {
            "required": True,
        },
        "dialog": {
            "required": True,
        },
    }

    def __init__(
        self,
        pings: List[float] = None,
        cancel_purchase_batch: bool = None,
        customerMessage: str = None,
        failureType: str = None,
        accountInfo: _accountInfo = None,
        passwordToken: str = None,
        clearToken: str = None,
        m_allowed: bool = None,
        is_cloud_enabled: str = None,
        dsPersonId: str = None,
        creditDisplay: str = None,
        creditBalance: str = None,
        freeSongBalance: str = None,
        isManagedStudent: bool = None,
        action: _action = None,
        subscriptionStatus: _subscriptionStatus = None,
        accountFlags: _accountFlags = None,
        status: int = None,
        download_queue_info: _download_queue_info = None,
        privacyAcknowledgement: _privacyAcknowledgement = None,
        dialog: _dialog = None,
    ):
        pass
        self.__pings = pings
        self.__cancel_purchase_batch = cancel_purchase_batch
        self.__customerMessage = customerMessage
        self.__failureType = failureType
        self.__accountInfo = accountInfo
        self.__passwordToken = passwordToken
        self.__clearToken = clearToken
        self.__m_allowed = m_allowed
        self.__is_cloud_enabled = is_cloud_enabled
        self.__dsPersonId = dsPersonId
        self.__creditDisplay = creditDisplay
        self.__creditBalance = creditBalance
        self.__freeSongBalance = freeSongBalance
        self.__isManagedStudent = isManagedStudent
        self.__action = action
        self.__subscriptionStatus = subscriptionStatus
        self.__accountFlags = accountFlags
        self.__status = status
        self.__download_queue_info = download_queue_info
        self.__privacyAcknowledgement = privacyAcknowledgement
        self.__dialog = dialog

    def _get_pings(self):
        return self.__pings

    def _set_pings(self, value):
        if not isinstance(value, list):
            raise TypeError("pings must be list")
        if not all(isinstance(i, float) for i in value):
            raise TypeError("pings list values must be float")

        self.__pings = value

    pings = property(_get_pings, _set_pings)

    def _get_cancel_purchase_batch(self):
        return self.__cancel_purchase_batch

    def _set_cancel_purchase_batch(self, value):
        if value is not None and not isinstance(value, bool):
            raise TypeError("cancel_purchase_batch must be bool")

        self.__cancel_purchase_batch = value

    cancel_purchase_batch = property(
        _get_cancel_purchase_batch, _set_cancel_purchase_batch
    )

    def _get_customerMessage(self):
        return self.__customerMessage

    def _set_customerMessage(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("customerMessage must be str")

        self.__customerMessage = value

    customerMessage = property(_get_customerMessage, _set_customerMessage)

    def _get_failureType(self):
        return self.__failureType

    def _set_failureType(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("failureType must be str")

        self.__failureType = value

    failureType = property(_get_failureType, _set_failureType)

    def _get_accountInfo(self):
        return self.__accountInfo

    def _set_accountInfo(self, value):
        if not isinstance(value, StoreAuthenticateResp._accountInfo):
            raise TypeError("accountInfo must be StoreAuthenticateResp._accountInfo")

        self.__accountInfo = value

    accountInfo = property(_get_accountInfo, _set_accountInfo)

    def _get_passwordToken(self):
        return self.__passwordToken

    def _set_passwordToken(self, value):
        if not isinstance(value, str):
            raise TypeError("passwordToken must be str")

        self.__passwordToken = value

    passwordToken = property(_get_passwordToken, _set_passwordToken)

    def _get_clearToken(self):
        return self.__clearToken

    def _set_clearToken(self, value):
        if not isinstance(value, str):
            raise TypeError("clearToken must be str")

        self.__clearToken = value

    clearToken = property(_get_clearToken, _set_clearToken)

    def _get_m_allowed(self):
        return self.__m_allowed

    def _set_m_allowed(self, value):
        if not isinstance(value, bool):
            raise TypeError("m_allowed must be bool")

        self.__m_allowed = value

    m_allowed = property(_get_m_allowed, _set_m_allowed)

    def _get_is_cloud_enabled(self):
        return self.__is_cloud_enabled

    def _set_is_cloud_enabled(self, value):
        if not isinstance(value, str):
            raise TypeError("is_cloud_enabled must be str")

        self.__is_cloud_enabled = value

    is_cloud_enabled = property(_get_is_cloud_enabled, _set_is_cloud_enabled)

    def _get_dsPersonId(self):
        return self.__dsPersonId

    def _set_dsPersonId(self, value):
        if not isinstance(value, str):
            raise TypeError("dsPersonId must be str")

        self.__dsPersonId = value

    dsPersonId = property(_get_dsPersonId, _set_dsPersonId)

    def _get_creditDisplay(self):
        return self.__creditDisplay

    def _set_creditDisplay(self, value):
        if not isinstance(value, str):
            raise TypeError("creditDisplay must be str")

        self.__creditDisplay = value

    creditDisplay = property(_get_creditDisplay, _set_creditDisplay)

    def _get_creditBalance(self):
        return self.__creditBalance

    def _set_creditBalance(self, value):
        if not isinstance(value, str):
            raise TypeError("creditBalance must be str")

        self.__creditBalance = value

    creditBalance = property(_get_creditBalance, _set_creditBalance)

    def _get_freeSongBalance(self):
        return self.__freeSongBalance

    def _set_freeSongBalance(self, value):
        if not isinstance(value, str):
            raise TypeError("freeSongBalance must be str")

        self.__freeSongBalance = value

    freeSongBalance = property(_get_freeSongBalance, _set_freeSongBalance)

    def _get_isManagedStudent(self):
        return self.__isManagedStudent

    def _set_isManagedStudent(self, value):
        if not isinstance(value, bool):
            raise TypeError("isManagedStudent must be bool")

        self.__isManagedStudent = value

    isManagedStudent = property(_get_isManagedStudent, _set_isManagedStudent)

    def _get_action(self):
        return self.__action

    def _set_action(self, value):
        if not isinstance(value, StoreAuthenticateResp._action):
            raise TypeError("action must be StoreAuthenticateResp._action")

        self.__action = value

    action = property(_get_action, _set_action)

    def _get_subscriptionStatus(self):
        return self.__subscriptionStatus

    def _set_subscriptionStatus(self, value):
        if not isinstance(value, StoreAuthenticateResp._subscriptionStatus):
            raise TypeError(
                "subscriptionStatus must be StoreAuthenticateResp._subscriptionStatus"
            )

        self.__subscriptionStatus = value

    subscriptionStatus = property(_get_subscriptionStatus, _set_subscriptionStatus)

    def _get_accountFlags(self):
        return self.__accountFlags

    def _set_accountFlags(self, value):
        if not isinstance(value, StoreAuthenticateResp._accountFlags):
            raise TypeError("accountFlags must be StoreAuthenticateResp._accountFlags")

        self.__accountFlags = value

    accountFlags = property(_get_accountFlags, _set_accountFlags)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, int):
            raise TypeError("status must be int")

        self.__status = value

    status = property(_get_status, _set_status)

    def _get_download_queue_info(self):
        return self.__download_queue_info

    def _set_download_queue_info(self, value):
        if not isinstance(value, StoreAuthenticateResp._download_queue_info):
            raise TypeError(
                "download_queue_info must be StoreAuthenticateResp._download_queue_info"
            )

        self.__download_queue_info = value

    download_queue_info = property(_get_download_queue_info, _set_download_queue_info)

    def _get_privacyAcknowledgement(self):
        return self.__privacyAcknowledgement

    def _set_privacyAcknowledgement(self, value):
        if not isinstance(value, StoreAuthenticateResp._privacyAcknowledgement):
            raise TypeError(
                "privacyAcknowledgement must be StoreAuthenticateResp._privacyAcknowledgement"
            )

        self.__privacyAcknowledgement = value

    privacyAcknowledgement = property(
        _get_privacyAcknowledgement, _set_privacyAcknowledgement
    )

    def _get_dialog(self):
        return self.__dialog

    def _set_dialog(self, value):
        if not isinstance(value, StoreAuthenticateResp._dialog):
            raise TypeError("dialog must be StoreAuthenticateResp._dialog")

        self.__dialog = value

    dialog = property(_get_dialog, _set_dialog)

    @staticmethod
    def from_dict(d):
        v = {}
        if "pings" in d:
            v["pings"] = [
                float.from_dict(p) if hasattr(float, "from_dict") else p
                for p in d["pings"]
            ]
        if "cancel-purchase-batch" in d:
            v["cancel_purchase_batch"] = (
                bool.from_dict(d["cancel-purchase-batch"])
                if hasattr(bool, "from_dict")
                else d["cancel-purchase-batch"]
            )
        if "customerMessage" in d:
            v["customerMessage"] = (
                str.from_dict(d["customerMessage"])
                if hasattr(str, "from_dict")
                else d["customerMessage"]
            )
        if "failureType" in d:
            v["failureType"] = (
                str.from_dict(d["failureType"])
                if hasattr(str, "from_dict")
                else d["failureType"]
            )
        if "accountInfo" in d:
            v["accountInfo"] = (
                StoreAuthenticateResp._accountInfo.from_dict(d["accountInfo"])
                if hasattr(StoreAuthenticateResp._accountInfo, "from_dict")
                else d["accountInfo"]
            )
        if "passwordToken" in d:
            v["passwordToken"] = (
                str.from_dict(d["passwordToken"])
                if hasattr(str, "from_dict")
                else d["passwordToken"]
            )
        if "clearToken" in d:
            v["clearToken"] = (
                str.from_dict(d["clearToken"])
                if hasattr(str, "from_dict")
                else d["clearToken"]
            )
        if "m-allowed" in d:
            v["m_allowed"] = (
                bool.from_dict(d["m-allowed"])
                if hasattr(bool, "from_dict")
                else d["m-allowed"]
            )
        if "is-cloud-enabled" in d:
            v["is_cloud_enabled"] = (
                str.from_dict(d["is-cloud-enabled"])
                if hasattr(str, "from_dict")
                else d["is-cloud-enabled"]
            )
        if "dsPersonId" in d:
            v["dsPersonId"] = (
                str.from_dict(d["dsPersonId"])
                if hasattr(str, "from_dict")
                else d["dsPersonId"]
            )
        if "creditDisplay" in d:
            v["creditDisplay"] = (
                str.from_dict(d["creditDisplay"])
                if hasattr(str, "from_dict")
                else d["creditDisplay"]
            )
        if "creditBalance" in d:
            v["creditBalance"] = (
                str.from_dict(d["creditBalance"])
                if hasattr(str, "from_dict")
                else d["creditBalance"]
            )
        if "freeSongBalance" in d:
            v["freeSongBalance"] = (
                str.from_dict(d["freeSongBalance"])
                if hasattr(str, "from_dict")
                else d["freeSongBalance"]
            )
        if "isManagedStudent" in d:
            v["isManagedStudent"] = (
                bool.from_dict(d["isManagedStudent"])
                if hasattr(bool, "from_dict")
                else d["isManagedStudent"]
            )
        if "action" in d:
            v["action"] = (
                StoreAuthenticateResp._action.from_dict(d["action"])
                if hasattr(StoreAuthenticateResp._action, "from_dict")
                else d["action"]
            )
        if "subscriptionStatus" in d:
            v["subscriptionStatus"] = (
                StoreAuthenticateResp._subscriptionStatus.from_dict(
                    d["subscriptionStatus"]
                )
                if hasattr(StoreAuthenticateResp._subscriptionStatus, "from_dict")
                else d["subscriptionStatus"]
            )
        if "accountFlags" in d:
            v["accountFlags"] = (
                StoreAuthenticateResp._accountFlags.from_dict(d["accountFlags"])
                if hasattr(StoreAuthenticateResp._accountFlags, "from_dict")
                else d["accountFlags"]
            )
        if "status" in d:
            v["status"] = (
                int.from_dict(d["status"]) if hasattr(int, "from_dict") else d["status"]
            )
        if "download-queue-info" in d:
            v["download_queue_info"] = (
                StoreAuthenticateResp._download_queue_info.from_dict(
                    d["download-queue-info"]
                )
                if hasattr(StoreAuthenticateResp._download_queue_info, "from_dict")
                else d["download-queue-info"]
            )
        if "privacyAcknowledgement" in d:
            v["privacyAcknowledgement"] = (
                StoreAuthenticateResp._privacyAcknowledgement.from_dict(
                    d["privacyAcknowledgement"]
                )
                if hasattr(StoreAuthenticateResp._privacyAcknowledgement, "from_dict")
                else d["privacyAcknowledgement"]
            )
        if "dialog" in d:
            v["dialog"] = (
                StoreAuthenticateResp._dialog.from_dict(d["dialog"])
                if hasattr(StoreAuthenticateResp._dialog, "from_dict")
                else d["dialog"]
            )
        return StoreAuthenticateResp(**v)

    def as_dict(self):
        d = {}
        if self.__pings is not None:
            d["pings"] = [
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__pings
            ]
        if self.__cancel_purchase_batch is not None:
            d["cancel-purchase-batch"] = (
                self.__cancel_purchase_batch.as_dict()
                if hasattr(self.__cancel_purchase_batch, "as_dict")
                else self.__cancel_purchase_batch
            )
        if self.__customerMessage is not None:
            d["customerMessage"] = (
                self.__customerMessage.as_dict()
                if hasattr(self.__customerMessage, "as_dict")
                else self.__customerMessage
            )
        if self.__failureType is not None:
            d["failureType"] = (
                self.__failureType.as_dict()
                if hasattr(self.__failureType, "as_dict")
                else self.__failureType
            )
        if self.__accountInfo is not None:
            d["accountInfo"] = (
                self.__accountInfo.as_dict()
                if hasattr(self.__accountInfo, "as_dict")
                else self.__accountInfo
            )
        if self.__passwordToken is not None:
            d["passwordToken"] = (
                self.__passwordToken.as_dict()
                if hasattr(self.__passwordToken, "as_dict")
                else self.__passwordToken
            )
        if self.__clearToken is not None:
            d["clearToken"] = (
                self.__clearToken.as_dict()
                if hasattr(self.__clearToken, "as_dict")
                else self.__clearToken
            )
        if self.__m_allowed is not None:
            d["m-allowed"] = (
                self.__m_allowed.as_dict()
                if hasattr(self.__m_allowed, "as_dict")
                else self.__m_allowed
            )
        if self.__is_cloud_enabled is not None:
            d["is-cloud-enabled"] = (
                self.__is_cloud_enabled.as_dict()
                if hasattr(self.__is_cloud_enabled, "as_dict")
                else self.__is_cloud_enabled
            )
        if self.__dsPersonId is not None:
            d["dsPersonId"] = (
                self.__dsPersonId.as_dict()
                if hasattr(self.__dsPersonId, "as_dict")
                else self.__dsPersonId
            )
        if self.__creditDisplay is not None:
            d["creditDisplay"] = (
                self.__creditDisplay.as_dict()
                if hasattr(self.__creditDisplay, "as_dict")
                else self.__creditDisplay
            )
        if self.__creditBalance is not None:
            d["creditBalance"] = (
                self.__creditBalance.as_dict()
                if hasattr(self.__creditBalance, "as_dict")
                else self.__creditBalance
            )
        if self.__freeSongBalance is not None:
            d["freeSongBalance"] = (
                self.__freeSongBalance.as_dict()
                if hasattr(self.__freeSongBalance, "as_dict")
                else self.__freeSongBalance
            )
        if self.__isManagedStudent is not None:
            d["isManagedStudent"] = (
                self.__isManagedStudent.as_dict()
                if hasattr(self.__isManagedStudent, "as_dict")
                else self.__isManagedStudent
            )
        if self.__action is not None:
            d["action"] = (
                self.__action.as_dict()
                if hasattr(self.__action, "as_dict")
                else self.__action
            )
        if self.__subscriptionStatus is not None:
            d["subscriptionStatus"] = (
                self.__subscriptionStatus.as_dict()
                if hasattr(self.__subscriptionStatus, "as_dict")
                else self.__subscriptionStatus
            )
        if self.__accountFlags is not None:
            d["accountFlags"] = (
                self.__accountFlags.as_dict()
                if hasattr(self.__accountFlags, "as_dict")
                else self.__accountFlags
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
            )
        if self.__download_queue_info is not None:
            d["download-queue-info"] = (
                self.__download_queue_info.as_dict()
                if hasattr(self.__download_queue_info, "as_dict")
                else self.__download_queue_info
            )
        if self.__privacyAcknowledgement is not None:
            d["privacyAcknowledgement"] = (
                self.__privacyAcknowledgement.as_dict()
                if hasattr(self.__privacyAcknowledgement, "as_dict")
                else self.__privacyAcknowledgement
            )
        if self.__dialog is not None:
            d["dialog"] = (
                self.__dialog.as_dict()
                if hasattr(self.__dialog, "as_dict")
                else self.__dialog
            )
        return d

    def __repr__(self):
        return "<Class StoreAuthenticateResp. pings: {}, cancel_purchase_batch: {}, customerMessage: {}, failureType: {}, accountInfo: {}, passwordToken: {}, clearToken: {}, m_allowed: {}, is_cloud_enabled: {}, dsPersonId: {}, creditDisplay: {}, creditBalance: {}, freeSongBalance: {}, isManagedStudent: {}, action: {}, subscriptionStatus: {}, accountFlags: {}, status: {}, download_queue_info: {}, privacyAcknowledgement: {}, dialog: {}>".format(
            limitedRepr(
                self.__pings[:20] if isinstance(self.__pings, bytes) else self.__pings
            ),
            limitedRepr(
                self.__cancel_purchase_batch[:20]
                if isinstance(self.__cancel_purchase_batch, bytes)
                else self.__cancel_purchase_batch
            ),
            limitedRepr(
                self.__customerMessage[:20]
                if isinstance(self.__customerMessage, bytes)
                else self.__customerMessage
            ),
            limitedRepr(
                self.__failureType[:20]
                if isinstance(self.__failureType, bytes)
                else self.__failureType
            ),
            limitedRepr(
                self.__accountInfo[:20]
                if isinstance(self.__accountInfo, bytes)
                else self.__accountInfo
            ),
            limitedRepr(
                self.__passwordToken[:20]
                if isinstance(self.__passwordToken, bytes)
                else self.__passwordToken
            ),
            limitedRepr(
                self.__clearToken[:20]
                if isinstance(self.__clearToken, bytes)
                else self.__clearToken
            ),
            limitedRepr(
                self.__m_allowed[:20]
                if isinstance(self.__m_allowed, bytes)
                else self.__m_allowed
            ),
            limitedRepr(
                self.__is_cloud_enabled[:20]
                if isinstance(self.__is_cloud_enabled, bytes)
                else self.__is_cloud_enabled
            ),
            limitedRepr(
                self.__dsPersonId[:20]
                if isinstance(self.__dsPersonId, bytes)
                else self.__dsPersonId
            ),
            limitedRepr(
                self.__creditDisplay[:20]
                if isinstance(self.__creditDisplay, bytes)
                else self.__creditDisplay
            ),
            limitedRepr(
                self.__creditBalance[:20]
                if isinstance(self.__creditBalance, bytes)
                else self.__creditBalance
            ),
            limitedRepr(
                self.__freeSongBalance[:20]
                if isinstance(self.__freeSongBalance, bytes)
                else self.__freeSongBalance
            ),
            limitedRepr(
                self.__isManagedStudent[:20]
                if isinstance(self.__isManagedStudent, bytes)
                else self.__isManagedStudent
            ),
            limitedRepr(
                self.__action[:20]
                if isinstance(self.__action, bytes)
                else self.__action
            ),
            limitedRepr(
                self.__subscriptionStatus[:20]
                if isinstance(self.__subscriptionStatus, bytes)
                else self.__subscriptionStatus
            ),
            limitedRepr(
                self.__accountFlags[:20]
                if isinstance(self.__accountFlags, bytes)
                else self.__accountFlags
            ),
            limitedRepr(
                self.__status[:20]
                if isinstance(self.__status, bytes)
                else self.__status
            ),
            limitedRepr(
                self.__download_queue_info[:20]
                if isinstance(self.__download_queue_info, bytes)
                else self.__download_queue_info
            ),
            limitedRepr(
                self.__privacyAcknowledgement[:20]
                if isinstance(self.__privacyAcknowledgement, bytes)
                else self.__privacyAcknowledgement
            ),
            limitedRepr(
                self.__dialog[:20]
                if isinstance(self.__dialog, bytes)
                else self.__dialog
            ),
        )
