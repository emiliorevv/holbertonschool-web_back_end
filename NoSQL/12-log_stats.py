#!/usr/bin/env python3
"""
Módulo para el análisis estadístico de registros Nginx en MongoDB.
"""
from pymongo import MongoClient


def run_log_stats():
    """
    Extrae y muestra estadísticas clave de la colección logs.nginx.
    """
    # Conexión al servidor local de MongoDB
    db_client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_col = db_client.logs.nginx

    # Obtención del total general de documentos
    total_records = nginx_col.count_documents({})
    print(f"{total_records} logs")

    # Resumen de conteos por método HTTP
    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for verb in http_methods:
        method_count = nginx_col.count_documents({"method": verb})
        print(f"\tmethod {verb}: {method_count}")

    # Verificación específica del endpoint de estado
    status_query = {"method": "GET", "path": "/status"}
    checks = nginx_col.count_documents(status_query)
    print(f"{checks} status check")


if __name__ == "__main__":
    run_log_stats()