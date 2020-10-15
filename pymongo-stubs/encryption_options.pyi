from typing import Any, Optional

class AutoEncryptionOpts:
    def __init__(
        self,
        kms_providers: Any,
        key_vault_namespace: Any,
        key_vault_client: Optional[Any] = ...,
        schema_map: Optional[Any] = ...,
        bypass_auto_encryption: bool = ...,
        mongocryptd_uri: str = ...,
        mongocryptd_bypass_spawn: bool = ...,
        mongocryptd_spawn_path: str = ...,
        mongocryptd_spawn_args: Optional[Any] = ...,
    ) -> None: ...

def validate_auto_encryption_opts_or_none(option: Any, value: Any) -> Any: ...
