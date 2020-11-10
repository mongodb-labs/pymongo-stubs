from typing import Any, List, Mapping, Optional

from bson.objectid import ObjectId
from gridfs.grid_file import GridIn, GridOut, GridOutCursor
from pymongo.client_session import ClientSession
from pymongo.common import UNAUTHORIZED_CODES as UNAUTHORIZED_CODES
from pymongo.database import Database
from pymongo.errors import OperationFailure as OperationFailure
from pymongo.read_preferences import _ServerMode
from pymongo.write_concern import WriteConcern

class GridFS:
    def __init__(self, database: Database, collection: str = ..., disable_md5: bool = ...) -> None: ...
    def new_file(self, **kwargs: Any) -> GridIn: ...
    def put(self, data: Any, **kwargs: Any) -> Any: ...
    def get(self, file_id: Any, session: Optional[ClientSession] = ...) -> GridOut: ...
    def get_version(
        self, filename: Optional[str] = ..., version: int = ..., session: Optional[ClientSession] = ..., **kwargs: Any
    ) -> GridOut: ...
    def get_last_version(
        self, filename: Optional[str] = ..., session: Optional[ClientSession] = ..., **kwargs: Any
    ) -> GridOut: ...
    def delete(self, file_id: Any, session: Optional[ClientSession] = ...) -> None: ...
    def list(self, session: Optional[ClientSession] = ...) -> List[str]: ...
    def find_one(
        self, filter: Optional[Any] = ..., session: Optional[ClientSession] = ..., *args: Any, **kwargs: Any
    ) -> Optional[GridOut]: ...
    def find(self, *args: Any, **kwargs: Any) -> GridOutCursor: ...
    def exists(self, document_or_id: Optional[Any] = ..., session: Optional[ClientSession] = ..., **kwargs: Any) -> bool: ...

class GridFSBucket:
    def __init__(
        self,
        db: Database,
        bucket_name: str = ...,
        chunk_size_bytes: int = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_preference: Optional[_ServerMode] = ...,
        disable_md5: bool = ...,
    ) -> None: ...
    def open_upload_stream(
        self,
        filename: str,
        chunk_size_bytes: Optional[int] = ...,
        metadata: Optional[Mapping[str, Any]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> GridIn: ...
    def open_upload_stream_with_id(
        self,
        file_id: Any,
        filename: str,
        chunk_size_bytes: Optional[int] = ...,
        metadata: Optional[Mapping[str, Any]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> GridIn: ...
    def upload_from_stream(
        self,
        filename: str,
        source: Any,
        chunk_size_bytes: Optional[int] = ...,
        metadata: Optional[Mapping[str, Any]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> ObjectId: ...
    def upload_from_stream_with_id(
        self,
        file_id: Any,
        filename: str,
        source: Any,
        chunk_size_bytes: Optional[int] = ...,
        metadata: Optional[Mapping[str, Any]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    def open_download_stream(self, file_id: Any, session: Optional[ClientSession] = ...) -> GridOut: ...
    def download_to_stream(self, file_id: Any, destination: Any, session: Optional[ClientSession] = ...) -> None: ...
    def delete(self, file_id: Any, session: Optional[ClientSession] = ...) -> None: ...
    def find(self, *args: Any, **kwargs: Any) -> GridOutCursor: ...
    def open_download_stream_by_name(
        self, filename: str, revision: Optional[int] = ..., session: Optional[ClientSession] = ...
    ) -> GridOut: ...
    def download_to_stream_by_name(
        self, filename: str, destination: Any, revision: int = ..., session: Optional[ClientSession] = ...
    ) -> None: ...
    def rename(self, file_id: Any, new_filename: str, session: Optional[ClientSession] = ...) -> None: ...
