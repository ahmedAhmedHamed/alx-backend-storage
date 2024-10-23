#!/usr/bin/env python3
"""
web redis exercise
"""
from functools import wraps
from typing import Callable

import requests
import redis


redis_instance = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ counting decorator """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ counting decorator """
        redis_instance.incr(f"count:{url}")
        cached_html = redis_instance.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_instance.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ request html get """
    res = requests.get(url)
    return res.text
