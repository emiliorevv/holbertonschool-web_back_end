#!/usr/bin/env python3
"""
Script que proporciona estadísticas sobre los logs de Nginx almacenados en MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Muestra estadísticas sobre la colección nginx en la base de datos logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total de logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Estadísticas por métodos
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Conteo específico para GET /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()