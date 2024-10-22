#!/usr/bin/env python3
"""
function that returns all students sorted by average score
"""
import pymongo


def top_students(mongo_collection: pymongo.collection.Collection):
    """
    function that returns all students sorted by average score
    """
    pipeline = [
        {
            '$unwind': '$topics'
        },
        {
            '$addFields': {'averageScore': {'$avg': "$topics.score"}}
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    return mongo_collection.aggregate(pipeline)

