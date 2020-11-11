import datetime
from typing import Any, BinaryIO, Iterator, List, Mapping, Type, TypeVar

from bson.binary import (
    ALL_UUID_SUBTYPES as ALL_UUID_SUBTYPES,
    CSHARP_LEGACY as CSHARP_LEGACY,
    JAVA_LEGACY as JAVA_LEGACY,
    OLD_UUID_SUBTYPE as OLD_UUID_SUBTYPE,
    UUID_SUBTYPE as UUID_SUBTYPE,
    Binary as Binary,
    UUIDLegacy as UUIDLegacy,
    UuidRepresentation as UuidRepresentation,
)
from bson.code import Code as Code
from bson.codec_options import DEFAULT_CODEC_OPTIONS as DEFAULT_CODEC_OPTIONS, CodecOptions as CodecOptions
from bson.dbref import DBRef as DBRef
from bson.decimal128 import Decimal128 as Decimal128
from bson.errors import InvalidBSON as InvalidBSON, InvalidDocument as InvalidDocument, InvalidStringData as InvalidStringData
from bson.int64 import Int64 as Int64
from bson.max_key import MaxKey as MaxKey
from bson.min_key import MinKey as MinKey
from bson.objectid import ObjectId as ObjectId
from bson.regex import Regex as Regex
from bson.son import RE_TYPE as RE_TYPE, SON as SON
from bson.timestamp import Timestamp as Timestamp
from bson.tz_util import utc as utc

EPOCH_AWARE: datetime.datetime
EPOCH_NAIVE: datetime.datetime
BSONNUM: bytes
BSONSTR: bytes
BSONOBJ: bytes
BSONARR: bytes
BSONBIN: bytes
BSONUND: bytes
BSONOID: bytes
BSONBOO: bytes
BSONDAT: bytes
BSONNUL: bytes
BSONRGX: bytes
BSONREF: bytes
BSONCOD: bytes
BSONSYM: bytes
BSONCWS: bytes
BSONINT: bytes
BSONTIM: bytes
BSONLON: bytes
BSONDEC: bytes
BSONMIN: bytes
BSONMAX: bytes

_DocumentIn = Mapping[str, Any]
_DocumentOut = Any

def get_data_and_view(data: Any): ...
def gen_list_name() -> Iterator[bytes]: ...
def encode(document: _DocumentIn, check_keys: bool = ..., codec_options: CodecOptions = ...) -> bytes: ...
def decode(data: bytes, codec_options: CodecOptions = ...) -> _DocumentOut: ...
def decode_all(data: bytes, codec_options: CodecOptions = ...) -> List[_DocumentOut]: ...
def decode_iter(data: bytes, codec_options: CodecOptions = ...) -> Iterator[_DocumentOut]: ...
def decode_file_iter(file_obj: BinaryIO, codec_options: CodecOptions = ...) -> Iterator[_DocumentOut]: ...
def is_valid(bson: bytes) -> bool: ...

_BSON = TypeVar("_BSON", bound="BSON")

class BSON(bytes):
    @classmethod
    def encode(cls: Type[_BSON], document: _DocumentIn, check_keys: bool = ..., codec_options: CodecOptions = ...) -> _BSON: ...
    # TODO: error: Signature of "update" incompatible with supertype "bytes"
    def decode(self, codec_options: CodecOptions = ...) -> _DocumentOut: ...  # type: ignore[override]

def has_c() -> bool: ...
