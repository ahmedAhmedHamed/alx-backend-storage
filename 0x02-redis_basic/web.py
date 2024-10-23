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

    @wraps(method)
    def inner(url):
        """
        inner func
        """
        cache.incr(f"count:{url}")
        res = cache.get(f"cached:{url}")
        if res:
            return res.decode('utf-8')
        res = method(url)
        cache.setex(f"cached:{url}", 10, res)
        return res
    return inner


@cache_decorator
def get_page(url: str) -> str:
    """
    gets a page using requests.get
    """
    res = requests.get(url).text
    return res
