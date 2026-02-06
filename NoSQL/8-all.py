#!/usr/bin/env python3
"""
Módulo para interactuar con MongoDB usando PyMongo.
Proporciona una función para listar todos los documentos de una colección.
"""


def list_all(mongo_collection):
    """
    Lista todos los documentos en una colección.

    Args:
        mongo_collection: Objeto de colección de pymongo.

    Returns:
        Una lista con todos los documentos, o una lista vacía si no hay ninguno.
    """
    documents = []
    if mongo_collection is not None:
        cursor = mongo_collection.find()
        for doc in cursor:
            documents.append(doc)
    return documents


if __name__ == "__main__":
    # El código no se ejecuta al ser importado
    pass