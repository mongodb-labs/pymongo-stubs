from typing import Any, List, Mapping, Optional

from pymongo.mongo_client import MongoClient

class AutoEncryptionOpts:
    def __init__(
        self,
        kms_providers: Mapping[str, Any],
        key_vault_namespace: str,
        key_vault_client: Optional[MongoClient] = ...,
        schema_map: Optional[Mapping[str, Any]] = ...,
        bypass_auto_encryption: bool = ...,
        mongocryptd_uri: str = ...,
        mongocryptd_bypass_spawn: bool = ...,
        mongocryptd_spawn_path: str = ...,
        mongocryptd_spawn_args: Optional[List[str]] = ...,
    ) -> None: ...

def validate_auto_encryption_opts_or_none(option: str, value: Any) -> Optional[AutoEncryptionOpts]: ...
