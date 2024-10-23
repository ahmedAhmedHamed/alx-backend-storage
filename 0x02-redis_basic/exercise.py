#!/usr/bin/env python3
"""
redis exercise
"""
import redis
from typing import Callable, Union
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
