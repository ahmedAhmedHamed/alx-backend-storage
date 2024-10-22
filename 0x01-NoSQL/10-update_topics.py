#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection: pymongo.collection.Collection,
                  name, topics):
    """
    function that changes all topics of a school document based on the name
    """
    mongo_collection.update({'name': name}, {'$set': {'topics': topics}})
