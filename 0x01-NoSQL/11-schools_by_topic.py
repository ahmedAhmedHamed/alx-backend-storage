#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection: pymongo.collection.Collection, topic):
    """
    function that returns the list of school having a specific topics
    """
    return mongo_collection.find({'topics': topic})
