#!/usr/bin/env python3
"""
web redis exercise
"""
from typing import Callable
import requests
import redis


def cache_decorator(method: Callable) -> Callable:
    """
    caches a function's result given args
    """
    def inner(*args, **kwargs):
        """
        inner func
        """
        cache = redis.Redis()
        res = cache.get(str(*args))
        if res:
            return res.decode('utf-8')
        res = method(*args, **kwargs)
        cache.setex(str(*args), 10, res)
        return res
    return inner


@cache_decorator
def get_page(url: str) -> str:
    res = requests.get(url).text
    return res
