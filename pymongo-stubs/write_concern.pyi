from typing import Any, Dict, Optional, Union

class WriteConcern:
    def __init__(
        self,
        w: Optional[Union[int, str]] = ...,
        wtimeout: Optional[int] = ...,
        j: Optional[bool] = ...,
        fsync: Optional[bool] = ...,
    ) -> None: ...
    @property
    def is_server_default(self) -> bool: ...
    @property
    def document(self) -> Dict[str, Any]: ...
    @property
    def acknowledged(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

DEFAULT_WRITE_CONCERN: WriteConcern
