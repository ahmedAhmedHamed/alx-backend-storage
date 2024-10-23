#!/usr/bin/env python3
"""
redis exercise
"""
from typing import Callable

import redis
import uuid


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

    def store(self, data: str | bytes | int | float) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable | int | str = None):
        if fn is None:
            return self._redis.get(key)
        if fn is str:
            pass
        if fn is int:
            pass
        return fn(self._redis.get(key))

    def get_int(self, key: str) -> int:
        return int(self._redis.get(key))

    def get_str(self, key: str) -> str:
        return str(self._redis.get(key))
