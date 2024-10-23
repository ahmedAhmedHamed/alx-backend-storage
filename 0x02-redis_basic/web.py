#!/usr/bin/env python3
"""
web redis exercise
"""
import requests
import redis


def get_page(url: str) -> str:
    """ Obtain the HTML content of a  URL """
    cache = redis.Redis()
    cached_html = cache.get(f"cached:{url}")
    if cached_html:
        return cached_html.decode('utf-8')
    html = requests.get(url).text
    cache.incr("count:" + url)
    cache.setex(f"cached:{url}", 10, html)
    return html
