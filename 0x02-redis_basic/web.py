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
    def wrapper(url):
        """ the decorator's child """

        # cached_html = cache.get(f"cached:{url}")
        # if cached_html:
        #     return cached_html.decode('utf-8')
        html = method(url)
        # cache.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content of a  URL """
    cache.incr("count:{" + url + "}")
    return requests.get(url).text

# url = 'http://slowwly.robertomurray.co.uk'
# print(cache.set("count:{" + url + "}"))
# get_page(url)
# print(cache.get("count:{" + url + "}"))
# get_page(url)
# get_page(url)
# print(cache.get("count:{" + url + "}"))

