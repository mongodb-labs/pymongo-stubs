from typing import Any, Mapping, Tuple, Type, TypeVar
from uuid import UUID

BINARY_SUBTYPE: int
FUNCTION_SUBTYPE: int
OLD_BINARY_SUBTYPE: int
OLD_UUID_SUBTYPE: int
UUID_SUBTYPE: int

class UuidRepresentation:
    UNSPECIFIED: int = ...
    STANDARD: int = ...
    PYTHON_LEGACY: int = ...
    JAVA_LEGACY: int = ...
    CSHARP_LEGACY: int = ...

STANDARD: int
PYTHON_LEGACY: int
JAVA_LEGACY: int
CSHARP_LEGACY: int
ALL_UUID_SUBTYPES: Tuple[int, int]
ALL_UUID_REPRESENTATIONS: Tuple[int, int, int, int, int]
UUID_REPRESENTATION_NAMES: Mapping[int, str]
MD5_SUBTYPE: int
USER_DEFINED_SUBTYPE: int

_Binary = TypeVar("_Binary", bound="Binary")

class Binary(bytes):
    def __new__(cls, data: bytes, subtype: int = ...) -> Binary: ...
    @classmethod
    def from_uuid(cls: Type[_Binary], uuid: UUID, uuid_representation: int = ...) -> _Binary: ...
    def as_uuid(self, uuid_representation: int = ...) -> UUID: ...
    @property
    def subtype(self) -> int: ...
    def __getnewargs__(self): ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> Any: ...
    def __ne__(self, other: Any) -> bool: ...

class UUIDLegacy(Binary):
    def __new__(cls, obj: UUID) -> UUIDLegacy: ...
    def __getnewargs__(self): ...
    @property
    def uuid(self) -> UUID: ...
