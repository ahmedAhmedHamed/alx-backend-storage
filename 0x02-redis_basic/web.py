#!/usr/bin/env python3
"""
web redis exercise
"""
from functools import wraps
from typing import Callable
import requests
import redis

cache = redis.Redis()


def cache_decorator(method: Callable) -> Callable:
    """
    caches a function's result given args
    """
    def inner(*args, **kwargs):
        """
        inner func
        """

        res = cache.get(str(*args))
        if res:
            return res.decode('utf-8')
        res = method(*args, **kwargs)
        cache.setex(f"cached:{args[0]}", 10, res)
        return res
    return inner


@cache_decorator
def get_page(url: str) -> str:
    """
    gets a page using requests.get
    """
    res = requests.get(url).text
    return res
