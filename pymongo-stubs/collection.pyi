from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

from bson.codec_options import CodecOptions
from pymongo import common
from pymongo.bulk import BulkOperationBuilder
from pymongo.client_session import ClientSession
from pymongo.command_cursor import CommandCursor
from pymongo.cursor import Cursor, RawBatchCursor
from pymongo.database import Database
from pymongo.operations import DeleteMany, DeleteOne, IndexModel, InsertOne, ReplaceOne, UpdateMany, UpdateOne
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.results import BulkWriteResult, InsertManyResult, InsertOneResult
from pymongo.write_concern import WriteConcern

WriteOp = Union[InsertOne, DeleteOne, DeleteMany, ReplaceOne, UpdateOne, UpdateMany]

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
    def __getattr__(self, name: Any): ...
    def __getitem__(self, name: Any): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
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
        requests: Sequence[WriteOp],
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[ClientSession] = ...,
    ) -> BulkWriteResult: ...
    def insert_one(
        self, document: Any, bypass_document_validation: bool = ..., session: Optional[ClientSession] = ...
    ) -> InsertOneResult: ...
    def insert_many(
        self,
        documents: Iterable[Any],
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[ClientSession] = ...,
    ) -> InsertManyResult: ...
    def replace_one(
        self,
        filter: Any,
        replacement: Any,
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ): ...
    def update_one(
        self,
        filter: Any,
        update: Any,
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Any] = ...,
        array_filters: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ): ...
    def update_many(
        self,
        filter: Any,
        update: Any,
        upsert: bool = ...,
        array_filters: Optional[Any] = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ): ...
    def drop(self, session: Optional[ClientSession] = ...) -> None: ...
    def delete_one(
        self, filter: Any, collation: Optional[Any] = ..., hint: Optional[Any] = ..., session: Optional[ClientSession] = ...
    ): ...
    def delete_many(
        self, filter: Any, collation: Optional[Any] = ..., hint: Optional[Any] = ..., session: Optional[ClientSession] = ...
    ): ...
    def find_one(self, filter: Optional[Mapping[str, Any]] = ..., *args: Any, **kwargs: Any) -> Optional[Dict[str, Any]]: ...
    def find(self, *args: Any, **kwargs: Any) -> Cursor: ...
    def find_raw_batches(self, *args: Any, **kwargs: Any) -> RawBatchCursor: ...
    def parallel_scan(self, num_cursors: int, session: Optional[ClientSession] = ..., **kwargs: Any) -> List[CommandCursor]: ...
    def estimated_document_count(self, **kwargs: Any) -> int: ...
    def count_documents(self, filter: Mapping[str, Any], session: Optional[ClientSession] = ..., **kwargs: Any) -> int: ...
    def count(self, filter: Optional[Mapping[str, Any]] = ..., session: Optional[ClientSession] = ..., **kwargs: Any) -> int: ...
    def create_indexes(
        self, indexes: Sequence[IndexModel], session: Optional[ClientSession] = ..., **kwargs: Any
    ) -> List[str]: ...
    def create_index(
        self,
        keys: Union[str, Sequence[Tuple[str, Union[int, str]]], Mapping[str, Union[int, str]]],
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> str: ...
    def ensure_index(
        self, key_or_list: Union[str, Sequence[Tuple[str, Union[int, str]]]], cache_for: int = ..., **kwargs: Any
    ) -> Optional[str]: ...
    def drop_indexes(self, session: Optional[ClientSession] = ..., **kwargs: Any) -> None: ...
    def drop_index(self, index_or_name: Any, session: Optional[ClientSession] = ..., **kwargs: Any) -> None: ...
    def reindex(self, session: Optional[ClientSession] = ..., **kwargs: Any): ...
    def list_indexes(self, session: Optional[ClientSession] = ...) -> CommandCursor: ...
    def index_information(self, session: Optional[ClientSession] = ...) -> Dict[str, Any]: ...
    def options(self, session: Optional[ClientSession] = ...) -> Dict[str, Any]: ...
    def aggregate(
        self, pipeline: Sequence[Mapping[str, Any]], session: Optional[ClientSession] = ..., **kwargs: Any
    ) -> CommandCursor: ...
    def aggregate_raw_batches(self, pipeline: Sequence[Mapping[str, Any]], **kwargs: Any) -> RawBatchCursor: ...
    def watch(
        self,
        pipeline: Optional[Any] = ...,
        full_document: Optional[Any] = ...,
        resume_after: Optional[Any] = ...,
        max_await_time_ms: Optional[Any] = ...,
        batch_size: Optional[Any] = ...,
        collation: Optional[Any] = ...,
        start_at_operation_time: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
        start_after: Optional[Any] = ...,
    ): ...
    def group(
        self,
        key: Mapping[str, Any],
        condition: Mapping[str, Any],
        initial: Mapping[str, int],
        reduce: str,
        finalize: Optional[bool] = ...,
        **kwargs: Any,
    ) -> List[Dict[str, Any]]: ...
    def rename(self, new_name: str, session: Optional[ClientSession] = ..., **kwargs: Any) -> None: ...
    def distinct(
        self, key: str, filter: Optional[Mapping[str, Any]] = ..., session: Optional[ClientSession] = ..., **kwargs: Any
    ) -> List[Any]: ...
    def map_reduce(
        self,
        map: str,
        reduce: str,
        out: Union[str, Mapping[str, Any]],
        full_response: bool = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], Database, Collection]: ...
    def inline_map_reduce(
        self, map: str, reduce: str, full_response: bool = ..., session: Optional[ClientSession] = ..., **kwargs: Any
    ) -> Dict[str, Any]: ...
    def find_one_and_delete(
        self,
        filter: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ): ...
    def find_one_and_replace(
        self,
        filter: Any,
        replacement: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        upsert: bool = ...,
        return_document: Any = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ): ...
    def find_one_and_update(
        self,
        filter: Any,
        update: Any,
        projection: Optional[Any] = ...,
        sort: Optional[Any] = ...,
        upsert: bool = ...,
        return_document: Any = ...,
        array_filters: Optional[Any] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
        **kwargs: Any,
    ): ...
    def save(self, to_save: Mapping[str, Any], manipulate: bool = ..., check_keys: bool = ..., **kwargs: Any) -> Any: ...
    def insert(
        self,
        doc_or_docs: Mapping[str, Any],
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
    ) -> Dict[str, Any]: ...
    def remove(self, spec_or_id: Optional[Mapping[str, Any]] = ..., multi: bool = ..., **kwargs: Any) -> Dict[str, Any]: ...
    def find_and_modify(
        self,
        query: Mapping[str, Any] = ...,
        update: Optional[Mapping[str, Any]] = ...,
        upsert: Optional[bool] = ...,
        sort: Optional[Sequence[Tuple[str, Union[int, str]]]] = ...,
        full_response: Optional[bool] = ...,
        manipulate: Optional[bool] = ...,
        **kwargs: Any,
    ) -> Dict[str, Any]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> None: ...
    next: Any = ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
