from typing import Any, Optional

from pymongo.errors import NetworkTimeout as NetworkTimeout

def command(
    sock_info: Any,
    dbname: Any,
    spec: Any,
    slave_ok: Any,
    is_mongos: Any,
    read_preference: Any,
    codec_options: Any,
    session: Any,
    client: Any,
    check: bool = ...,
    allowable_errors: Optional[Any] = ...,
    address: Optional[Any] = ...,
    check_keys: bool = ...,
    listeners: Optional[Any] = ...,
    max_bson_size: Optional[Any] = ...,
    read_concern: Optional[Any] = ...,
    parse_write_concern_error: bool = ...,
    collation: Optional[Any] = ...,
    compression_ctx: Optional[Any] = ...,
    use_op_msg: bool = ...,
    unacknowledged: bool = ...,
    user_fields: Optional[Any] = ...,
    exhaust_allowed: bool = ...,
): ...
def receive_message(sock_info: Any, request_id: Any, max_message_size: Any = ...): ...
def wait_for_read(sock_info: Any, deadline: Any) -> None: ...
