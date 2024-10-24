#!/usr/bin/env python3
"""
redis exercise
"""
from functools import wraps
import redis
from typing import Callable, Union, Optional
import uuid


def replay(method: Callable):
    """
    method needs to be a bound function
    """
    cache = redis.Redis()
    name = method.__qualname__
    call_count = int(cache.get(name).decode("utf-8"))
    in_history = cache.lrange(name + ':inputs', 0, -1)
    out_history = cache.lrange(name + ':outputs', 0, -1)
    print(f'{name} was called {call_count} times:')
    for i_history, o_history in zip(in_history, out_history):
        print("{}(*{}) -> {}".format(name, i_history.decode('utf-8'),
                                     o_history.decode('utf-8')))


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
