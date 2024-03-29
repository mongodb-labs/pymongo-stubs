from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Union

from bson.code import Code
from bson.codec_options import CodecOptions
from bson.dbref import DBRef
from pymongo import MongoClient, common
from pymongo.change_stream import ChangeStream
from pymongo.client_session import ClientSession
from pymongo.collation import Collation
from pymongo.collection import Collection
from pymongo.command_cursor import CommandCursor
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.son_manipulator import SONManipulator
from pymongo.write_concern import WriteConcern

_Pipeline = List[Mapping[str, Any]]
_Collation = Union[Mapping[str, Any], Collation]
_Code = Union[str, Code]
_DocumentOut = Any

class Database(common.BaseObject):
    def __init__(
        self,
        client: MongoClient,
        name: str,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[_ServerMode] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
    ) -> None: ...
    def add_son_manipulator(self, manipulator: SONManipulator) -> None: ...
    @property
    def system_js(self) -> SystemJS: ...
    @property
    def client(self) -> MongoClient: ...
    @property
    def name(self) -> str: ...
    @property
    def incoming_manipulators(self) -> List[str]: ...
    @property
    def incoming_copying_manipulators(self) -> List[str]: ...
    @property
    def outgoing_manipulators(self) -> List[str]: ...
    @property
    def outgoing_copying_manipulators(self) -> List[str]: ...
    def with_options(
        self,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[_ServerMode] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
    ): ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __getattr__(self, name: str) -> Collection: ...
    def __getitem__(self, name: str) -> Collection: ...
    def get_collection(
        self,
        name: str,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[_ServerMode] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
    ) -> Collection: ...
    def create_collection(
        self,
        name: str,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[_ServerMode] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> Collection: ...
    def aggregate(self, pipeline: _Pipeline, session: Optional[ClientSession] = ..., **kwargs: Any) -> CommandCursor: ...
    def watch(
        self,
        pipeline: Optional[_Pipeline] = ...,
        full_document: Optional[bool] = ...,
        resume_after: Optional[Mapping[str, Any]] = ...,
        max_await_time_ms: Optional[int] = ...,
        batch_size: Optional[int] = ...,
        collation: Optional[_Collation] = ...,
        start_at_operation_time: Optional[Mapping[str, Any]] = ...,
        session: Optional[ClientSession] = ...,
        start_after: Optional[Mapping[str, Any]] = ...,
    ) -> ChangeStream: ...
    def command(
        self,
        command: Union[str, Mapping[str, Any]],
        value: Any = ...,
        check: bool = ...,
        allowable_errors: Optional[Sequence[Union[str, int]]] = ...,
        read_preference: Optional[_ServerMode] = ...,
        codec_options: Optional[CodecOptions] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> _DocumentOut: ...
    def list_collections(
        self, session: Optional[ClientSession] = ..., filter: Optional[Mapping[str, Any]] = ..., **kwargs: Any
    ) -> CommandCursor: ...
    def list_collection_names(
        self, session: Optional[ClientSession] = ..., filter: Optional[Mapping[str, Any]] = ..., **kwargs: Any
    ) -> List[str]: ...
    def collection_names(self, include_system_collections: bool = ..., session: Optional[ClientSession] = ...) -> List[str]: ...
    def drop_collection(
        self, name_or_collection: Union[str, Collection], session: Optional[ClientSession] = ...
    ) -> Dict[str, Any]: ...
    def validate_collection(
        self,
        name_or_collection: Union[str, Collection],
        scandata: bool = ...,
        full: bool = ...,
        session: Optional[ClientSession] = ...,
        background: Optional[bool] = ...,
    ) -> Dict[str, Any]: ...
    def current_op(self, include_all: bool = ..., session: Optional[ClientSession] = ...) -> _DocumentOut: ...
    def profiling_level(self, session: Optional[ClientSession] = ...) -> int: ...
    def set_profiling_level(
        self,
        level: int,
        slow_ms: Optional[int] = ...,
        session: Optional[ClientSession] = ...,
        sample_rate: Optional[int] = ...,
        filter: Optional[bool] = ...,
    ) -> None: ...
    def profiling_info(self, session: Optional[ClientSession] = ...) -> List[Mapping[str, Any]]: ...
    def error(self) -> Optional[Mapping[str, Any]]: ...
    def last_status(self) -> Dict[str, Any]: ...
    def previous_error(self) -> Optional[Dict[str, Any]]: ...
    def reset_error_history(self) -> None: ...
    def add_user(
        self,
        name: str,
        password: Optional[str] = ...,
        read_only: Optional[bool] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> None: ...
    def remove_user(self, name: str, session: Optional[ClientSession] = ...) -> None: ...
    def authenticate(
        self,
        name: Optional[str] = ...,
        password: Optional[str] = ...,
        source: Optional[str] = ...,
        mechanism: str = ...,
        **kwargs: Any,
    ) -> bool: ...
    def logout(self) -> None: ...
    def dereference(self, dbref: DBRef, session: Optional[ClientSession] = ..., **kwargs: Any) -> _DocumentOut: ...
    def eval(self, code: _Code, *args: Any) -> Any: ...

class SystemJS:
    def __init__(self, database: Database) -> None: ...
    def __setattr__(self, name: str, code: _Code) -> None: ...
    def __setitem__(self, name: str, code: _Code) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def __getattr__(self, name: str) -> Callable[..., Any]: ...
    def __getitem__(self, name: str) -> Callable[..., Any]: ...
    def list(self) -> List[str]: ...
