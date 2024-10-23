#!/usr/bin/env python3
"""
web redis exercise
"""
from functools import wraps
from typing import Callable

import requests
import redis


redis_instance = redis.Redis()


def my_cache(method: Callable) -> Callable:
    """ Caches the output of fetched data. """
    @wraps(method)
    def invoker(url) -> str:
        """The wrapper function for caching the output.
        """
        redis_instance.incr(f'count:{url}')
        result = redis_instance.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_instance.set(f'count:{url}', 0)
        redis_instance.setex(f'result:{url}', 10, result)
        return result
    return invoker


@my_cache
def get_page(url: str) -> str:
    """Returns the content of a URL after caching the request's response,
    and tracking the request.
    """
    return requests.get(url).text
