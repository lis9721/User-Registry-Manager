def validar_nombre(nombre: str) -> None:
    """
    Valida que el nombre no esté vacío.
    """
    if not nombre or nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío")