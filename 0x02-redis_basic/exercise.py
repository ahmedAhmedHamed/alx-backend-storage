#!/usr/bin/env python3
"""
redis exercise
"""
import redis
from typing import Callable, Union, Optional
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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores the data in the cache
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> (
            Union)[str, bytes, int, float]:
        """
        gets data from cache
        """
        if fn is None:
            return self._redis.get(key)
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
