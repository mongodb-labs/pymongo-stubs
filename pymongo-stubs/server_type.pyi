from typing import NamedTuple

class _ServerType(NamedTuple):
    Unknown: int
    Mongos: int
    RSPrimary: int
    RSSecondary: int
    RSArbiter: int
    RSOther: int
    RSGhost: int
    Standalone: int

SERVER_TYPE: _ServerType
