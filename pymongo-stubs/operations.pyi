from typing import Any, Dict, List, Mapping, MutableMapping, Optional, Sequence, Tuple, Union

from bson.raw_bson import RawBSONDocument
from pymongo.collation import Collation

_DocumentIn = Union[MutableMapping[str, Any], RawBSONDocument]
_Collation = Union[Mapping[str, Any], Collation]
# Hint supports index name, "myIndex", or list of index pairs: [('x', 1), ('y', -1)]
_IndexList = Sequence[Tuple[str, Union[int, str, Mapping[str, Any]]]]
_IndexKeyHint = Union[str, _IndexList]
_Pipeline = List[Mapping[str, Any]]

class InsertOne:
    def __init__(self, document: _DocumentIn) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class DeleteOne:
    def __init__(
        self, filter: Mapping[str, Any], collation: Optional[_Collation] = ..., hint: Optional[_IndexKeyHint] = ...
    ) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class DeleteMany:
    def __init__(
        self, filter: Mapping[str, Any], collation: Optional[_Collation] = ..., hint: Optional[_IndexKeyHint] = ...
    ) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class ReplaceOne:
    def __init__(
        self,
        filter: Mapping[str, Any],
        replacement: Mapping[str, Any],
        upsert: bool = ...,
        collation: Optional[_Collation] = ...,
        hint: Optional[_IndexKeyHint] = ...,
    ) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class UpdateOne:
    def __init__(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        upsert: bool = ...,
        collation: Optional[_Collation] = ...,
        array_filters: Optional[List[Mapping[str, Any]]] = ...,
        hint: Optional[_IndexKeyHint] = ...,
    ) -> None: ...

class UpdateMany:
    def __init__(
        self,
        filter: Mapping[str, Any],
        update: Union[Mapping[str, Any], _Pipeline],
        upsert: bool = ...,
        collation: Optional[_Collation] = ...,
        array_filters: Optional[List[Mapping[str, Any]]] = ...,
        hint: Optional[_IndexKeyHint] = ...,
    ) -> None: ...

class IndexModel:
    def __init__(self, keys: _IndexKeyHint, **kwargs: Any) -> None: ...
    @property
    def document(self) -> Dict[str, Any]: ...
