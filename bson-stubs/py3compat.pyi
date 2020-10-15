from collections import abc as abc
from io import BytesIO as StringIO
from typing import Any, Callable, Iterable, Iterator, Mapping, Optional, Tuple, TypeVar

PY3: bool

def abstractproperty(func: Any) -> Any: ...

MAXSIZE: int
_T = TypeVar("_T")
_S = TypeVar("_S")
imap: Callable[[Callable[[_T], _S], Iterable[_T]], Iterator[_S]]

def b(s: Any) -> bytes: ...
def bytes_from_hex(h: Any) -> bytes: ...

_K = TypeVar("_K")
_V = TypeVar("_V")

def iteritems(d: Mapping[_K, _V]) -> Iterable[Tuple[_K, _V]]: ...
def itervalues(d: Mapping[_K, _V]) -> Iterable[_V]: ...
def reraise(exctype: Any, value: Any, trace: Optional[Any] = ...) -> None: ...
def reraise_instance(exc_instance: Any, trace: Optional[Any] = ...) -> None: ...
def _unicode(s: str) -> str: ...

text_type = str
string_type = str
integer_types = int
