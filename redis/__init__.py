from redis.client import Redis, StrictRedis
from redis.connection import (
    ConnectionPool,
    Connection,
    UnixDomainSocketConnection
    )
from redis.exceptions import (
    AuthenticationError,
    ConnectionError,
    DataError,
    InvalidResponse,
    NoScriptError,
    PubSubError,
    RedisError,
    ResponseError,
    WatchError,
    )


__version__ = '2.4.13.1'
VERSION = tuple(map(int, __version__.split('.')))

__all__ = [
    'Redis', 'StrictRedis', 'ConnectionPool',
    'Connection', 'UnixDomainSocketConnection',
    'RedisError', 'ConnectionError', 'ResponseError', 'AuthenticationError',
    'InvalidResponse', 'NoScriptError', 'DataError', 'PubSubError', 'WatchError',
    ]
