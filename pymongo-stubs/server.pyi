from queue import Queue
from typing import Any, Callable, Iterator, Mapping, Optional, Sequence, Tuple
from weakref import ref

from bson.objectid import ObjectId
from pymongo.auth import MongoCredential
from pymongo.monitor import Monitor
from pymongo.monitoring import _EventListeners
from pymongo.pool import Pool, SocketInfo
from pymongo.server_description import ServerDescription
from pymongo.server_type import SERVER_TYPE as SERVER_TYPE

class Server:
    def __init__(
        self,
        server_description: ServerDescription,
        pool: Pool,
        monitor: Monitor,
        topology_id: Optional[ObjectId] = ...,
        listeners: Optional[_EventListeners] = ...,
        events: Optional[ref[Queue[Tuple[Callable[..., Any], Sequence[Any]]]]] = ...,
    ) -> None: ...
    def open(self) -> None: ...
    def reset(self) -> None: ...
    def close(self) -> None: ...
    def request_check(self) -> None: ...
    def run_operation_with_response(
        self, sock_info: Any, operation: Any, set_slave_okay: Any, listeners: Any, exhaust: Any, unpack_res: Any
    ): ...
    def get_socket(self, all_credentials: Mapping[str, MongoCredential], checkout: bool = ...) -> Iterator[SocketInfo]: ...
    @property
    def description(self) -> ServerDescription: ...
    @description.setter
    def description(self, server_description: Any) -> None: ...
    @property
    def pool(self) -> Pool: ...
