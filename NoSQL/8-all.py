def list_all(mongo_collection):
    """
    Lista todos los documentos en una colección de MongoDB.
    """
    # .find() devuelve un cursor con todos los documentos.
    # Convertirlo a una lista maneja automáticamente el caso de estar vacía.
    return list(mongo_collection.find())