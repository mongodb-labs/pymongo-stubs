from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

from bson.code import Code
from bson.codec_options import CodecOptions
from pymongo import common
from pymongo.bulk import BulkOperationBuilder
from pymongo.change_stream import ChangeStream
from pymongo.client_session import ClientSession
from pymongo.collation import Collation
from pymongo.command_cursor import CommandCursor
from pymongo.cursor import Cursor, RawBatchCursor
from pymongo.database import Database
from pymongo.operations import DeleteMany, DeleteOne, IndexModel, InsertOne, ReplaceOne, UpdateMany, UpdateOne
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.results import BulkWriteResult, DeleteResult, InsertManyResult, InsertOneResult, UpdateResult
from pymongo.write_concern import WriteConcern

WriteOp = Union[InsertOne, DeleteOne, DeleteMany, ReplaceOne, UpdateOne, UpdateMany]
_Collation = Union[Mapping[str, Any], Collation]
# Hint supports index name, "myIndex", or list of index pairs: [('x', 1), ('y', -1)]
_IndexList = Sequence[Tuple[str, Union[int, str, Mapping[str, Any]]]]
_IndexKeyHint = Union[str, _IndexList]
_Pipeline = List[Mapping[str, Any]]
_Code = Union[str, Code]
_DocumentIn = Mapping[str, Any]
_DocumentOut = Any

class ReturnDocument:
    BEFORE: bool = ...
    AFTER: bool = ...

class Collection(common.BaseObject):
    def __init__(
        self,
        database: Database,
        name: str,
        create: Optional[bool] = ...,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[_ServerMode] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> None: ...
    def __getattr__(self, name: str) -> Collection: ...
    def __getitem__(self, name: str) -> Collection: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    @property
    def full_name(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def database(self) -> Database: ...
    def with_options(
        self,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[_ServerMode] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
    ) -> Collection: ...
    def initialize_unordered_bulk_op(self, bypass_document_validation: bool = ...) -> BulkOperationBuilder: ...
    def initialize_ordered_bulk_op(self, bypass_document_validation: bool = ...) -> BulkOperationBuilder: ...
    def bulk_write(
        self,
        requests: List[WriteOp],
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[ClientSession] = ...,
    ) -> BulkWriteResult: ...
    def insert_one(
        self, document: _DocumentIn, bypass_document_validation: bool = ..., session: Optional[ClientSession] = ...
    ) -> InsertOneResult: ...
    def insert_many(
        self,
        documents: Iterable[_DocumentIn],
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[ClientSession] = ...,
    ) -> InsertManyResult: ...
    def replace_one(
        self,
        filter: Mapping[str, Any],
        replacement: Mapping[str, Any],
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[_Collation] = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
    ) -> UpdateResult: ...
    def update_one(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[_Collation] = ...,
        array_filters: Optional[List[Mapping[str, Any]]] = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
    ) -> UpdateResult: ...
    def update_many(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        upsert: bool = ...,
        array_filters: Optional[List[Mapping[str, Any]]] = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[_Collation] = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
    ) -> UpdateResult: ...
    def drop(self, session: Optional[ClientSession] = ...) -> None: ...
    def delete_one(
        self,
        filter: Mapping[str, Any],
        collation: Optional[_Collation] = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
    ) -> DeleteResult: ...
    def delete_many(
        self,
        filter: Mapping[str, Any],
        collation: Optional[_Collation] = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
    ) -> DeleteResult: ...
    def find_one(self, filter: Optional[Any] = ..., *args: Any, **kwargs: Any) -> Optional[_DocumentOut]: ...
    def find(self, *args: Any, **kwargs: Any) -> Cursor: ...
    def find_raw_batches(self, *args: Any, **kwargs: Any) -> RawBatchCursor: ...
    def parallel_scan(self, num_cursors: int, session: Optional[ClientSession] = ..., **kwargs: Any) -> List[CommandCursor]: ...
    def estimated_document_count(self, **kwargs: Any) -> int: ...
    def count_documents(self, filter: Mapping[str, Any], session: Optional[ClientSession] = ..., **kwargs: Any) -> int: ...
    def count(self, filter: Optional[Mapping[str, Any]] = ..., session: Optional[ClientSession] = ..., **kwargs: Any) -> int: ...
    def create_indexes(self, indexes: List[IndexModel], session: Optional[ClientSession] = ..., **kwargs: Any) -> List[str]: ...
    def create_index(self, keys: _IndexKeyHint, session: Optional[ClientSession] = ..., **kwargs: Any) -> str: ...
    def ensure_index(self, key_or_list: _IndexKeyHint, cache_for: int = ..., **kwargs: Any) -> Optional[str]: ...
    def drop_indexes(self, session: Optional[ClientSession] = ..., **kwargs: Any) -> None: ...
    def drop_index(self, index_or_name: _IndexKeyHint, session: Optional[ClientSession] = ..., **kwargs: Any) -> None: ...
    def reindex(self, session: Optional[ClientSession] = ..., **kwargs: Any): ...
    def list_indexes(self, session: Optional[ClientSession] = ...) -> CommandCursor: ...
    def index_information(self, session: Optional[ClientSession] = ...) -> Dict[str, Any]: ...
    def options(self, session: Optional[ClientSession] = ...) -> Dict[str, Any]: ...
    def aggregate(self, pipeline: _Pipeline, session: Optional[ClientSession] = ..., **kwargs: Any) -> CommandCursor: ...
    def aggregate_raw_batches(self, pipeline: _Pipeline, **kwargs: Any) -> RawBatchCursor: ...
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
    def group(
        self,
        key: Optional[Union[str, Mapping[str, Any], Iterable[str]]],
        condition: Optional[Mapping[str, Any]],
        initial: Mapping[str, Any],
        reduce: _Code,
        finalize: Optional[_Code] = ...,
        **kwargs: Any,
    ) -> List[_DocumentOut]: ...
    def rename(self, new_name: str, session: Optional[ClientSession] = ..., **kwargs: Any) -> Dict[str, Any]: ...
    def distinct(
        self, key: str, filter: Optional[Mapping[str, Any]] = ..., session: Optional[ClientSession] = ..., **kwargs: Any
    ) -> List[Any]: ...
    def map_reduce(
        self,
        map: _Code,
        reduce: _Code,
        out: Union[str, Mapping[str, Any]],
        full_response: bool = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> Union[Collection, _DocumentOut]: ...
    def inline_map_reduce(
        self,
        map: _Code,
        reduce: _Code,
        full_response: bool = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> _DocumentOut: ...
    def find_one_and_delete(
        self,
        filter: Mapping[str, Any],
        projection: Optional[Union[Mapping[str, Any], Iterable[str]]] = ...,
        sort: Optional[_IndexList] = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> _DocumentOut: ...
    def find_one_and_replace(
        self,
        filter: Mapping[str, Any],
        replacement: Mapping[str, Any],
        projection: Optional[Union[Mapping[str, Any], Iterable[str]]] = ...,
        sort: Optional[_IndexList] = ...,
        upsert: bool = ...,
        return_document: bool = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> _DocumentOut: ...
    def find_one_and_update(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        projection: Optional[Union[Mapping[str, Any], Iterable[str]]] = ...,
        sort: Optional[_IndexList] = ...,
        upsert: bool = ...,
        return_document: bool = ...,
        array_filters: Optional[List[Mapping[str, Any]]] = ...,
        hint: Optional[_IndexKeyHint] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> _DocumentOut: ...
    def save(self, to_save: Mapping[str, Any], manipulate: bool = ..., check_keys: bool = ..., **kwargs: Any) -> Any: ...
    def insert(
        self,
        doc_or_docs: Union[Mapping[str, Any], List[Mapping[str, Any]]],
        manipulate: bool = ...,
        check_keys: bool = ...,
        continue_on_error: bool = ...,
        **kwargs: Any,
    ) -> Any: ...
    def update(
        self,
        spec: Mapping[str, Any],
        document: Mapping[str, Any],
        upsert: bool = ...,
        manipulate: bool = ...,
        multi: bool = ...,
        check_keys: bool = ...,
        **kwargs: Any,
    ) -> Optional[Dict[str, Any]]: ...
    def remove(self, spec_or_id: Any = ..., multi: bool = ..., **kwargs: Any) -> Optional[Dict[str, Any]]: ...
    def find_and_modify(
        self,
        query: Mapping[str, Any] = ...,
        update: Optional[Union[Mapping[str, Any], _Pipeline]] = ...,
        upsert: Optional[bool] = ...,
        sort: Optional[Union[_IndexList, Mapping[str, Any]]] = ...,
        full_response: Optional[bool] = ...,
        manipulate: Optional[bool] = ...,
        **kwargs: Any,
    ) -> Optional[_DocumentOut]: ...
