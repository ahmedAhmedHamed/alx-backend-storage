#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
import pymongo
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection: pymongo.collection = client.logs.nginx

    count_logs = log_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f'{count_logs} logs')
    print("Methods:")
    # x = (log_collection.find())
    # for y in x:
    #     print(y)

    for method in methods:
        print(f'\tmethod {method}: '
              f'{log_collection.count_documents({"method": method})}')
    count_status = log_collection.count_documents({
        "method": "GET",
        "path": '/status'
    })
    print(f'{count_status} status check')
