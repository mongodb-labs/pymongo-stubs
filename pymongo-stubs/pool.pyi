from socket import socket
from ssl import SSLContext
from typing import Any, Dict, Iterator, Mapping, Optional, Tuple, Union

from pymongo.auth import MongoCredential
from pymongo.client_session import ClientSession
from pymongo.compression_support import CompressionSettings
from pymongo.driver_info import DriverInfo
from pymongo.errors import PyMongoError
from pymongo.ismaster import IsMaster
from pymongo.monitoring import _EventListeners

def is_ip_address(address: Any): ...

class PoolOptions:
    def __init__(
        self,
        max_pool_size: int = ...,
        min_pool_size: int = ...,
        max_idle_time_seconds: Optional[int] = ...,
        connect_timeout: Optional[int] = ...,
        socket_timeout: Optional[int] = ...,
        wait_queue_timeout: Optional[int] = ...,
        wait_queue_multiple: Optional[int] = ...,
        ssl_context: Union[SSLContext, None] = ...,
        ssl_match_hostname: bool = ...,
        socket_keepalive: bool = ...,
        event_listeners: Optional[_EventListeners] = ...,
        appname: Optional[str] = ...,
        driver: Optional[DriverInfo] = ...,
        compression_settings: Optional[CompressionSettings] = ...,
    ) -> None: ...
    @property
    def non_default_options(self): ...
    @property
    def max_pool_size(self) -> int: ...
    @property
    def min_pool_size(self) -> int: ...
    @property
    def max_idle_time_seconds(self): ...
    @property
    def connect_timeout(self) -> int: ...
    @property
    def socket_timeout(self) -> int: ...
    @property
    def wait_queue_timeout(self) -> int: ...
    @property
    def wait_queue_multiple(self) -> int: ...
    @property
    def ssl_context(self) -> SSLContext: ...
    @property
    def ssl_match_hostname(self) -> bool: ...
    @property
    def socket_keepalive(self) -> bool: ...
    @property
    def event_listeners(self) -> _EventListeners: ...
    @property
    def appname(self) -> str: ...
    @property
    def driver(self) -> DriverInfo: ...
    @property
    def compression_settings(self) -> CompressionSettings: ...
    @property
    def metadata(self) -> Dict[str, Any]: ...

class _CancellationContext:
    def __init__(self) -> None: ...
    def cancel(self) -> None: ...
    @property
    def cancelled(self): ...

class SocketInfo:
    sock: Any = ...
    address: Any = ...
    id: Any = ...
    authset: Any = ...
    closed: bool = ...
    last_checkin_time: Any = ...
    performed_handshake: bool = ...
    is_writable: bool = ...
    max_wire_version: Any = ...
    max_bson_size: Any = ...
    max_message_size: Any = ...
    max_write_batch_size: Any = ...
    supports_sessions: bool = ...
    is_mongos: bool = ...
    op_msg_enabled: bool = ...
    listeners: Any = ...
    enabled_for_cmap: Any = ...
    compression_settings: Any = ...
    compression_context: Any = ...
    socket_checker: Any = ...
    negotiated_mechanisms: Any = ...
    auth_ctx: Any = ...
    generation: Any = ...
    ready: bool = ...
    cancel_context: Any = ...
    opts: Any = ...
    more_to_come: bool = ...
    def __init__(self, sock: socket, pool: Pool, address: IsMaster, id: Tuple[str, int]) -> None: ...
    def ismaster(self, all_credentials: Optional[Any] = ...): ...
    def command(
        self,
        dbname: Any,
        spec: Any,
        slave_ok: bool = ...,
        read_preference: Any = ...,
        codec_options: Any = ...,
        check: bool = ...,
        allowable_errors: Optional[Any] = ...,
        check_keys: bool = ...,
        read_concern: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        parse_write_concern_error: bool = ...,
        collation: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
        client: Optional[Any] = ...,
        retryable_write: bool = ...,
        publish_events: bool = ...,
        user_fields: Optional[Any] = ...,
        exhaust_allowed: bool = ...,
    ): ...
    def send_message(self, message: bytes, max_doc_size: int) -> None: ...
    def receive_message(self, request_id: Any): ...
    def legacy_write(self, request_id: int, msg: bytes, max_doc_size: int, with_last_error: bool) -> Dict[str, Any]: ...
    def write_command(self, request_id: int, msg: bytes) -> Dict[str, Any]: ...
    def check_auth(self, all_credentials: Mapping[str, MongoCredential]) -> None: ...
    def authenticate(self, credentials: MongoCredential) -> None: ...
    def validate_session(self, client: Any, session: Any) -> None: ...
    def close_socket(self, reason: Any) -> None: ...
    def socket_closed(self): ...
    def send_cluster_time(self, command: Any, session: Optional[ClientSession], client: Any) -> None: ...
    def update_last_checkin_time(self) -> None: ...
    def update_is_writable(self, is_writable: Any) -> None: ...
    def idle_time_seconds(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class _PoolClosedError(PyMongoError): ...

class Pool:
    sockets: Any = ...
    lock: Any = ...
    active_sockets: int = ...
    next_connection_id: int = ...
    closed: bool = ...
    is_writable: Any = ...
    generation: int = ...
    pid: Any = ...
    address: Any = ...
    opts: Any = ...
    handshake: Any = ...
    enabled_for_cmap: Any = ...
    def __init__(self, address: Tuple[str, int], options: PoolOptions, handshake: bool = ...) -> None: ...
    def update_is_writable(self, is_writable: Any) -> None: ...
    def reset(self) -> None: ...
    def close(self) -> None: ...
    def remove_stale_sockets(self, reference_generation: Any, all_credentials: Any) -> None: ...
    def connect(self, all_credentials: Optional[Any] = ...): ...
    def get_socket(self, all_credentials: Mapping[str, MongoCredential], checkout: bool = ...) -> Iterator[SocketInfo]: ...
    def return_socket(self, sock_info: SocketInfo) -> None: ...
    def __del__(self) -> None: ...
