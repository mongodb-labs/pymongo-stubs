from queue import Queue
from typing import Any, Callable, List, Optional, Sequence, Set, Tuple

from pymongo.server import Server
from pymongo.settings import TopologySettings
from pymongo.topology_description import TopologyDescription

def process_events_queue(queue_ref: Queue[Tuple[Callable[..., Any], Sequence[Any]]]) -> bool: ...

class Topology:
    def __init__(self, topology_settings: TopologySettings): ...
    def open(self) -> None: ...
    def select_servers(
        self,
        selector: Callable[[Sequence[Server]], Sequence[Server]],
        server_selection_timeout: Optional[int] = ...,
        address: Optional[Tuple[str, int]] = ...,
    ) -> List[Server]: ...
    def select_server(
        self,
        selector: Callable[[Sequence[Server]], Sequence[Server]],
        server_selection_timeout: Optional[int] = ...,
        address: Optional[Tuple[str, int]] = ...,
    ) -> Server: ...
    def select_server_by_address(self, address: Tuple[str, int], server_selection_timeout: Optional[int] = ...) -> Server: ...
    def on_change(self, server_description: Any, reset_pool: bool = ...) -> None: ...
    def on_srv_update(self, seedlist: Any) -> None: ...
    def get_server_by_address(self, address: Tuple[str, int]) -> Optional[Server]: ...
    def has_server(self, address: Tuple[str, int]) -> bool: ...
    def get_primary(self) -> Optional[Tuple[str, int]]: ...
    def get_secondaries(self) -> Set[Tuple[str, int]]: ...
    def get_arbiters(self) -> Set[Tuple[str, int]]: ...
    def max_cluster_time(self): ...
    def receive_cluster_time(self, cluster_time: Any) -> None: ...
    def request_check_all(self, wait_time: int = ...) -> None: ...
    def handle_getlasterror(self, address: Any, error_msg: Any) -> None: ...
    def update_pool(self, all_credentials: Any) -> None: ...
    def close(self) -> None: ...
    @property
    def description(self) -> TopologyDescription: ...
    def pop_all_sessions(self): ...
    def get_server_session(self): ...
    def return_server_session(self, server_session: Any, lock: Any) -> None: ...
    def handle_error(self, address: Any, err_ctx: Any) -> None: ...

class _ErrorContext:
    error: Any = ...
    max_wire_version: Any = ...
    sock_generation: Any = ...
    completed_handshake: Any = ...
    def __init__(self, error: Any, max_wire_version: Any, sock_generation: Any, completed_handshake: Any) -> None: ...