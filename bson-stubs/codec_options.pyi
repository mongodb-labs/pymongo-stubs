import abc
import datetime
from collections import namedtuple
from typing import Any, Callable, Iterable, NamedTuple, Optional, Union

class TypeEncoder(abc.ABC, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def python_type(self) -> Any: ...
    @abc.abstractmethod
    def transform_python(self, value: Any) -> Any: ...

class TypeDecoder(abc.ABC, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def bson_type(self) -> Any: ...
    @abc.abstractmethod
    def transform_bson(self, value: Any) -> Any: ...

class TypeCodec(TypeEncoder, TypeDecoder, metaclass=abc.ABCMeta): ...

Codec = Union[TypeEncoder, TypeDecoder, TypeCodec]
Fallback = Callable[[Any], Any]

class TypeRegistry:
    def __init__(self, type_codecs: Optional[Iterable[Codec]] = ..., fallback_encoder: Optional[Fallback] = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...

_options_base = namedtuple(
    "_options_base",
    ["document_class", "tz_aware", "uuid_representation", "unicode_decode_error_handler", "tzinfo", "type_registry"],
)

class CodecOptions(_options_base):
    def __new__(
        cls: Any,
        document_class: Optional[type] = ...,
        tz_aware: Optional[bool] = ...,
        uuid_representation: Optional[int] = ...,
        unicode_decode_error_handler: Optional[str] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
        type_registry: Optional[TypeRegistry] = ...,
    ) -> CodecOptions: ...
    def with_options(self, **kwargs: Any) -> CodecOptions: ...

DEFAULT_CODEC_OPTIONS: Any
