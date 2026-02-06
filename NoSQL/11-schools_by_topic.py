#!/usr/bin/env python3
"""
Módulo para filtrar documentos de una colección de MongoDB por un tema.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Devuelve la lista de escuelas que tienen un tema específico.

    Args:
        mongo_collection: Objeto de colección de pymongo.
        topic (string): El tema buscado dentro de la lista 'topics'.

    Returns:
        Una lista de documentos que coinciden con el criterio.
    """
    # Buscamos documentos donde 'topic' esté contenido en el array 'topics'
    schools = mongo_collection.find({"topics": topic})
    return list(schools)


if __name__ == "__main__":
    # El código no se ejecuta al ser importado
    pass