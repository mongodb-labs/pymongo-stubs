from collections import namedtuple

from pymongo.pool import SocketInfo

HAVE_KERBEROS: bool
MECHANISMS: frozenset[str]

MongoCredential = namedtuple("MongoCredential", ["mechanism", "source", "username", "password", "mechanism_properties", "cache"])

GSSAPIProperties = namedtuple("GSSAPIProperties", ["service_name", "canonicalize_host_name", "service_realm"])

def authenticate(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def logout(source: str, sock_info: SocketInfo) -> None: ...
