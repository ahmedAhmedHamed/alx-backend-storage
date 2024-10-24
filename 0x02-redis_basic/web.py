#!/usr/bin/env python3
"""
web redis exercise
"""
from functools import wraps
from typing import Callable

import requests
import redis


redis_instance = redis.Redis()


def cache(method: Callable) -> Callable:
    """ decorator for url """
    @wraps(method)
    def wrapper(url: str):
        """ decorator for url """
        cached_key = url
        cached_data = redis_instance.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")
        html = method(url)
        redis_instance.set(cached_key, html)
        redis_instance.expire(cached_key, 10)
        return html
    return wrapper


@cache
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    count_key = "count:{url}"
    redis_instance.incr(count_key)
    res = requests.get(url)
    return res.text
