import decimal
from typing import Any, Union

def create_decimal128_context() -> decimal.Context: ...

class Decimal128:
    def __init__(self, value: Union[str, decimal.Decimal]) -> None: ...
    def to_decimal(self) -> decimal.Decimal: ...
    @classmethod
    def from_bid(cls: Any, value: bytes) -> Decimal128: ...
    @property
    def bid(self) -> bytes: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
