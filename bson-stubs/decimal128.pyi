import decimal
from typing import Any, List, Tuple, Type, TypeVar, Union

def create_decimal128_context() -> decimal.Context: ...

_Decimal128 = TypeVar("_Decimal128", bound="Decimal128")

class Decimal128:
    # TODO: typing.overload instead of Union?
    def __init__(self, value: Union[str, decimal.Decimal, Tuple[int, int], List[int]]) -> None: ...
    def to_decimal(self) -> decimal.Decimal: ...
    @classmethod
    def from_bid(cls: Type[_Decimal128], value: bytes) -> _Decimal128: ...
    @property
    def bid(self) -> bytes: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
