from typing import Any, Dict, Optional, Union

class WriteConcern(object):
    def __init__(self, w: Optional[Union[int, str]] = ..., wtimeout: Optional[int] = ..., j: Optional[bool] = ..., fsync: Optional[bool] = ...) -> None: ...
    @property
    def document(self) -> Dict[str, Any]: ...
    @property
    def acknowledged(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...
