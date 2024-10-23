#!/usr/bin/env python3
"""
web redis exercise
"""
from functools import wraps
from typing import Callable
import requests
import redis

cache = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ decorator that counts requests """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ the decorator's child """
        cache.incr(f"count:{url}")
        cached_html = cache.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        cache.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content of a  URL """
    return requests.get(url).text
