from reprlib import repr as limitedRepr


from typing import List


class StoreDownloadResp:
    class _songList:
        class _chunks:

            _types_map = {
                "chunkSize": {"type": int, "subtype": None},
                "hashes": {"type": list, "subtype": str},
            }
            _formats_map = {}
            _validations_map = {
                "chunkSize": {
                    "required": True,
                },
                "hashes": {
                    "required": True,
                },
            }

            def __init__(self, chunkSize: int = None, hashes: List[str] = None):
                pass
                self.__chunkSize = chunkSize
                self.__hashes = hashes

            def _get_chunkSize(self):
                return self.__chunkSize

            def _set_chunkSize(self, value):
                if not isinstance(value, int):
                    raise TypeError("chunkSize must be int")

                self.__chunkSize = value

            chunkSize = property(_get_chunkSize, _set_chunkSize)

            def _get_hashes(self):
                return self.__hashes

            def _set_hashes(self, value):
                if not isinstance(value, list):
                    raise TypeError("hashes must be list")
                if not all(isinstance(i, str) for i in value):
                    raise TypeError("hashes list values must be str")

                self.__hashes = value

            hashes = property(_get_hashes, _set_hashes)

            @staticmethod
            def from_dict(d):
                v = {}
                if "chunkSize" in d:
                    v["chunkSize"] = (
                        int.from_dict(d["chunkSize"])
                        if hasattr(int, "from_dict")
                        else d["chunkSize"]
                    )
                if "hashes" in d:
                    v["hashes"] = [
                        str.from_dict(p) if hasattr(str, "from_dict") else p
                        for p in d["hashes"]
                    ]
                return StoreDownloadResp._songList._chunks(**v)

            def as_dict(self):
                d = {}
                if self.__chunkSize is not None:
                    d["chunkSize"] = (
                        self.__chunkSize.as_dict()
                        if hasattr(self.__chunkSize, "as_dict")
                        else self.__chunkSize
                    )
                if self.__hashes is not None:
                    d["hashes"] = [
                        p.as_dict() if hasattr(p, "as_dict") else p
                        for p in self.__hashes
                    ]
                return d

            def __repr__(self):
                return "<Class _chunks. chunkSize: {}, hashes: {}>".format(
                    limitedRepr(
                        self.__chunkSize[:20]
                        if isinstance(self.__chunkSize, bytes)
                        else self.__chunkSize
                    ),
                    limitedRepr(
                        self.__hashes[:20]
                        if isinstance(self.__hashes, bytes)
                        else self.__hashes
                    ),
                )

        class _artwork_urls:
            class _default:

                _types_map = {
                    "url": {"type": str, "subtype": None},
                }
                _formats_map = {}
                _validations_map = {
                    "url": {
                        "required": True,
                    },
                }

                def __init__(self, url: str = None):
                    pass
                    self.__url = url

                def _get_url(self):
                    return self.__url

                def _set_url(self, value):
                    if not isinstance(value, str):
                        raise TypeError("url must be str")

                    self.__url = value

                url = property(_get_url, _set_url)

                @staticmethod
                def from_dict(d):
                    v = {}
                    if "url" in d:
                        v["url"] = (
                            str.from_dict(d["url"])
                            if hasattr(str, "from_dict")
                            else d["url"]
                        )
                    return StoreDownloadResp._songList._artwork_urls._default(**v)

                def as_dict(self):
                    d = {}
                    if self.__url is not None:
                        d["url"] = (
                            self.__url.as_dict()
                            if hasattr(self.__url, "as_dict")
                            else self.__url
                        )
                    return d

                def __repr__(self):
                    return "<Class _default. url: {}>".format(
                        limitedRepr(
                            self.__url[:20]
                            if isinstance(self.__url, bytes)
                            else self.__url
                        )
                    )

            _types_map = {
                "image_type": {"type": str, "subtype": None},
                "default": {"type": _default, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "image_type": {
                    "required": True,
                },
                "default": {
                    "required": True,
                },
            }

            def __init__(self, image_type: str = None, default: _default = None):
                pass
                self.__image_type = image_type
                self.__default = default

            def _get_image_type(self):
                return self.__image_type

            def _set_image_type(self, value):
                if not isinstance(value, str):
                    raise TypeError("image_type must be str")

                self.__image_type = value

            image_type = property(_get_image_type, _set_image_type)

            def _get_default(self):
                return self.__default

            def _set_default(self, value):
                if not isinstance(
                    value, StoreDownloadResp._songList._artwork_urls._default
                ):
                    raise TypeError(
                        "default must be StoreDownloadResp._songList._artwork_urls._default"
                    )

                self.__default = value

            default = property(_get_default, _set_default)

            @staticmethod
            def from_dict(d):
                v = {}
                if "image-type" in d:
                    v["image_type"] = (
                        str.from_dict(d["image-type"])
                        if hasattr(str, "from_dict")
                        else d["image-type"]
                    )
                if "default" in d:
                    v["default"] = (
                        StoreDownloadResp._songList._artwork_urls._default.from_dict(
                            d["default"]
                        )
                        if hasattr(
                            StoreDownloadResp._songList._artwork_urls._default,
                            "from_dict",
                        )
                        else d["default"]
                    )
                return StoreDownloadResp._songList._artwork_urls(**v)

            def as_dict(self):
                d = {}
                if self.__image_type is not None:
                    d["image-type"] = (
                        self.__image_type.as_dict()
                        if hasattr(self.__image_type, "as_dict")
                        else self.__image_type
                    )
                if self.__default is not None:
                    d["default"] = (
                        self.__default.as_dict()
                        if hasattr(self.__default, "as_dict")
                        else self.__default
                    )
                return d

            def __repr__(self):
                return "<Class _artwork_urls. image_type: {}, default: {}>".format(
                    limitedRepr(
                        self.__image_type[:20]
                        if isinstance(self.__image_type, bytes)
                        else self.__image_type
                    ),
                    limitedRepr(
                        self.__default[:20]
                        if isinstance(self.__default, bytes)
                        else self.__default
                    ),
                )

        class _sinfs:

            _types_map = {
                "id": {"type": int, "subtype": None},
                "sinf": {"type": str, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "id": {
                    "required": True,
                },
                "sinf": {
                    "required": True,
                },
            }

            def __init__(self, id: int = None, sinf: str = None):
                pass
                self.__id = id
                self.__sinf = sinf

            def _get_id(self):
                return self.__id

            def _set_id(self, value):
                if not isinstance(value, int):
                    raise TypeError("id must be int")

                self.__id = value

            id = property(_get_id, _set_id)

            def _get_sinf(self):
                return self.__sinf

            def _set_sinf(self, value):
                if not isinstance(value, str):
                    raise TypeError("sinf must be str")

                self.__sinf = value

            sinf = property(_get_sinf, _set_sinf)

            @staticmethod
            def from_dict(d):
                v = {}
                if "id" in d:
                    v["id"] = (
                        int.from_dict(d["id"]) if hasattr(int, "from_dict") else d["id"]
                    )
                if "sinf" in d:
                    v["sinf"] = (
                        str.from_dict(d["sinf"])
                        if hasattr(str, "from_dict")
                        else d["sinf"]
                    )
                return StoreDownloadResp._songList._sinfs(**v)

            def as_dict(self):
                d = {}
                if self.__id is not None:
                    d["id"] = (
                        self.__id.as_dict()
                        if hasattr(self.__id, "as_dict")
                        else self.__id
                    )
                if self.__sinf is not None:
                    d["sinf"] = (
                        self.__sinf.as_dict()
                        if hasattr(self.__sinf, "as_dict")
                        else self.__sinf
                    )
                return d

            def __repr__(self):
                return "<Class _sinfs. id: {}, sinf: {}>".format(
                    limitedRepr(
                        self.__id[:20] if isinstance(self.__id, bytes) else self.__id
                    ),
                    limitedRepr(
                        self.__sinf[:20]
                        if isinstance(self.__sinf, bytes)
                        else self.__sinf
                    ),
                )

        class _asset_info:

            _types_map = {
                "file_size": {"type": int, "subtype": None},
                "flavor": {"type": str, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "file_size": {
                    "required": True,
                },
                "flavor": {
                    "required": True,
                },
            }

            def __init__(self, file_size: int = None, flavor: str = None):
                pass
                self.__file_size = file_size
                self.__flavor = flavor

            def _get_file_size(self):
                return self.__file_size

            def _set_file_size(self, value):
                if not isinstance(value, int):
                    raise TypeError("file_size must be int")

                self.__file_size = value

            file_size = property(_get_file_size, _set_file_size)

            def _get_flavor(self):
                return self.__flavor

            def _set_flavor(self, value):
                if not isinstance(value, str):
                    raise TypeError("flavor must be str")

                self.__flavor = value

            flavor = property(_get_flavor, _set_flavor)

            @staticmethod
            def from_dict(d):
                v = {}
                if "file-size" in d:
                    v["file_size"] = (
                        int.from_dict(d["file-size"])
                        if hasattr(int, "from_dict")
                        else d["file-size"]
                    )
                if "flavor" in d:
                    v["flavor"] = (
                        str.from_dict(d["flavor"])
                        if hasattr(str, "from_dict")
                        else d["flavor"]
                    )
                return StoreDownloadResp._songList._asset_info(**v)

            def as_dict(self):
                d = {}
                if self.__file_size is not None:
                    d["file-size"] = (
                        self.__file_size.as_dict()
                        if hasattr(self.__file_size, "as_dict")
                        else self.__file_size
                    )
                if self.__flavor is not None:
                    d["flavor"] = (
                        self.__flavor.as_dict()
                        if hasattr(self.__flavor, "as_dict")
                        else self.__flavor
                    )
                return d

            def __repr__(self):
                return "<Class _asset_info. file_size: {}, flavor: {}>".format(
                    limitedRepr(
                        self.__file_size[:20]
                        if isinstance(self.__file_size, bytes)
                        else self.__file_size
                    ),
                    limitedRepr(
                        self.__flavor[:20]
                        if isinstance(self.__flavor, bytes)
                        else self.__flavor
                    ),
                )

        class _metadata:
            class _MacUIRequiredDeviceCapabilities:

                _types_map = {
                    "arm64": {"type": bool, "subtype": None},
                    "gamekit": {"type": bool, "subtype": None},
                    "metal": {"type": bool, "subtype": None},
                }
                _formats_map = {}
                _validations_map = {
                    "arm64": {
                        "required": True,
                    },
                    "gamekit": {
                        "required": True,
                    },
                    "metal": {
                        "required": True,
                    },
                }

                def __init__(
                    self, arm64: bool = None, gamekit: bool = None, metal: bool = None
                ):
                    pass
                    self.__arm64 = arm64
                    self.__gamekit = gamekit
                    self.__metal = metal

                def _get_arm64(self):
                    return self.__arm64

                def _set_arm64(self, value):
                    if not isinstance(value, bool):
                        raise TypeError("arm64 must be bool")

                    self.__arm64 = value

                arm64 = property(_get_arm64, _set_arm64)

                def _get_gamekit(self):
                    return self.__gamekit

                def _set_gamekit(self, value):
                    if not isinstance(value, bool):
                        raise TypeError("gamekit must be bool")

                    self.__gamekit = value

                gamekit = property(_get_gamekit, _set_gamekit)

                def _get_metal(self):
                    return self.__metal

                def _set_metal(self, value):
                    if not isinstance(value, bool):
                        raise TypeError("metal must be bool")

                    self.__metal = value

                metal = property(_get_metal, _set_metal)

                @staticmethod
                def from_dict(d):
                    v = {}
                    if "arm64" in d:
                        v["arm64"] = (
                            bool.from_dict(d["arm64"])
                            if hasattr(bool, "from_dict")
                            else d["arm64"]
                        )
                    if "gamekit" in d:
                        v["gamekit"] = (
                            bool.from_dict(d["gamekit"])
                            if hasattr(bool, "from_dict")
                            else d["gamekit"]
                        )
                    if "metal" in d:
                        v["metal"] = (
                            bool.from_dict(d["metal"])
                            if hasattr(bool, "from_dict")
                            else d["metal"]
                        )
                    return StoreDownloadResp._songList._metadata._MacUIRequiredDeviceCapabilities(
                        **v
                    )

                def as_dict(self):
                    d = {}
                    if self.__arm64 is not None:
                        d["arm64"] = (
                            self.__arm64.as_dict()
                            if hasattr(self.__arm64, "as_dict")
                            else self.__arm64
                        )
                    if self.__gamekit is not None:
                        d["gamekit"] = (
                            self.__gamekit.as_dict()
                            if hasattr(self.__gamekit, "as_dict")
                            else self.__gamekit
                        )
                    if self.__metal is not None:
                        d["metal"] = (
                            self.__metal.as_dict()
                            if hasattr(self.__metal, "as_dict")
                            else self.__metal
                        )
                    return d

                def __repr__(self):
                    return "<Class _MacUIRequiredDeviceCapabilities. arm64: {}, gamekit: {}, metal: {}>".format(
                        limitedRepr(
                            self.__arm64[:20]
                            if isinstance(self.__arm64, bytes)
                            else self.__arm64
                        ),
                        limitedRepr(
                            self.__gamekit[:20]
                            if isinstance(self.__gamekit, bytes)
                            else self.__gamekit
                        ),
                        limitedRepr(
                            self.__metal[:20]
                            if isinstance(self.__metal, bytes)
                            else self.__metal
                        ),
                    )

            class _UIRequiredDeviceCapabilities:

                _types_map = {
                    "arm64": {"type": bool, "subtype": None},
                    "gamekit": {"type": bool, "subtype": None},
                    "metal": {"type": bool, "subtype": None},
                }
                _formats_map = {}
                _validations_map = {
                    "arm64": {
                        "required": True,
                    },
                    "gamekit": {
                        "required": True,
                    },
                    "metal": {
                        "required": True,
                    },
                }

                def __init__(
                    self, arm64: bool = None, gamekit: bool = None, metal: bool = None
                ):
                    pass
                    self.__arm64 = arm64
                    self.__gamekit = gamekit
                    self.__metal = metal

                def _get_arm64(self):
                    return self.__arm64

                def _set_arm64(self, value):
                    if not isinstance(value, bool):
                        raise TypeError("arm64 must be bool")

                    self.__arm64 = value

                arm64 = property(_get_arm64, _set_arm64)

                def _get_gamekit(self):
                    return self.__gamekit

                def _set_gamekit(self, value):
                    if not isinstance(value, bool):
                        raise TypeError("gamekit must be bool")

                    self.__gamekit = value

                gamekit = property(_get_gamekit, _set_gamekit)

                def _get_metal(self):
                    return self.__metal

                def _set_metal(self, value):
                    if not isinstance(value, bool):
                        raise TypeError("metal must be bool")

                    self.__metal = value

                metal = property(_get_metal, _set_metal)

                @staticmethod
                def from_dict(d):
                    v = {}
                    if "arm64" in d:
                        v["arm64"] = (
                            bool.from_dict(d["arm64"])
                            if hasattr(bool, "from_dict")
                            else d["arm64"]
                        )
                    if "gamekit" in d:
                        v["gamekit"] = (
                            bool.from_dict(d["gamekit"])
                            if hasattr(bool, "from_dict")
                            else d["gamekit"]
                        )
                    if "metal" in d:
                        v["metal"] = (
                            bool.from_dict(d["metal"])
                            if hasattr(bool, "from_dict")
                            else d["metal"]
                        )
                    return StoreDownloadResp._songList._metadata._UIRequiredDeviceCapabilities(
                        **v
                    )

                def as_dict(self):
                    d = {}
                    if self.__arm64 is not None:
                        d["arm64"] = (
                            self.__arm64.as_dict()
                            if hasattr(self.__arm64, "as_dict")
                            else self.__arm64
                        )
                    if self.__gamekit is not None:
                        d["gamekit"] = (
                            self.__gamekit.as_dict()
                            if hasattr(self.__gamekit, "as_dict")
                            else self.__gamekit
                        )
                    if self.__metal is not None:
                        d["metal"] = (
                            self.__metal.as_dict()
                            if hasattr(self.__metal, "as_dict")
                            else self.__metal
                        )
                    return d

                def __repr__(self):
                    return "<Class _UIRequiredDeviceCapabilities. arm64: {}, gamekit: {}, metal: {}>".format(
                        limitedRepr(
                            self.__arm64[:20]
                            if isinstance(self.__arm64, bytes)
                            else self.__arm64
                        ),
                        limitedRepr(
                            self.__gamekit[:20]
                            if isinstance(self.__gamekit, bytes)
                            else self.__gamekit
                        ),
                        limitedRepr(
                            self.__metal[:20]
                            if isinstance(self.__metal, bytes)
                            else self.__metal
                        ),
                    )

            class _subgenres:

                _types_map = {
                    "genre": {"type": str, "subtype": None},
                    "genreId": {"type": int, "subtype": None},
                }
                _formats_map = {}
                _validations_map = {
                    "genre": {
                        "required": True,
                    },
                    "genreId": {
                        "required": True,
                    },
                }

                def __init__(self, genre: str = None, genreId: int = None):
                    pass
                    self.__genre = genre
                    self.__genreId = genreId

                def _get_genre(self):
                    return self.__genre

                def _set_genre(self, value):
                    if not isinstance(value, str):
                        raise TypeError("genre must be str")

                    self.__genre = value

                genre = property(_get_genre, _set_genre)

                def _get_genreId(self):
                    return self.__genreId

                def _set_genreId(self, value):
                    if not isinstance(value, int):
                        raise TypeError("genreId must be int")

                    self.__genreId = value

                genreId = property(_get_genreId, _set_genreId)

                @staticmethod
                def from_dict(d):
                    v = {}
                    if "genre" in d:
                        v["genre"] = (
                            str.from_dict(d["genre"])
                            if hasattr(str, "from_dict")
                            else d["genre"]
                        )
                    if "genreId" in d:
                        v["genreId"] = (
                            int.from_dict(d["genreId"])
                            if hasattr(int, "from_dict")
                            else d["genreId"]
                        )
                    return StoreDownloadResp._songList._metadata._subgenres(**v)

                def as_dict(self):
                    d = {}
                    if self.__genre is not None:
                        d["genre"] = (
                            self.__genre.as_dict()
                            if hasattr(self.__genre, "as_dict")
                            else self.__genre
                        )
                    if self.__genreId is not None:
                        d["genreId"] = (
                            self.__genreId.as_dict()
                            if hasattr(self.__genreId, "as_dict")
                            else self.__genreId
                        )
                    return d

                def __repr__(self):
                    return "<Class _subgenres. genre: {}, genreId: {}>".format(
                        limitedRepr(
                            self.__genre[:20]
                            if isinstance(self.__genre, bytes)
                            else self.__genre
                        ),
                        limitedRepr(
                            self.__genreId[:20]
                            if isinstance(self.__genreId, bytes)
                            else self.__genreId
                        ),
                    )

            class _rating:

                _types_map = {
                    "content": {"type": str, "subtype": None},
                    "label": {"type": str, "subtype": None},
                    "rank": {"type": int, "subtype": None},
                    "system": {"type": str, "subtype": None},
                }
                _formats_map = {}
                _validations_map = {
                    "content": {
                        "required": True,
                    },
                    "label": {
                        "required": True,
                    },
                    "rank": {
                        "required": True,
                    },
                    "system": {
                        "required": True,
                    },
                }

                def __init__(
                    self,
                    content: str = None,
                    label: str = None,
                    rank: int = None,
                    system: str = None,
                ):
                    pass
                    self.__content = content
                    self.__label = label
                    self.__rank = rank
                    self.__system = system

                def _get_content(self):
                    return self.__content

                def _set_content(self, value):
                    if not isinstance(value, str):
                        raise TypeError("content must be str")

                    self.__content = value

                content = property(_get_content, _set_content)

                def _get_label(self):
                    return self.__label

                def _set_label(self, value):
                    if not isinstance(value, str):
                        raise TypeError("label must be str")

                    self.__label = value

                label = property(_get_label, _set_label)

                def _get_rank(self):
                    return self.__rank

                def _set_rank(self, value):
                    if not isinstance(value, int):
                        raise TypeError("rank must be int")

                    self.__rank = value

                rank = property(_get_rank, _set_rank)

                def _get_system(self):
                    return self.__system

                def _set_system(self, value):
                    if not isinstance(value, str):
                        raise TypeError("system must be str")

                    self.__system = value

                system = property(_get_system, _set_system)

                @staticmethod
                def from_dict(d):
                    v = {}
                    if "content" in d:
                        v["content"] = (
                            str.from_dict(d["content"])
                            if hasattr(str, "from_dict")
                            else d["content"]
                        )
                    if "label" in d:
                        v["label"] = (
                            str.from_dict(d["label"])
                            if hasattr(str, "from_dict")
                            else d["label"]
                        )
                    if "rank" in d:
                        v["rank"] = (
                            int.from_dict(d["rank"])
                            if hasattr(int, "from_dict")
                            else d["rank"]
                        )
                    if "system" in d:
                        v["system"] = (
                            str.from_dict(d["system"])
                            if hasattr(str, "from_dict")
                            else d["system"]
                        )
                    return StoreDownloadResp._songList._metadata._rating(**v)

                def as_dict(self):
                    d = {}
                    if self.__content is not None:
                        d["content"] = (
                            self.__content.as_dict()
                            if hasattr(self.__content, "as_dict")
                            else self.__content
                        )
                    if self.__label is not None:
                        d["label"] = (
                            self.__label.as_dict()
                            if hasattr(self.__label, "as_dict")
                            else self.__label
                        )
                    if self.__rank is not None:
                        d["rank"] = (
                            self.__rank.as_dict()
                            if hasattr(self.__rank, "as_dict")
                            else self.__rank
                        )
                    if self.__system is not None:
                        d["system"] = (
                            self.__system.as_dict()
                            if hasattr(self.__system, "as_dict")
                            else self.__system
                        )
                    return d

                def __repr__(self):
                    return "<Class _rating. content: {}, label: {}, rank: {}, system: {}>".format(
                        limitedRepr(
                            self.__content[:20]
                            if isinstance(self.__content, bytes)
                            else self.__content
                        ),
                        limitedRepr(
                            self.__label[:20]
                            if isinstance(self.__label, bytes)
                            else self.__label
                        ),
                        limitedRepr(
                            self.__rank[:20]
                            if isinstance(self.__rank, bytes)
                            else self.__rank
                        ),
                        limitedRepr(
                            self.__system[:20]
                            if isinstance(self.__system, bytes)
                            else self.__system
                        ),
                    )

            _types_map = {
                "MacUIRequiredDeviceCapabilities": {
                    "type": _MacUIRequiredDeviceCapabilities,
                    "subtype": None,
                },
                "UIRequiredDeviceCapabilities": {
                    "type": _UIRequiredDeviceCapabilities,
                    "subtype": None,
                },
                "artistId": {"type": int, "subtype": None},
                "artistName": {"type": str, "subtype": None},
                "bundleDisplayName": {"type": str, "subtype": None},
                "bundleShortVersionString": {"type": str, "subtype": None},
                "bundleVersion": {"type": str, "subtype": None},
                "copyright": {"type": str, "subtype": None},
                "fileExtension": {"type": str, "subtype": None},
                "gameCenterEnabled": {"type": bool, "subtype": None},
                "gameCenterEverEnabled": {"type": bool, "subtype": None},
                "genre": {"type": str, "subtype": None},
                "genreId": {"type": int, "subtype": None},
                "itemId": {"type": int, "subtype": None},
                "itemName": {"type": str, "subtype": None},
                "kind": {"type": str, "subtype": None},
                "playlistName": {"type": str, "subtype": None},
                "product_type": {"type": str, "subtype": None},
                "rating": {"type": _rating, "subtype": None},
                "releaseDate": {"type": str, "subtype": None},
                "requiresRosetta": {"type": bool, "subtype": None},
                "runsOnAppleSilicon": {"type": bool, "subtype": None},
                "runsOnIntel": {"type": bool, "subtype": None},
                "s": {"type": int, "subtype": None},
                "software_platform": {"type": str, "subtype": None},
                "softwareIcon57x57URL": {"type": str, "subtype": None},
                "softwareIconNeedsShine": {"type": bool, "subtype": None},
                "softwareSupportedDeviceIds": {"type": list, "subtype": int},
                "softwareVersionBundleId": {"type": str, "subtype": None},
                "softwareVersionExternalIdentifier": {"type": int, "subtype": None},
                "softwareVersionExternalIdentifiers": {"type": list, "subtype": int},
                "subgenres": {"type": list, "subtype": _subgenres},
                "vendorId": {"type": int, "subtype": None},
                "drmVersionNumber": {"type": int, "subtype": None},
                "versionRestrictions": {"type": int, "subtype": None},
            }
            _formats_map = {}
            _validations_map = {
                "MacUIRequiredDeviceCapabilities": {
                    "required": True,
                },
                "UIRequiredDeviceCapabilities": {
                    "required": True,
                },
                "artistId": {
                    "required": True,
                },
                "artistName": {
                    "required": True,
                },
                "bundleDisplayName": {
                    "required": True,
                },
                "bundleShortVersionString": {
                    "required": True,
                },
                "bundleVersion": {
                    "required": True,
                },
                "copyright": {
                    "required": True,
                },
                "fileExtension": {
                    "required": True,
                },
                "gameCenterEnabled": {
                    "required": True,
                },
                "gameCenterEverEnabled": {
                    "required": True,
                },
                "genre": {
                    "required": True,
                },
                "genreId": {
                    "required": True,
                },
                "itemId": {
                    "required": True,
                },
                "itemName": {
                    "required": True,
                },
                "kind": {
                    "required": True,
                },
                "playlistName": {
                    "required": True,
                },
                "product_type": {
                    "required": True,
                },
                "rating": {
                    "required": True,
                },
                "releaseDate": {
                    "required": True,
                },
                "requiresRosetta": {
                    "required": True,
                },
                "runsOnAppleSilicon": {
                    "required": True,
                },
                "runsOnIntel": {
                    "required": True,
                },
                "s": {
                    "required": True,
                },
                "software_platform": {
                    "required": True,
                },
                "softwareIcon57x57URL": {
                    "required": True,
                },
                "softwareIconNeedsShine": {
                    "required": True,
                },
                "softwareSupportedDeviceIds": {
                    "required": True,
                },
                "softwareVersionBundleId": {
                    "required": True,
                },
                "softwareVersionExternalIdentifier": {
                    "required": True,
                },
                "softwareVersionExternalIdentifiers": {
                    "required": True,
                },
                "subgenres": {
                    "required": True,
                },
                "vendorId": {
                    "required": True,
                },
                "drmVersionNumber": {
                    "required": True,
                },
                "versionRestrictions": {
                    "required": True,
                },
            }

            def __init__(
                self,
                MacUIRequiredDeviceCapabilities: _MacUIRequiredDeviceCapabilities = None,
                UIRequiredDeviceCapabilities: _UIRequiredDeviceCapabilities = None,
                artistId: int = None,
                artistName: str = None,
                bundleDisplayName: str = None,
                bundleShortVersionString: str = None,
                bundleVersion: str = None,
                copyright: str = None,
                fileExtension: str = None,
                gameCenterEnabled: bool = None,
                gameCenterEverEnabled: bool = None,
                genre: str = None,
                genreId: int = None,
                itemId: int = None,
                itemName: str = None,
                kind: str = None,
                playlistName: str = None,
                product_type: str = None,
                rating: _rating = None,
                releaseDate: str = None,
                requiresRosetta: bool = None,
                runsOnAppleSilicon: bool = None,
                runsOnIntel: bool = None,
                s: int = None,
                software_platform: str = None,
                softwareIcon57x57URL: str = None,
                softwareIconNeedsShine: bool = None,
                softwareSupportedDeviceIds: List[int] = None,
                softwareVersionBundleId: str = None,
                softwareVersionExternalIdentifier: int = None,
                softwareVersionExternalIdentifiers: List[int] = None,
                subgenres: List[_subgenres] = None,
                vendorId: int = None,
                drmVersionNumber: int = None,
                versionRestrictions: int = None,
            ):
                pass
                self.__MacUIRequiredDeviceCapabilities = MacUIRequiredDeviceCapabilities
                self.__UIRequiredDeviceCapabilities = UIRequiredDeviceCapabilities
                self.__artistId = artistId
                self.__artistName = artistName
                self.__bundleDisplayName = bundleDisplayName
                self.__bundleShortVersionString = bundleShortVersionString
                self.__bundleVersion = bundleVersion
                self.__copyright = copyright
                self.__fileExtension = fileExtension
                self.__gameCenterEnabled = gameCenterEnabled
                self.__gameCenterEverEnabled = gameCenterEverEnabled
                self.__genre = genre
                self.__genreId = genreId
                self.__itemId = itemId
                self.__itemName = itemName
                self.__kind = kind
                self.__playlistName = playlistName
                self.__product_type = product_type
                self.__rating = rating
                self.__releaseDate = releaseDate
                self.__requiresRosetta = requiresRosetta
                self.__runsOnAppleSilicon = runsOnAppleSilicon
                self.__runsOnIntel = runsOnIntel
                self.__s = s
                self.__software_platform = software_platform
                self.__softwareIcon57x57URL = softwareIcon57x57URL
                self.__softwareIconNeedsShine = softwareIconNeedsShine
                self.__softwareSupportedDeviceIds = softwareSupportedDeviceIds
                self.__softwareVersionBundleId = softwareVersionBundleId
                self.__softwareVersionExternalIdentifier = (
                    softwareVersionExternalIdentifier
                )
                self.__softwareVersionExternalIdentifiers = (
                    softwareVersionExternalIdentifiers
                )
                self.__subgenres = subgenres
                self.__vendorId = vendorId
                self.__drmVersionNumber = drmVersionNumber
                self.__versionRestrictions = versionRestrictions

            def _get_MacUIRequiredDeviceCapabilities(self):
                return self.__MacUIRequiredDeviceCapabilities

            def _set_MacUIRequiredDeviceCapabilities(self, value):
                if not isinstance(
                    value,
                    StoreDownloadResp._songList._metadata._MacUIRequiredDeviceCapabilities,
                ):
                    raise TypeError(
                        "MacUIRequiredDeviceCapabilities must be StoreDownloadResp._songList._metadata._MacUIRequiredDeviceCapabilities"
                    )

                self.__MacUIRequiredDeviceCapabilities = value

            MacUIRequiredDeviceCapabilities = property(
                _get_MacUIRequiredDeviceCapabilities,
                _set_MacUIRequiredDeviceCapabilities,
            )

            def _get_UIRequiredDeviceCapabilities(self):
                return self.__UIRequiredDeviceCapabilities

            def _set_UIRequiredDeviceCapabilities(self, value):
                if not isinstance(
                    value,
                    StoreDownloadResp._songList._metadata._UIRequiredDeviceCapabilities,
                ):
                    raise TypeError(
                        "UIRequiredDeviceCapabilities must be StoreDownloadResp._songList._metadata._UIRequiredDeviceCapabilities"
                    )

                self.__UIRequiredDeviceCapabilities = value

            UIRequiredDeviceCapabilities = property(
                _get_UIRequiredDeviceCapabilities, _set_UIRequiredDeviceCapabilities
            )

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

            def _get_bundleDisplayName(self):
                return self.__bundleDisplayName

            def _set_bundleDisplayName(self, value):
                if not isinstance(value, str):
                    raise TypeError("bundleDisplayName must be str")

                self.__bundleDisplayName = value

            bundleDisplayName = property(_get_bundleDisplayName, _set_bundleDisplayName)

            def _get_bundleShortVersionString(self):
                return self.__bundleShortVersionString

            def _set_bundleShortVersionString(self, value):
                if not isinstance(value, str):
                    raise TypeError("bundleShortVersionString must be str")

                self.__bundleShortVersionString = value

            bundleShortVersionString = property(
                _get_bundleShortVersionString, _set_bundleShortVersionString
            )

            def _get_bundleVersion(self):
                return self.__bundleVersion

            def _set_bundleVersion(self, value):
                if not isinstance(value, str):
                    raise TypeError("bundleVersion must be str")

                self.__bundleVersion = value

            bundleVersion = property(_get_bundleVersion, _set_bundleVersion)

            def _get_copyright(self):
                return self.__copyright

            def _set_copyright(self, value):
                if not isinstance(value, str):
                    raise TypeError("copyright must be str")

                self.__copyright = value

            copyright = property(_get_copyright, _set_copyright)

            def _get_fileExtension(self):
                return self.__fileExtension

            def _set_fileExtension(self, value):
                if not isinstance(value, str):
                    raise TypeError("fileExtension must be str")

                self.__fileExtension = value

            fileExtension = property(_get_fileExtension, _set_fileExtension)

            def _get_gameCenterEnabled(self):
                return self.__gameCenterEnabled

            def _set_gameCenterEnabled(self, value):
                if not isinstance(value, bool):
                    raise TypeError("gameCenterEnabled must be bool")

                self.__gameCenterEnabled = value

            gameCenterEnabled = property(_get_gameCenterEnabled, _set_gameCenterEnabled)

            def _get_gameCenterEverEnabled(self):
                return self.__gameCenterEverEnabled

            def _set_gameCenterEverEnabled(self, value):
                if not isinstance(value, bool):
                    raise TypeError("gameCenterEverEnabled must be bool")

                self.__gameCenterEverEnabled = value

            gameCenterEverEnabled = property(
                _get_gameCenterEverEnabled, _set_gameCenterEverEnabled
            )

            def _get_genre(self):
                return self.__genre

            def _set_genre(self, value):
                if not isinstance(value, str):
                    raise TypeError("genre must be str")

                self.__genre = value

            genre = property(_get_genre, _set_genre)

            def _get_genreId(self):
                return self.__genreId

            def _set_genreId(self, value):
                if not isinstance(value, int):
                    raise TypeError("genreId must be int")

                self.__genreId = value

            genreId = property(_get_genreId, _set_genreId)

            def _get_itemId(self):
                return self.__itemId

            def _set_itemId(self, value):
                if not isinstance(value, int):
                    raise TypeError("itemId must be int")

                self.__itemId = value

            itemId = property(_get_itemId, _set_itemId)

            def _get_itemName(self):
                return self.__itemName

            def _set_itemName(self, value):
                if not isinstance(value, str):
                    raise TypeError("itemName must be str")

                self.__itemName = value

            itemName = property(_get_itemName, _set_itemName)

            def _get_kind(self):
                return self.__kind

            def _set_kind(self, value):
                if not isinstance(value, str):
                    raise TypeError("kind must be str")

                self.__kind = value

            kind = property(_get_kind, _set_kind)

            def _get_playlistName(self):
                return self.__playlistName

            def _set_playlistName(self, value):
                if not isinstance(value, str):
                    raise TypeError("playlistName must be str")

                self.__playlistName = value

            playlistName = property(_get_playlistName, _set_playlistName)

            def _get_product_type(self):
                return self.__product_type

            def _set_product_type(self, value):
                if not isinstance(value, str):
                    raise TypeError("product_type must be str")

                self.__product_type = value

            product_type = property(_get_product_type, _set_product_type)

            def _get_rating(self):
                return self.__rating

            def _set_rating(self, value):
                if not isinstance(value, StoreDownloadResp._songList._metadata._rating):
                    raise TypeError(
                        "rating must be StoreDownloadResp._songList._metadata._rating"
                    )

                self.__rating = value

            rating = property(_get_rating, _set_rating)

            def _get_releaseDate(self):
                return self.__releaseDate

            def _set_releaseDate(self, value):
                if not isinstance(value, str):
                    raise TypeError("releaseDate must be str")

                self.__releaseDate = value

            releaseDate = property(_get_releaseDate, _set_releaseDate)

            def _get_requiresRosetta(self):
                return self.__requiresRosetta

            def _set_requiresRosetta(self, value):
                if not isinstance(value, bool):
                    raise TypeError("requiresRosetta must be bool")

                self.__requiresRosetta = value

            requiresRosetta = property(_get_requiresRosetta, _set_requiresRosetta)

            def _get_runsOnAppleSilicon(self):
                return self.__runsOnAppleSilicon

            def _set_runsOnAppleSilicon(self, value):
                if not isinstance(value, bool):
                    raise TypeError("runsOnAppleSilicon must be bool")

                self.__runsOnAppleSilicon = value

            runsOnAppleSilicon = property(
                _get_runsOnAppleSilicon, _set_runsOnAppleSilicon
            )

            def _get_runsOnIntel(self):
                return self.__runsOnIntel

            def _set_runsOnIntel(self, value):
                if not isinstance(value, bool):
                    raise TypeError("runsOnIntel must be bool")

                self.__runsOnIntel = value

            runsOnIntel = property(_get_runsOnIntel, _set_runsOnIntel)

            def _get_s(self):
                return self.__s

            def _set_s(self, value):
                if not isinstance(value, int):
                    raise TypeError("s must be int")

                self.__s = value

            s = property(_get_s, _set_s)

            def _get_software_platform(self):
                return self.__software_platform

            def _set_software_platform(self, value):
                if not isinstance(value, str):
                    raise TypeError("software_platform must be str")

                self.__software_platform = value

            software_platform = property(_get_software_platform, _set_software_platform)

            def _get_softwareIcon57x57URL(self):
                return self.__softwareIcon57x57URL

            def _set_softwareIcon57x57URL(self, value):
                if not isinstance(value, str):
                    raise TypeError("softwareIcon57x57URL must be str")

                self.__softwareIcon57x57URL = value

            softwareIcon57x57URL = property(
                _get_softwareIcon57x57URL, _set_softwareIcon57x57URL
            )

            def _get_softwareIconNeedsShine(self):
                return self.__softwareIconNeedsShine

            def _set_softwareIconNeedsShine(self, value):
                if not isinstance(value, bool):
                    raise TypeError("softwareIconNeedsShine must be bool")

                self.__softwareIconNeedsShine = value

            softwareIconNeedsShine = property(
                _get_softwareIconNeedsShine, _set_softwareIconNeedsShine
            )

            def _get_softwareSupportedDeviceIds(self):
                return self.__softwareSupportedDeviceIds

            def _set_softwareSupportedDeviceIds(self, value):
                if not isinstance(value, list):
                    raise TypeError("softwareSupportedDeviceIds must be list")
                if not all(isinstance(i, int) for i in value):
                    raise TypeError(
                        "softwareSupportedDeviceIds list values must be int"
                    )

                self.__softwareSupportedDeviceIds = value

            softwareSupportedDeviceIds = property(
                _get_softwareSupportedDeviceIds, _set_softwareSupportedDeviceIds
            )

            def _get_softwareVersionBundleId(self):
                return self.__softwareVersionBundleId

            def _set_softwareVersionBundleId(self, value):
                if not isinstance(value, str):
                    raise TypeError("softwareVersionBundleId must be str")

                self.__softwareVersionBundleId = value

            softwareVersionBundleId = property(
                _get_softwareVersionBundleId, _set_softwareVersionBundleId
            )

            def _get_softwareVersionExternalIdentifier(self):
                return self.__softwareVersionExternalIdentifier

            def _set_softwareVersionExternalIdentifier(self, value):
                if not isinstance(value, int):
                    raise TypeError("softwareVersionExternalIdentifier must be int")

                self.__softwareVersionExternalIdentifier = value

            softwareVersionExternalIdentifier = property(
                _get_softwareVersionExternalIdentifier,
                _set_softwareVersionExternalIdentifier,
            )

            def _get_softwareVersionExternalIdentifiers(self):
                return self.__softwareVersionExternalIdentifiers

            def _set_softwareVersionExternalIdentifiers(self, value):
                if not isinstance(value, list):
                    raise TypeError("softwareVersionExternalIdentifiers must be list")
                if not all(isinstance(i, int) for i in value):
                    raise TypeError(
                        "softwareVersionExternalIdentifiers list values must be int"
                    )

                self.__softwareVersionExternalIdentifiers = value

            softwareVersionExternalIdentifiers = property(
                _get_softwareVersionExternalIdentifiers,
                _set_softwareVersionExternalIdentifiers,
            )

            def _get_subgenres(self):
                return self.__subgenres

            def _set_subgenres(self, value):
                if not isinstance(value, list):
                    raise TypeError("subgenres must be list")
                if not all(
                    isinstance(i, StoreDownloadResp._songList._metadata._subgenres)
                    for i in value
                ):
                    raise TypeError(
                        "subgenres list values must be StoreDownloadResp._songList._metadata._subgenres"
                    )

                self.__subgenres = value

            subgenres = property(_get_subgenres, _set_subgenres)

            def _get_vendorId(self):
                return self.__vendorId

            def _set_vendorId(self, value):
                if not isinstance(value, int):
                    raise TypeError("vendorId must be int")

                self.__vendorId = value

            vendorId = property(_get_vendorId, _set_vendorId)

            def _get_drmVersionNumber(self):
                return self.__drmVersionNumber

            def _set_drmVersionNumber(self, value):
                if not isinstance(value, int):
                    raise TypeError("drmVersionNumber must be int")

                self.__drmVersionNumber = value

            drmVersionNumber = property(_get_drmVersionNumber, _set_drmVersionNumber)

            def _get_versionRestrictions(self):
                return self.__versionRestrictions

            def _set_versionRestrictions(self, value):
                if not isinstance(value, int):
                    raise TypeError("versionRestrictions must be int")

                self.__versionRestrictions = value

            versionRestrictions = property(
                _get_versionRestrictions, _set_versionRestrictions
            )

            @staticmethod
            def from_dict(d):
                v = {}
                if "MacUIRequiredDeviceCapabilities" in d:
                    v["MacUIRequiredDeviceCapabilities"] = (
                        StoreDownloadResp._songList._metadata._MacUIRequiredDeviceCapabilities.from_dict(
                            d["MacUIRequiredDeviceCapabilities"]
                        )
                        if hasattr(
                            StoreDownloadResp._songList._metadata._MacUIRequiredDeviceCapabilities,
                            "from_dict",
                        )
                        else d["MacUIRequiredDeviceCapabilities"]
                    )
                if "UIRequiredDeviceCapabilities" in d:
                    v["UIRequiredDeviceCapabilities"] = (
                        StoreDownloadResp._songList._metadata._UIRequiredDeviceCapabilities.from_dict(
                            d["UIRequiredDeviceCapabilities"]
                        )
                        if hasattr(
                            StoreDownloadResp._songList._metadata._UIRequiredDeviceCapabilities,
                            "from_dict",
                        )
                        else d["UIRequiredDeviceCapabilities"]
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
                if "bundleDisplayName" in d:
                    v["bundleDisplayName"] = (
                        str.from_dict(d["bundleDisplayName"])
                        if hasattr(str, "from_dict")
                        else d["bundleDisplayName"]
                    )
                if "bundleShortVersionString" in d:
                    v["bundleShortVersionString"] = (
                        str.from_dict(d["bundleShortVersionString"])
                        if hasattr(str, "from_dict")
                        else d["bundleShortVersionString"]
                    )
                if "bundleVersion" in d:
                    v["bundleVersion"] = (
                        str.from_dict(d["bundleVersion"])
                        if hasattr(str, "from_dict")
                        else d["bundleVersion"]
                    )
                if "copyright" in d:
                    v["copyright"] = (
                        str.from_dict(d["copyright"])
                        if hasattr(str, "from_dict")
                        else d["copyright"]
                    )
                if "fileExtension" in d:
                    v["fileExtension"] = (
                        str.from_dict(d["fileExtension"])
                        if hasattr(str, "from_dict")
                        else d["fileExtension"]
                    )
                if "gameCenterEnabled" in d:
                    v["gameCenterEnabled"] = (
                        bool.from_dict(d["gameCenterEnabled"])
                        if hasattr(bool, "from_dict")
                        else d["gameCenterEnabled"]
                    )
                if "gameCenterEverEnabled" in d:
                    v["gameCenterEverEnabled"] = (
                        bool.from_dict(d["gameCenterEverEnabled"])
                        if hasattr(bool, "from_dict")
                        else d["gameCenterEverEnabled"]
                    )
                if "genre" in d:
                    v["genre"] = (
                        str.from_dict(d["genre"])
                        if hasattr(str, "from_dict")
                        else d["genre"]
                    )
                if "genreId" in d:
                    v["genreId"] = (
                        int.from_dict(d["genreId"])
                        if hasattr(int, "from_dict")
                        else d["genreId"]
                    )
                if "itemId" in d:
                    v["itemId"] = (
                        int.from_dict(d["itemId"])
                        if hasattr(int, "from_dict")
                        else d["itemId"]
                    )
                if "itemName" in d:
                    v["itemName"] = (
                        str.from_dict(d["itemName"])
                        if hasattr(str, "from_dict")
                        else d["itemName"]
                    )
                if "kind" in d:
                    v["kind"] = (
                        str.from_dict(d["kind"])
                        if hasattr(str, "from_dict")
                        else d["kind"]
                    )
                if "playlistName" in d:
                    v["playlistName"] = (
                        str.from_dict(d["playlistName"])
                        if hasattr(str, "from_dict")
                        else d["playlistName"]
                    )
                if "product-type" in d:
                    v["product_type"] = (
                        str.from_dict(d["product-type"])
                        if hasattr(str, "from_dict")
                        else d["product-type"]
                    )
                if "rating" in d:
                    v["rating"] = (
                        StoreDownloadResp._songList._metadata._rating.from_dict(
                            d["rating"]
                        )
                        if hasattr(
                            StoreDownloadResp._songList._metadata._rating, "from_dict"
                        )
                        else d["rating"]
                    )
                if "releaseDate" in d:
                    v["releaseDate"] = (
                        str.from_dict(d["releaseDate"])
                        if hasattr(str, "from_dict")
                        else d["releaseDate"]
                    )
                if "requiresRosetta" in d:
                    v["requiresRosetta"] = (
                        bool.from_dict(d["requiresRosetta"])
                        if hasattr(bool, "from_dict")
                        else d["requiresRosetta"]
                    )
                if "runsOnAppleSilicon" in d:
                    v["runsOnAppleSilicon"] = (
                        bool.from_dict(d["runsOnAppleSilicon"])
                        if hasattr(bool, "from_dict")
                        else d["runsOnAppleSilicon"]
                    )
                if "runsOnIntel" in d:
                    v["runsOnIntel"] = (
                        bool.from_dict(d["runsOnIntel"])
                        if hasattr(bool, "from_dict")
                        else d["runsOnIntel"]
                    )
                if "s" in d:
                    v["s"] = (
                        int.from_dict(d["s"]) if hasattr(int, "from_dict") else d["s"]
                    )
                if "software-platform" in d:
                    v["software_platform"] = (
                        str.from_dict(d["software-platform"])
                        if hasattr(str, "from_dict")
                        else d["software-platform"]
                    )
                if "softwareIcon57x57URL" in d:
                    v["softwareIcon57x57URL"] = (
                        str.from_dict(d["softwareIcon57x57URL"])
                        if hasattr(str, "from_dict")
                        else d["softwareIcon57x57URL"]
                    )
                if "softwareIconNeedsShine" in d:
                    v["softwareIconNeedsShine"] = (
                        bool.from_dict(d["softwareIconNeedsShine"])
                        if hasattr(bool, "from_dict")
                        else d["softwareIconNeedsShine"]
                    )
                if "softwareSupportedDeviceIds" in d:
                    v["softwareSupportedDeviceIds"] = [
                        int.from_dict(p) if hasattr(int, "from_dict") else p
                        for p in d["softwareSupportedDeviceIds"]
                    ]
                if "softwareVersionBundleId" in d:
                    v["softwareVersionBundleId"] = (
                        str.from_dict(d["softwareVersionBundleId"])
                        if hasattr(str, "from_dict")
                        else d["softwareVersionBundleId"]
                    )
                if "softwareVersionExternalIdentifier" in d:
                    v["softwareVersionExternalIdentifier"] = (
                        int.from_dict(d["softwareVersionExternalIdentifier"])
                        if hasattr(int, "from_dict")
                        else d["softwareVersionExternalIdentifier"]
                    )
                if "softwareVersionExternalIdentifiers" in d:
                    v["softwareVersionExternalIdentifiers"] = [
                        int.from_dict(p) if hasattr(int, "from_dict") else p
                        for p in d["softwareVersionExternalIdentifiers"]
                    ]
                if "subgenres" in d:
                    v["subgenres"] = [
                        StoreDownloadResp._songList._metadata._subgenres.from_dict(p)
                        if hasattr(
                            StoreDownloadResp._songList._metadata._subgenres,
                            "from_dict",
                        )
                        else p
                        for p in d["subgenres"]
                    ]
                if "vendorId" in d:
                    v["vendorId"] = (
                        int.from_dict(d["vendorId"])
                        if hasattr(int, "from_dict")
                        else d["vendorId"]
                    )
                if "drmVersionNumber" in d:
                    v["drmVersionNumber"] = (
                        int.from_dict(d["drmVersionNumber"])
                        if hasattr(int, "from_dict")
                        else d["drmVersionNumber"]
                    )
                if "versionRestrictions" in d:
                    v["versionRestrictions"] = (
                        int.from_dict(d["versionRestrictions"])
                        if hasattr(int, "from_dict")
                        else d["versionRestrictions"]
                    )
                return StoreDownloadResp._songList._metadata(**v)

            def as_dict(self):
                d = {}
                if self.__MacUIRequiredDeviceCapabilities is not None:
                    d["MacUIRequiredDeviceCapabilities"] = (
                        self.__MacUIRequiredDeviceCapabilities.as_dict()
                        if hasattr(self.__MacUIRequiredDeviceCapabilities, "as_dict")
                        else self.__MacUIRequiredDeviceCapabilities
                    )
                if self.__UIRequiredDeviceCapabilities is not None:
                    d["UIRequiredDeviceCapabilities"] = (
                        self.__UIRequiredDeviceCapabilities.as_dict()
                        if hasattr(self.__UIRequiredDeviceCapabilities, "as_dict")
                        else self.__UIRequiredDeviceCapabilities
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
                if self.__bundleDisplayName is not None:
                    d["bundleDisplayName"] = (
                        self.__bundleDisplayName.as_dict()
                        if hasattr(self.__bundleDisplayName, "as_dict")
                        else self.__bundleDisplayName
                    )
                if self.__bundleShortVersionString is not None:
                    d["bundleShortVersionString"] = (
                        self.__bundleShortVersionString.as_dict()
                        if hasattr(self.__bundleShortVersionString, "as_dict")
                        else self.__bundleShortVersionString
                    )
                if self.__bundleVersion is not None:
                    d["bundleVersion"] = (
                        self.__bundleVersion.as_dict()
                        if hasattr(self.__bundleVersion, "as_dict")
                        else self.__bundleVersion
                    )
                if self.__copyright is not None:
                    d["copyright"] = (
                        self.__copyright.as_dict()
                        if hasattr(self.__copyright, "as_dict")
                        else self.__copyright
                    )
                if self.__fileExtension is not None:
                    d["fileExtension"] = (
                        self.__fileExtension.as_dict()
                        if hasattr(self.__fileExtension, "as_dict")
                        else self.__fileExtension
                    )
                if self.__gameCenterEnabled is not None:
                    d["gameCenterEnabled"] = (
                        self.__gameCenterEnabled.as_dict()
                        if hasattr(self.__gameCenterEnabled, "as_dict")
                        else self.__gameCenterEnabled
                    )
                if self.__gameCenterEverEnabled is not None:
                    d["gameCenterEverEnabled"] = (
                        self.__gameCenterEverEnabled.as_dict()
                        if hasattr(self.__gameCenterEverEnabled, "as_dict")
                        else self.__gameCenterEverEnabled
                    )
                if self.__genre is not None:
                    d["genre"] = (
                        self.__genre.as_dict()
                        if hasattr(self.__genre, "as_dict")
                        else self.__genre
                    )
                if self.__genreId is not None:
                    d["genreId"] = (
                        self.__genreId.as_dict()
                        if hasattr(self.__genreId, "as_dict")
                        else self.__genreId
                    )
                if self.__itemId is not None:
                    d["itemId"] = (
                        self.__itemId.as_dict()
                        if hasattr(self.__itemId, "as_dict")
                        else self.__itemId
                    )
                if self.__itemName is not None:
                    d["itemName"] = (
                        self.__itemName.as_dict()
                        if hasattr(self.__itemName, "as_dict")
                        else self.__itemName
                    )
                if self.__kind is not None:
                    d["kind"] = (
                        self.__kind.as_dict()
                        if hasattr(self.__kind, "as_dict")
                        else self.__kind
                    )
                if self.__playlistName is not None:
                    d["playlistName"] = (
                        self.__playlistName.as_dict()
                        if hasattr(self.__playlistName, "as_dict")
                        else self.__playlistName
                    )
                if self.__product_type is not None:
                    d["product-type"] = (
                        self.__product_type.as_dict()
                        if hasattr(self.__product_type, "as_dict")
                        else self.__product_type
                    )
                if self.__rating is not None:
                    d["rating"] = (
                        self.__rating.as_dict()
                        if hasattr(self.__rating, "as_dict")
                        else self.__rating
                    )
                if self.__releaseDate is not None:
                    d["releaseDate"] = (
                        self.__releaseDate.as_dict()
                        if hasattr(self.__releaseDate, "as_dict")
                        else self.__releaseDate
                    )
                if self.__requiresRosetta is not None:
                    d["requiresRosetta"] = (
                        self.__requiresRosetta.as_dict()
                        if hasattr(self.__requiresRosetta, "as_dict")
                        else self.__requiresRosetta
                    )
                if self.__runsOnAppleSilicon is not None:
                    d["runsOnAppleSilicon"] = (
                        self.__runsOnAppleSilicon.as_dict()
                        if hasattr(self.__runsOnAppleSilicon, "as_dict")
                        else self.__runsOnAppleSilicon
                    )
                if self.__runsOnIntel is not None:
                    d["runsOnIntel"] = (
                        self.__runsOnIntel.as_dict()
                        if hasattr(self.__runsOnIntel, "as_dict")
                        else self.__runsOnIntel
                    )
                if self.__s is not None:
                    d["s"] = (
                        self.__s.as_dict() if hasattr(self.__s, "as_dict") else self.__s
                    )
                if self.__software_platform is not None:
                    d["software-platform"] = (
                        self.__software_platform.as_dict()
                        if hasattr(self.__software_platform, "as_dict")
                        else self.__software_platform
                    )
                if self.__softwareIcon57x57URL is not None:
                    d["softwareIcon57x57URL"] = (
                        self.__softwareIcon57x57URL.as_dict()
                        if hasattr(self.__softwareIcon57x57URL, "as_dict")
                        else self.__softwareIcon57x57URL
                    )
                if self.__softwareIconNeedsShine is not None:
                    d["softwareIconNeedsShine"] = (
                        self.__softwareIconNeedsShine.as_dict()
                        if hasattr(self.__softwareIconNeedsShine, "as_dict")
                        else self.__softwareIconNeedsShine
                    )
                if self.__softwareSupportedDeviceIds is not None:
                    d["softwareSupportedDeviceIds"] = [
                        p.as_dict() if hasattr(p, "as_dict") else p
                        for p in self.__softwareSupportedDeviceIds
                    ]
                if self.__softwareVersionBundleId is not None:
                    d["softwareVersionBundleId"] = (
                        self.__softwareVersionBundleId.as_dict()
                        if hasattr(self.__softwareVersionBundleId, "as_dict")
                        else self.__softwareVersionBundleId
                    )
                if self.__softwareVersionExternalIdentifier is not None:
                    d["softwareVersionExternalIdentifier"] = (
                        self.__softwareVersionExternalIdentifier.as_dict()
                        if hasattr(self.__softwareVersionExternalIdentifier, "as_dict")
                        else self.__softwareVersionExternalIdentifier
                    )
                if self.__softwareVersionExternalIdentifiers is not None:
                    d["softwareVersionExternalIdentifiers"] = [
                        p.as_dict() if hasattr(p, "as_dict") else p
                        for p in self.__softwareVersionExternalIdentifiers
                    ]
                if self.__subgenres is not None:
                    d["subgenres"] = [
                        p.as_dict() if hasattr(p, "as_dict") else p
                        for p in self.__subgenres
                    ]
                if self.__vendorId is not None:
                    d["vendorId"] = (
                        self.__vendorId.as_dict()
                        if hasattr(self.__vendorId, "as_dict")
                        else self.__vendorId
                    )
                if self.__drmVersionNumber is not None:
                    d["drmVersionNumber"] = (
                        self.__drmVersionNumber.as_dict()
                        if hasattr(self.__drmVersionNumber, "as_dict")
                        else self.__drmVersionNumber
                    )
                if self.__versionRestrictions is not None:
                    d["versionRestrictions"] = (
                        self.__versionRestrictions.as_dict()
                        if hasattr(self.__versionRestrictions, "as_dict")
                        else self.__versionRestrictions
                    )
                return d

            def __repr__(self):
                return "<Class _metadata. MacUIRequiredDeviceCapabilities: {}, UIRequiredDeviceCapabilities: {}, artistId: {}, artistName: {}, bundleDisplayName: {}, bundleShortVersionString: {}, bundleVersion: {}, copyright: {}, fileExtension: {}, gameCenterEnabled: {}, gameCenterEverEnabled: {}, genre: {}, genreId: {}, itemId: {}, itemName: {}, kind: {}, playlistName: {}, product_type: {}, rating: {}, releaseDate: {}, requiresRosetta: {}, runsOnAppleSilicon: {}, runsOnIntel: {}, s: {}, software_platform: {}, softwareIcon57x57URL: {}, softwareIconNeedsShine: {}, softwareSupportedDeviceIds: {}, softwareVersionBundleId: {}, softwareVersionExternalIdentifier: {}, softwareVersionExternalIdentifiers: {}, subgenres: {}, vendorId: {}, drmVersionNumber: {}, versionRestrictions: {}>".format(
                    limitedRepr(
                        self.__MacUIRequiredDeviceCapabilities[:20]
                        if isinstance(self.__MacUIRequiredDeviceCapabilities, bytes)
                        else self.__MacUIRequiredDeviceCapabilities
                    ),
                    limitedRepr(
                        self.__UIRequiredDeviceCapabilities[:20]
                        if isinstance(self.__UIRequiredDeviceCapabilities, bytes)
                        else self.__UIRequiredDeviceCapabilities
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
                        self.__bundleDisplayName[:20]
                        if isinstance(self.__bundleDisplayName, bytes)
                        else self.__bundleDisplayName
                    ),
                    limitedRepr(
                        self.__bundleShortVersionString[:20]
                        if isinstance(self.__bundleShortVersionString, bytes)
                        else self.__bundleShortVersionString
                    ),
                    limitedRepr(
                        self.__bundleVersion[:20]
                        if isinstance(self.__bundleVersion, bytes)
                        else self.__bundleVersion
                    ),
                    limitedRepr(
                        self.__copyright[:20]
                        if isinstance(self.__copyright, bytes)
                        else self.__copyright
                    ),
                    limitedRepr(
                        self.__fileExtension[:20]
                        if isinstance(self.__fileExtension, bytes)
                        else self.__fileExtension
                    ),
                    limitedRepr(
                        self.__gameCenterEnabled[:20]
                        if isinstance(self.__gameCenterEnabled, bytes)
                        else self.__gameCenterEnabled
                    ),
                    limitedRepr(
                        self.__gameCenterEverEnabled[:20]
                        if isinstance(self.__gameCenterEverEnabled, bytes)
                        else self.__gameCenterEverEnabled
                    ),
                    limitedRepr(
                        self.__genre[:20]
                        if isinstance(self.__genre, bytes)
                        else self.__genre
                    ),
                    limitedRepr(
                        self.__genreId[:20]
                        if isinstance(self.__genreId, bytes)
                        else self.__genreId
                    ),
                    limitedRepr(
                        self.__itemId[:20]
                        if isinstance(self.__itemId, bytes)
                        else self.__itemId
                    ),
                    limitedRepr(
                        self.__itemName[:20]
                        if isinstance(self.__itemName, bytes)
                        else self.__itemName
                    ),
                    limitedRepr(
                        self.__kind[:20]
                        if isinstance(self.__kind, bytes)
                        else self.__kind
                    ),
                    limitedRepr(
                        self.__playlistName[:20]
                        if isinstance(self.__playlistName, bytes)
                        else self.__playlistName
                    ),
                    limitedRepr(
                        self.__product_type[:20]
                        if isinstance(self.__product_type, bytes)
                        else self.__product_type
                    ),
                    limitedRepr(
                        self.__rating[:20]
                        if isinstance(self.__rating, bytes)
                        else self.__rating
                    ),
                    limitedRepr(
                        self.__releaseDate[:20]
                        if isinstance(self.__releaseDate, bytes)
                        else self.__releaseDate
                    ),
                    limitedRepr(
                        self.__requiresRosetta[:20]
                        if isinstance(self.__requiresRosetta, bytes)
                        else self.__requiresRosetta
                    ),
                    limitedRepr(
                        self.__runsOnAppleSilicon[:20]
                        if isinstance(self.__runsOnAppleSilicon, bytes)
                        else self.__runsOnAppleSilicon
                    ),
                    limitedRepr(
                        self.__runsOnIntel[:20]
                        if isinstance(self.__runsOnIntel, bytes)
                        else self.__runsOnIntel
                    ),
                    limitedRepr(
                        self.__s[:20] if isinstance(self.__s, bytes) else self.__s
                    ),
                    limitedRepr(
                        self.__software_platform[:20]
                        if isinstance(self.__software_platform, bytes)
                        else self.__software_platform
                    ),
                    limitedRepr(
                        self.__softwareIcon57x57URL[:20]
                        if isinstance(self.__softwareIcon57x57URL, bytes)
                        else self.__softwareIcon57x57URL
                    ),
                    limitedRepr(
                        self.__softwareIconNeedsShine[:20]
                        if isinstance(self.__softwareIconNeedsShine, bytes)
                        else self.__softwareIconNeedsShine
                    ),
                    limitedRepr(
                        self.__softwareSupportedDeviceIds[:20]
                        if isinstance(self.__softwareSupportedDeviceIds, bytes)
                        else self.__softwareSupportedDeviceIds
                    ),
                    limitedRepr(
                        self.__softwareVersionBundleId[:20]
                        if isinstance(self.__softwareVersionBundleId, bytes)
                        else self.__softwareVersionBundleId
                    ),
                    limitedRepr(
                        self.__softwareVersionExternalIdentifier[:20]
                        if isinstance(self.__softwareVersionExternalIdentifier, bytes)
                        else self.__softwareVersionExternalIdentifier
                    ),
                    limitedRepr(
                        self.__softwareVersionExternalIdentifiers[:20]
                        if isinstance(self.__softwareVersionExternalIdentifiers, bytes)
                        else self.__softwareVersionExternalIdentifiers
                    ),
                    limitedRepr(
                        self.__subgenres[:20]
                        if isinstance(self.__subgenres, bytes)
                        else self.__subgenres
                    ),
                    limitedRepr(
                        self.__vendorId[:20]
                        if isinstance(self.__vendorId, bytes)
                        else self.__vendorId
                    ),
                    limitedRepr(
                        self.__drmVersionNumber[:20]
                        if isinstance(self.__drmVersionNumber, bytes)
                        else self.__drmVersionNumber
                    ),
                    limitedRepr(
                        self.__versionRestrictions[:20]
                        if isinstance(self.__versionRestrictions, bytes)
                        else self.__versionRestrictions
                    ),
                )

        _types_map = {
            "songId": {"type": int, "subtype": None},
            "URL": {"type": str, "subtype": None},
            "downloadKey": {"type": str, "subtype": None},
            "artworkURL": {"type": str, "subtype": None},
            "artwork_urls": {"type": _artwork_urls, "subtype": None},
            "md5": {"type": str, "subtype": None},
            "chunks": {"type": _chunks, "subtype": None},
            "isStreamable": {"type": bool, "subtype": None},
            "uncompressedSize": {"type": str, "subtype": None},
            "sinfs": {"type": list, "subtype": _sinfs},
            "purchaseDate": {"type": str, "subtype": None},
            "download_id": {"type": str, "subtype": None},
            "is_in_queue": {"type": bool, "subtype": None},
            "asset_info": {"type": _asset_info, "subtype": None},
            "metadata": {"type": _metadata, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "songId": {
                "required": True,
            },
            "URL": {
                "required": True,
            },
            "downloadKey": {
                "required": True,
            },
            "artworkURL": {
                "required": True,
            },
            "artwork_urls": {
                "required": True,
            },
            "md5": {
                "required": True,
            },
            "chunks": {
                "required": True,
            },
            "isStreamable": {
                "required": True,
            },
            "uncompressedSize": {
                "required": True,
            },
            "sinfs": {
                "required": True,
            },
            "purchaseDate": {
                "required": True,
            },
            "download_id": {
                "required": True,
            },
            "is_in_queue": {
                "required": True,
            },
            "asset_info": {
                "required": True,
            },
            "metadata": {
                "required": True,
            },
        }

        def __init__(
            self,
            songId: int = None,
            URL: str = None,
            downloadKey: str = None,
            artworkURL: str = None,
            artwork_urls: _artwork_urls = None,
            md5: str = None,
            chunks: _chunks = None,
            isStreamable: bool = None,
            uncompressedSize: str = None,
            sinfs: List[_sinfs] = None,
            purchaseDate: str = None,
            download_id: str = None,
            is_in_queue: bool = None,
            asset_info: _asset_info = None,
            metadata: _metadata = None,
        ):
            pass
            self.__songId = songId
            self.__URL = URL
            self.__downloadKey = downloadKey
            self.__artworkURL = artworkURL
            self.__artwork_urls = artwork_urls
            self.__md5 = md5
            self.__chunks = chunks
            self.__isStreamable = isStreamable
            self.__uncompressedSize = uncompressedSize
            self.__sinfs = sinfs
            self.__purchaseDate = purchaseDate
            self.__download_id = download_id
            self.__is_in_queue = is_in_queue
            self.__asset_info = asset_info
            self.__metadata = metadata

        def _get_songId(self):
            return self.__songId

        def _set_songId(self, value):
            if not isinstance(value, int):
                raise TypeError("songId must be int")

            self.__songId = value

        songId = property(_get_songId, _set_songId)

        def _get_URL(self):
            return self.__URL

        def _set_URL(self, value):
            if not isinstance(value, str):
                raise TypeError("URL must be str")

            self.__URL = value

        URL = property(_get_URL, _set_URL)

        def _get_downloadKey(self):
            return self.__downloadKey

        def _set_downloadKey(self, value):
            if not isinstance(value, str):
                raise TypeError("downloadKey must be str")

            self.__downloadKey = value

        downloadKey = property(_get_downloadKey, _set_downloadKey)

        def _get_artworkURL(self):
            return self.__artworkURL

        def _set_artworkURL(self, value):
            if not isinstance(value, str):
                raise TypeError("artworkURL must be str")

            self.__artworkURL = value

        artworkURL = property(_get_artworkURL, _set_artworkURL)

        def _get_artwork_urls(self):
            return self.__artwork_urls

        def _set_artwork_urls(self, value):
            if not isinstance(value, StoreDownloadResp._songList._artwork_urls):
                raise TypeError(
                    "artwork_urls must be StoreDownloadResp._songList._artwork_urls"
                )

            self.__artwork_urls = value

        artwork_urls = property(_get_artwork_urls, _set_artwork_urls)

        def _get_md5(self):
            return self.__md5

        def _set_md5(self, value):
            if not isinstance(value, str):
                raise TypeError("md5 must be str")

            self.__md5 = value

        md5 = property(_get_md5, _set_md5)

        def _get_chunks(self):
            return self.__chunks

        def _set_chunks(self, value):
            if not isinstance(value, StoreDownloadResp._songList._chunks):
                raise TypeError("chunks must be StoreDownloadResp._songList._chunks")

            self.__chunks = value

        chunks = property(_get_chunks, _set_chunks)

        def _get_isStreamable(self):
            return self.__isStreamable

        def _set_isStreamable(self, value):
            if not isinstance(value, bool):
                raise TypeError("isStreamable must be bool")

            self.__isStreamable = value

        isStreamable = property(_get_isStreamable, _set_isStreamable)

        def _get_uncompressedSize(self):
            return self.__uncompressedSize

        def _set_uncompressedSize(self, value):
            if not isinstance(value, str):
                raise TypeError("uncompressedSize must be str")

            self.__uncompressedSize = value

        uncompressedSize = property(_get_uncompressedSize, _set_uncompressedSize)

        def _get_sinfs(self):
            return self.__sinfs

        def _set_sinfs(self, value):
            if not isinstance(value, list):
                raise TypeError("sinfs must be list")
            if not all(
                isinstance(i, StoreDownloadResp._songList._sinfs) for i in value
            ):
                raise TypeError(
                    "sinfs list values must be StoreDownloadResp._songList._sinfs"
                )

            self.__sinfs = value

        sinfs = property(_get_sinfs, _set_sinfs)

        def _get_purchaseDate(self):
            return self.__purchaseDate

        def _set_purchaseDate(self, value):
            if not isinstance(value, str):
                raise TypeError("purchaseDate must be str")

            self.__purchaseDate = value

        purchaseDate = property(_get_purchaseDate, _set_purchaseDate)

        def _get_download_id(self):
            return self.__download_id

        def _set_download_id(self, value):
            if not isinstance(value, str):
                raise TypeError("download_id must be str")

            self.__download_id = value

        download_id = property(_get_download_id, _set_download_id)

        def _get_is_in_queue(self):
            return self.__is_in_queue

        def _set_is_in_queue(self, value):
            if not isinstance(value, bool):
                raise TypeError("is_in_queue must be bool")

            self.__is_in_queue = value

        is_in_queue = property(_get_is_in_queue, _set_is_in_queue)

        def _get_asset_info(self):
            return self.__asset_info

        def _set_asset_info(self, value):
            if not isinstance(value, StoreDownloadResp._songList._asset_info):
                raise TypeError(
                    "asset_info must be StoreDownloadResp._songList._asset_info"
                )

            self.__asset_info = value

        asset_info = property(_get_asset_info, _set_asset_info)

        def _get_metadata(self):
            return self.__metadata

        def _set_metadata(self, value):
            if not isinstance(value, StoreDownloadResp._songList._metadata):
                raise TypeError(
                    "metadata must be StoreDownloadResp._songList._metadata"
                )

            self.__metadata = value

        metadata = property(_get_metadata, _set_metadata)

        @staticmethod
        def from_dict(d):
            v = {}
            if "songId" in d:
                v["songId"] = (
                    int.from_dict(d["songId"])
                    if hasattr(int, "from_dict")
                    else d["songId"]
                )
            if "URL" in d:
                v["URL"] = (
                    str.from_dict(d["URL"]) if hasattr(str, "from_dict") else d["URL"]
                )
            if "downloadKey" in d:
                v["downloadKey"] = (
                    str.from_dict(d["downloadKey"])
                    if hasattr(str, "from_dict")
                    else d["downloadKey"]
                )
            if "artworkURL" in d:
                v["artworkURL"] = (
                    str.from_dict(d["artworkURL"])
                    if hasattr(str, "from_dict")
                    else d["artworkURL"]
                )
            if "artwork-urls" in d:
                v["artwork_urls"] = (
                    StoreDownloadResp._songList._artwork_urls.from_dict(
                        d["artwork-urls"]
                    )
                    if hasattr(StoreDownloadResp._songList._artwork_urls, "from_dict")
                    else d["artwork-urls"]
                )
            if "md5" in d:
                v["md5"] = (
                    str.from_dict(d["md5"]) if hasattr(str, "from_dict") else d["md5"]
                )
            if "chunks" in d:
                v["chunks"] = (
                    StoreDownloadResp._songList._chunks.from_dict(d["chunks"])
                    if hasattr(StoreDownloadResp._songList._chunks, "from_dict")
                    else d["chunks"]
                )
            if "isStreamable" in d:
                v["isStreamable"] = (
                    bool.from_dict(d["isStreamable"])
                    if hasattr(bool, "from_dict")
                    else d["isStreamable"]
                )
            if "uncompressedSize" in d:
                v["uncompressedSize"] = (
                    str.from_dict(d["uncompressedSize"])
                    if hasattr(str, "from_dict")
                    else d["uncompressedSize"]
                )
            if "sinfs" in d:
                v["sinfs"] = [
                    StoreDownloadResp._songList._sinfs.from_dict(p)
                    if hasattr(StoreDownloadResp._songList._sinfs, "from_dict")
                    else p
                    for p in d["sinfs"]
                ]
            if "purchaseDate" in d:
                v["purchaseDate"] = (
                    str.from_dict(d["purchaseDate"])
                    if hasattr(str, "from_dict")
                    else d["purchaseDate"]
                )
            if "download-id" in d:
                v["download_id"] = (
                    str.from_dict(d["download-id"])
                    if hasattr(str, "from_dict")
                    else d["download-id"]
                )
            if "is-in-queue" in d:
                v["is_in_queue"] = (
                    bool.from_dict(d["is-in-queue"])
                    if hasattr(bool, "from_dict")
                    else d["is-in-queue"]
                )
            if "asset-info" in d:
                v["asset_info"] = (
                    StoreDownloadResp._songList._asset_info.from_dict(d["asset-info"])
                    if hasattr(StoreDownloadResp._songList._asset_info, "from_dict")
                    else d["asset-info"]
                )
            if "metadata" in d:
                v["metadata"] = (
                    StoreDownloadResp._songList._metadata.from_dict(d["metadata"])
                    if hasattr(StoreDownloadResp._songList._metadata, "from_dict")
                    else d["metadata"]
                )
            return StoreDownloadResp._songList(**v)

        def as_dict(self):
            d = {}
            if self.__songId is not None:
                d["songId"] = (
                    self.__songId.as_dict()
                    if hasattr(self.__songId, "as_dict")
                    else self.__songId
                )
            if self.__URL is not None:
                d["URL"] = (
                    self.__URL.as_dict()
                    if hasattr(self.__URL, "as_dict")
                    else self.__URL
                )
            if self.__downloadKey is not None:
                d["downloadKey"] = (
                    self.__downloadKey.as_dict()
                    if hasattr(self.__downloadKey, "as_dict")
                    else self.__downloadKey
                )
            if self.__artworkURL is not None:
                d["artworkURL"] = (
                    self.__artworkURL.as_dict()
                    if hasattr(self.__artworkURL, "as_dict")
                    else self.__artworkURL
                )
            if self.__artwork_urls is not None:
                d["artwork-urls"] = (
                    self.__artwork_urls.as_dict()
                    if hasattr(self.__artwork_urls, "as_dict")
                    else self.__artwork_urls
                )
            if self.__md5 is not None:
                d["md5"] = (
                    self.__md5.as_dict()
                    if hasattr(self.__md5, "as_dict")
                    else self.__md5
                )
            if self.__chunks is not None:
                d["chunks"] = (
                    self.__chunks.as_dict()
                    if hasattr(self.__chunks, "as_dict")
                    else self.__chunks
                )
            if self.__isStreamable is not None:
                d["isStreamable"] = (
                    self.__isStreamable.as_dict()
                    if hasattr(self.__isStreamable, "as_dict")
                    else self.__isStreamable
                )
            if self.__uncompressedSize is not None:
                d["uncompressedSize"] = (
                    self.__uncompressedSize.as_dict()
                    if hasattr(self.__uncompressedSize, "as_dict")
                    else self.__uncompressedSize
                )
            if self.__sinfs is not None:
                d["sinfs"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p for p in self.__sinfs
                ]
            if self.__purchaseDate is not None:
                d["purchaseDate"] = (
                    self.__purchaseDate.as_dict()
                    if hasattr(self.__purchaseDate, "as_dict")
                    else self.__purchaseDate
                )
            if self.__download_id is not None:
                d["download-id"] = (
                    self.__download_id.as_dict()
                    if hasattr(self.__download_id, "as_dict")
                    else self.__download_id
                )
            if self.__is_in_queue is not None:
                d["is-in-queue"] = (
                    self.__is_in_queue.as_dict()
                    if hasattr(self.__is_in_queue, "as_dict")
                    else self.__is_in_queue
                )
            if self.__asset_info is not None:
                d["asset-info"] = (
                    self.__asset_info.as_dict()
                    if hasattr(self.__asset_info, "as_dict")
                    else self.__asset_info
                )
            if self.__metadata is not None:
                d["metadata"] = (
                    self.__metadata.as_dict()
                    if hasattr(self.__metadata, "as_dict")
                    else self.__metadata
                )
            return d

        def __repr__(self):
            return "<Class _songList. songId: {}, URL: {}, downloadKey: {}, artworkURL: {}, artwork_urls: {}, md5: {}, chunks: {}, isStreamable: {}, uncompressedSize: {}, sinfs: {}, purchaseDate: {}, download_id: {}, is_in_queue: {}, asset_info: {}, metadata: {}>".format(
                limitedRepr(
                    self.__songId[:20]
                    if isinstance(self.__songId, bytes)
                    else self.__songId
                ),
                limitedRepr(
                    self.__URL[:20] if isinstance(self.__URL, bytes) else self.__URL
                ),
                limitedRepr(
                    self.__downloadKey[:20]
                    if isinstance(self.__downloadKey, bytes)
                    else self.__downloadKey
                ),
                limitedRepr(
                    self.__artworkURL[:20]
                    if isinstance(self.__artworkURL, bytes)
                    else self.__artworkURL
                ),
                limitedRepr(
                    self.__artwork_urls[:20]
                    if isinstance(self.__artwork_urls, bytes)
                    else self.__artwork_urls
                ),
                limitedRepr(
                    self.__md5[:20] if isinstance(self.__md5, bytes) else self.__md5
                ),
                limitedRepr(
                    self.__chunks[:20]
                    if isinstance(self.__chunks, bytes)
                    else self.__chunks
                ),
                limitedRepr(
                    self.__isStreamable[:20]
                    if isinstance(self.__isStreamable, bytes)
                    else self.__isStreamable
                ),
                limitedRepr(
                    self.__uncompressedSize[:20]
                    if isinstance(self.__uncompressedSize, bytes)
                    else self.__uncompressedSize
                ),
                limitedRepr(
                    self.__sinfs[:20]
                    if isinstance(self.__sinfs, bytes)
                    else self.__sinfs
                ),
                limitedRepr(
                    self.__purchaseDate[:20]
                    if isinstance(self.__purchaseDate, bytes)
                    else self.__purchaseDate
                ),
                limitedRepr(
                    self.__download_id[:20]
                    if isinstance(self.__download_id, bytes)
                    else self.__download_id
                ),
                limitedRepr(
                    self.__is_in_queue[:20]
                    if isinstance(self.__is_in_queue, bytes)
                    else self.__is_in_queue
                ),
                limitedRepr(
                    self.__asset_info[:20]
                    if isinstance(self.__asset_info, bytes)
                    else self.__asset_info
                ),
                limitedRepr(
                    self.__metadata[:20]
                    if isinstance(self.__metadata, bytes)
                    else self.__metadata
                ),
            )

    class _metrics:

        _types_map = {
            "itemIds": {"type": list, "subtype": int},
            "currency": {"type": str, "subtype": None},
            "exchangeRateToUSD": {"type": float, "subtype": None},
        }
        _formats_map = {}
        _validations_map = {
            "itemIds": {
                "required": True,
            },
            "currency": {
                "required": True,
            },
            "exchangeRateToUSD": {
                "required": True,
            },
        }

        def __init__(
            self,
            itemIds: List[int] = None,
            currency: str = None,
            exchangeRateToUSD: float = None,
        ):
            pass
            self.__itemIds = itemIds
            self.__currency = currency
            self.__exchangeRateToUSD = exchangeRateToUSD

        def _get_itemIds(self):
            return self.__itemIds

        def _set_itemIds(self, value):
            if not isinstance(value, list):
                raise TypeError("itemIds must be list")
            if not all(isinstance(i, int) for i in value):
                raise TypeError("itemIds list values must be int")

            self.__itemIds = value

        itemIds = property(_get_itemIds, _set_itemIds)

        def _get_currency(self):
            return self.__currency

        def _set_currency(self, value):
            if not isinstance(value, str):
                raise TypeError("currency must be str")

            self.__currency = value

        currency = property(_get_currency, _set_currency)

        def _get_exchangeRateToUSD(self):
            return self.__exchangeRateToUSD

        def _set_exchangeRateToUSD(self, value):
            if not isinstance(value, float):
                raise TypeError("exchangeRateToUSD must be float")

            self.__exchangeRateToUSD = value

        exchangeRateToUSD = property(_get_exchangeRateToUSD, _set_exchangeRateToUSD)

        @staticmethod
        def from_dict(d):
            v = {}
            if "itemIds" in d:
                v["itemIds"] = [
                    int.from_dict(p) if hasattr(int, "from_dict") else p
                    for p in d["itemIds"]
                ]
            if "currency" in d:
                v["currency"] = (
                    str.from_dict(d["currency"])
                    if hasattr(str, "from_dict")
                    else d["currency"]
                )
            if "exchangeRateToUSD" in d:
                v["exchangeRateToUSD"] = (
                    float.from_dict(d["exchangeRateToUSD"])
                    if hasattr(float, "from_dict")
                    else d["exchangeRateToUSD"]
                )
            return StoreDownloadResp._metrics(**v)

        def as_dict(self):
            d = {}
            if self.__itemIds is not None:
                d["itemIds"] = [
                    p.as_dict() if hasattr(p, "as_dict") else p for p in self.__itemIds
                ]
            if self.__currency is not None:
                d["currency"] = (
                    self.__currency.as_dict()
                    if hasattr(self.__currency, "as_dict")
                    else self.__currency
                )
            if self.__exchangeRateToUSD is not None:
                d["exchangeRateToUSD"] = (
                    self.__exchangeRateToUSD.as_dict()
                    if hasattr(self.__exchangeRateToUSD, "as_dict")
                    else self.__exchangeRateToUSD
                )
            return d

        def __repr__(self):
            return "<Class _metrics. itemIds: {}, currency: {}, exchangeRateToUSD: {}>".format(
                limitedRepr(
                    self.__itemIds[:20]
                    if isinstance(self.__itemIds, bytes)
                    else self.__itemIds
                ),
                limitedRepr(
                    self.__currency[:20]
                    if isinstance(self.__currency, bytes)
                    else self.__currency
                ),
                limitedRepr(
                    self.__exchangeRateToUSD[:20]
                    if isinstance(self.__exchangeRateToUSD, bytes)
                    else self.__exchangeRateToUSD
                ),
            )

    class _subscriptionStatus:
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
                return StoreDownloadResp._subscriptionStatus._account(**v)

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
                return StoreDownloadResp._subscriptionStatus._terms(**v)

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
                return StoreDownloadResp._subscriptionStatus._family(**v)

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
                isinstance(i, StoreDownloadResp._subscriptionStatus._terms)
                for i in value
            ):
                raise TypeError(
                    "terms list values must be StoreDownloadResp._subscriptionStatus._terms"
                )

            self.__terms = value

        terms = property(_get_terms, _set_terms)

        def _get_account(self):
            return self.__account

        def _set_account(self, value):
            if not isinstance(value, StoreDownloadResp._subscriptionStatus._account):
                raise TypeError(
                    "account must be StoreDownloadResp._subscriptionStatus._account"
                )

            self.__account = value

        account = property(_get_account, _set_account)

        def _get_family(self):
            return self.__family

        def _set_family(self, value):
            if not isinstance(value, StoreDownloadResp._subscriptionStatus._family):
                raise TypeError(
                    "family must be StoreDownloadResp._subscriptionStatus._family"
                )

            self.__family = value

        family = property(_get_family, _set_family)

        @staticmethod
        def from_dict(d):
            v = {}
            if "terms" in d:
                v["terms"] = [
                    StoreDownloadResp._subscriptionStatus._terms.from_dict(p)
                    if hasattr(
                        StoreDownloadResp._subscriptionStatus._terms, "from_dict"
                    )
                    else p
                    for p in d["terms"]
                ]
            if "account" in d:
                v["account"] = (
                    StoreDownloadResp._subscriptionStatus._account.from_dict(
                        d["account"]
                    )
                    if hasattr(
                        StoreDownloadResp._subscriptionStatus._account, "from_dict"
                    )
                    else d["account"]
                )
            if "family" in d:
                v["family"] = (
                    StoreDownloadResp._subscriptionStatus._family.from_dict(d["family"])
                    if hasattr(
                        StoreDownloadResp._subscriptionStatus._family, "from_dict"
                    )
                    else d["family"]
                )
            return StoreDownloadResp._subscriptionStatus(**v)

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

    _types_map = {
        "pings": {"type": list, "subtype": float},
        "cancel_purchase_batch": {"type": bool, "subtype": None},
        "customerMessage": {"type": str, "subtype": None},
        "failureType": {"type": str, "subtype": None},
        "jingleDocType": {"type": str, "subtype": None},
        "jingleAction": {"type": str, "subtype": None},
        "status": {"type": int, "subtype": None},
        "dsPersonId": {"type": str, "subtype": None},
        "creditDisplay": {"type": str, "subtype": None},
        "creditBalance": {"type": str, "subtype": None},
        "freeSongBalance": {"type": str, "subtype": None},
        "authorized": {"type": bool, "subtype": None},
        "download_queue_item_count": {"type": int, "subtype": None},
        "songList": {"type": list, "subtype": _songList},
        "metrics": {"type": _metrics, "subtype": None},
        "subscriptionStatus": {"type": _subscriptionStatus, "subtype": None},
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
        "jingleDocType": {
            "required": True,
        },
        "jingleAction": {
            "required": True,
        },
        "status": {
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
        "authorized": {
            "required": True,
        },
        "download_queue_item_count": {
            "required": True,
        },
        "songList": {
            "required": True,
        },
        "metrics": {
            "required": True,
        },
        "subscriptionStatus": {
            "required": True,
        },
    }

    def __init__(
        self,
        pings: List[float] = None,
        cancel_purchase_batch: bool = None,
        customerMessage: str = None,
        failureType: str = None,
        jingleDocType: str = None,
        jingleAction: str = None,
        status: int = None,
        dsPersonId: str = None,
        creditDisplay: str = None,
        creditBalance: str = None,
        freeSongBalance: str = None,
        authorized: bool = None,
        download_queue_item_count: int = None,
        songList: List[_songList] = None,
        metrics: _metrics = None,
        subscriptionStatus: _subscriptionStatus = None,
    ):
        pass
        self.__pings = pings
        self.__cancel_purchase_batch = cancel_purchase_batch
        self.__customerMessage = customerMessage
        self.__failureType = failureType
        self.__jingleDocType = jingleDocType
        self.__jingleAction = jingleAction
        self.__status = status
        self.__dsPersonId = dsPersonId
        self.__creditDisplay = creditDisplay
        self.__creditBalance = creditBalance
        self.__freeSongBalance = freeSongBalance
        self.__authorized = authorized
        self.__download_queue_item_count = download_queue_item_count
        self.__songList = songList
        self.__metrics = metrics
        self.__subscriptionStatus = subscriptionStatus

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

    def _get_jingleDocType(self):
        return self.__jingleDocType

    def _set_jingleDocType(self, value):
        if not isinstance(value, str):
            raise TypeError("jingleDocType must be str")

        self.__jingleDocType = value

    jingleDocType = property(_get_jingleDocType, _set_jingleDocType)

    def _get_jingleAction(self):
        return self.__jingleAction

    def _set_jingleAction(self, value):
        if not isinstance(value, str):
            raise TypeError("jingleAction must be str")

        self.__jingleAction = value

    jingleAction = property(_get_jingleAction, _set_jingleAction)

    def _get_status(self):
        return self.__status

    def _set_status(self, value):
        if not isinstance(value, int):
            raise TypeError("status must be int")

        self.__status = value

    status = property(_get_status, _set_status)

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

    def _get_authorized(self):
        return self.__authorized

    def _set_authorized(self, value):
        if not isinstance(value, bool):
            raise TypeError("authorized must be bool")

        self.__authorized = value

    authorized = property(_get_authorized, _set_authorized)

    def _get_download_queue_item_count(self):
        return self.__download_queue_item_count

    def _set_download_queue_item_count(self, value):
        if not isinstance(value, int):
            raise TypeError("download_queue_item_count must be int")

        self.__download_queue_item_count = value

    download_queue_item_count = property(
        _get_download_queue_item_count, _set_download_queue_item_count
    )

    def _get_songList(self):
        return self.__songList

    def _set_songList(self, value):
        if not isinstance(value, list):
            raise TypeError("songList must be list")
        if not all(isinstance(i, StoreDownloadResp._songList) for i in value):
            raise TypeError("songList list values must be StoreDownloadResp._songList")

        self.__songList = value

    songList = property(_get_songList, _set_songList)

    def _get_metrics(self):
        return self.__metrics

    def _set_metrics(self, value):
        if not isinstance(value, StoreDownloadResp._metrics):
            raise TypeError("metrics must be StoreDownloadResp._metrics")

        self.__metrics = value

    metrics = property(_get_metrics, _set_metrics)

    def _get_subscriptionStatus(self):
        return self.__subscriptionStatus

    def _set_subscriptionStatus(self, value):
        if not isinstance(value, StoreDownloadResp._subscriptionStatus):
            raise TypeError(
                "subscriptionStatus must be StoreDownloadResp._subscriptionStatus"
            )

        self.__subscriptionStatus = value

    subscriptionStatus = property(_get_subscriptionStatus, _set_subscriptionStatus)

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
        if "jingleDocType" in d:
            v["jingleDocType"] = (
                str.from_dict(d["jingleDocType"])
                if hasattr(str, "from_dict")
                else d["jingleDocType"]
            )
        if "jingleAction" in d:
            v["jingleAction"] = (
                str.from_dict(d["jingleAction"])
                if hasattr(str, "from_dict")
                else d["jingleAction"]
            )
        if "status" in d:
            v["status"] = (
                int.from_dict(d["status"]) if hasattr(int, "from_dict") else d["status"]
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
        if "authorized" in d:
            v["authorized"] = (
                bool.from_dict(d["authorized"])
                if hasattr(bool, "from_dict")
                else d["authorized"]
            )
        if "download-queue-item-count" in d:
            v["download_queue_item_count"] = (
                int.from_dict(d["download-queue-item-count"])
                if hasattr(int, "from_dict")
                else d["download-queue-item-count"]
            )
        if "songList" in d:
            v["songList"] = [
                StoreDownloadResp._songList.from_dict(p)
                if hasattr(StoreDownloadResp._songList, "from_dict")
                else p
                for p in d["songList"]
            ]
        if "metrics" in d:
            v["metrics"] = (
                StoreDownloadResp._metrics.from_dict(d["metrics"])
                if hasattr(StoreDownloadResp._metrics, "from_dict")
                else d["metrics"]
            )
        if "subscriptionStatus" in d:
            v["subscriptionStatus"] = (
                StoreDownloadResp._subscriptionStatus.from_dict(d["subscriptionStatus"])
                if hasattr(StoreDownloadResp._subscriptionStatus, "from_dict")
                else d["subscriptionStatus"]
            )
        return StoreDownloadResp(**v)

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
        if self.__jingleDocType is not None:
            d["jingleDocType"] = (
                self.__jingleDocType.as_dict()
                if hasattr(self.__jingleDocType, "as_dict")
                else self.__jingleDocType
            )
        if self.__jingleAction is not None:
            d["jingleAction"] = (
                self.__jingleAction.as_dict()
                if hasattr(self.__jingleAction, "as_dict")
                else self.__jingleAction
            )
        if self.__status is not None:
            d["status"] = (
                self.__status.as_dict()
                if hasattr(self.__status, "as_dict")
                else self.__status
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
        if self.__authorized is not None:
            d["authorized"] = (
                self.__authorized.as_dict()
                if hasattr(self.__authorized, "as_dict")
                else self.__authorized
            )
        if self.__download_queue_item_count is not None:
            d["download-queue-item-count"] = (
                self.__download_queue_item_count.as_dict()
                if hasattr(self.__download_queue_item_count, "as_dict")
                else self.__download_queue_item_count
            )
        if self.__songList is not None:
            d["songList"] = [
                p.as_dict() if hasattr(p, "as_dict") else p for p in self.__songList
            ]
        if self.__metrics is not None:
            d["metrics"] = (
                self.__metrics.as_dict()
                if hasattr(self.__metrics, "as_dict")
                else self.__metrics
            )
        if self.__subscriptionStatus is not None:
            d["subscriptionStatus"] = (
                self.__subscriptionStatus.as_dict()
                if hasattr(self.__subscriptionStatus, "as_dict")
                else self.__subscriptionStatus
            )
        return d

    def __repr__(self):
        return "<Class StoreDownloadResp. pings: {}, cancel_purchase_batch: {}, customerMessage: {}, failureType: {}, jingleDocType: {}, jingleAction: {}, status: {}, dsPersonId: {}, creditDisplay: {}, creditBalance: {}, freeSongBalance: {}, authorized: {}, download_queue_item_count: {}, songList: {}, metrics: {}, subscriptionStatus: {}>".format(
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
                self.__jingleDocType[:20]
                if isinstance(self.__jingleDocType, bytes)
                else self.__jingleDocType
            ),
            limitedRepr(
                self.__jingleAction[:20]
                if isinstance(self.__jingleAction, bytes)
                else self.__jingleAction
            ),
            limitedRepr(
                self.__status[:20]
                if isinstance(self.__status, bytes)
                else self.__status
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
                self.__authorized[:20]
                if isinstance(self.__authorized, bytes)
                else self.__authorized
            ),
            limitedRepr(
                self.__download_queue_item_count[:20]
                if isinstance(self.__download_queue_item_count, bytes)
                else self.__download_queue_item_count
            ),
            limitedRepr(
                self.__songList[:20]
                if isinstance(self.__songList, bytes)
                else self.__songList
            ),
            limitedRepr(
                self.__metrics[:20]
                if isinstance(self.__metrics, bytes)
                else self.__metrics
            ),
            limitedRepr(
                self.__subscriptionStatus[:20]
                if isinstance(self.__subscriptionStatus, bytes)
                else self.__subscriptionStatus
            ),
        )
