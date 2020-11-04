from typing import Any, Dict, List, MutableMapping, Optional, Tuple, TypeVar, Union

SCHEME: str
SCHEME_LEN: int
SRV_SCHEME: str
SRV_SCHEME_LEN: int
DEFAULT_PORT: int

def parse_userinfo(userinfo: str) -> Tuple[str, str]: ...
def parse_ipv6_literal_host(entity: str, default_port: Optional[int]) -> Tuple[str, Optional[Union[str, int]]]: ...
def parse_host(entity: str, default_port: Optional[int] = ...) -> Tuple[str, Optional[int]]: ...

_T = TypeVar("_T", bound=MutableMapping)

def validate_options(opts: _T, warn: bool = ...) -> _T: ...
def split_options(opts: str, validate: bool = ..., warn: bool = ..., normalize: bool = ...) -> MutableMapping[str, Any]: ...
def split_hosts(hosts: str, default_port: Optional[int] = ...) -> List[Tuple[str, Optional[int]]]: ...
def parse_uri(
    uri: str,
    default_port: Optional[int] = ...,
    validate: bool = ...,
    warn: bool = ...,
    normalize: bool = ...,
    connect_timeout: Optional[float] = ...,
) -> Dict[str, Any]: ...
