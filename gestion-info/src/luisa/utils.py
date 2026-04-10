def crear_cliente(**kwargs):
    return {
        "nombre": kwargs.get("nombre", ""),
        "telefono": kwargs.get("telefono", "")
    }