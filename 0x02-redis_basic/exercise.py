#!/usr/bin/env python3
"""
redis exercise
"""
from functools import wraps
import redis
from typing import Callable
import uuid


def replay(method: Callable):
    """
    method needs to be a bound function
    """
    print(method.__qualname__)
    print(method.__self__)


def count_calls(method: Callable) -> Callable:
    """
    counts the call of a particular function
    """
    @wraps(method)
    def inner(self, *args, **kwargs):
        """
        inner doc
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return inner


def call_history(method: Callable) -> Callable:
    """
    sets the call history of a function
    """
    @wraps(method)
    def inner(self, *args, **kwargs):
        """
        inner doc
        """
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        ret = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ':outputs', ret)
        return ret
    return inner


class Cache:
    """
    cache class
    """
    def __init__(self):
        """
        initializes the cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: str | bytes | int | float) -> str:
        """
        stores the data in the cache
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable | int | str = None):
        """
        gets data from cache
        """
        if fn is None:
            return self._redis.get(key)
        if fn is str:
            pass
        if fn is int:
            pass
        return fn(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """
        gets key as int
        """
        return int(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """
        gets key as str
        """
        return str(self._redis.get(key))
