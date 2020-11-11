from typing import Any, Dict, List

class _WriteResult:
    def __init__(self, acknowledged: bool) -> None: ...
    @property
    def acknowledged(self) -> bool: ...

class InsertOneResult(_WriteResult):
    def __init__(self, inserted_id: Any, acknowledged: bool) -> None: ...
    @property
    def inserted_id(self) -> Any: ...

class InsertManyResult(_WriteResult):
    def __init__(self, inserted_ids: List[Any], acknowledged: bool) -> None: ...
    @property
    def inserted_ids(self) -> List[Any]: ...

class UpdateResult(_WriteResult):
    def __init__(self, raw_result: Dict[str, Any], acknowledged: bool) -> None: ...
    @property
    def raw_result(self) -> Dict[str, Any]: ...
    @property
    def matched_count(self) -> int: ...
    @property
    def modified_count(self) -> int: ...
    @property
    def upserted_id(self) -> Any: ...

class DeleteResult(_WriteResult):
    def __init__(self, raw_result: Dict[str, Any], acknowledged: bool) -> None: ...
    @property
    def raw_result(self) -> Dict[str, Any]: ...
    @property
    def deleted_count(self) -> int: ...

class BulkWriteResult(_WriteResult):
    def __init__(self, bulk_api_result: Dict[str, Any], acknowledged: bool) -> None: ...
    @property
    def bulk_api_result(self) -> Dict[str, Any]: ...
    @property
    def inserted_count(self) -> int: ...
    @property
    def matched_count(self) -> int: ...
    @property
    def modified_count(self) -> int: ...
    @property
    def deleted_count(self) -> int: ...
    @property
    def upserted_count(self) -> int: ...
    @property
    def upserted_ids(self) -> Dict[int, Any]: ...
