#!/usr/bin/env python3
"""
nginx logins guardados en la db
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    estadisticas de los logins de nginx
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    log_count = nginx_collection.count_documents({})
    print("{} logs".format(log_count))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))