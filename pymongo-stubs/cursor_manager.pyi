from typing import Any, Tuple

from pymongo import MongoClient

class CursorManager:
    def __init__(self, client: MongoClient) -> None: ...
    def close(self, cursor_id: int, address: Tuple[str, Any]) -> None: ...
