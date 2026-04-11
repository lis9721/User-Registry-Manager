from utils import validar_nombre


def crear_usuario(usuarios: list, nombre: str) -> dict:
    """
    Crea un usuario y lo agrega a la lista.
    """
    validar_nombre(nombre)

    usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre
    }

    usuarios.append(usuario)
    return usuario


def listar_usuarios(usuarios: list) -> list:
    """
    Retorna la lista de usuarios.
    """
    return usuarios


def obtener_usuario(usuarios: list, user_id: int) -> dict:
    """
    Busca un usuario por ID.
    """
    for u in usuarios:
        if u["id"] == user_id:
            return u
    raise ValueError("Usuario no encontrado")


def actualizar_usuario(usuarios: list, user_id: int, nuevo_nombre: str) -> dict:
    """
    Actualiza el nombre de un usuario.
    """
    validar_nombre(nuevo_nombre)

    usuario = obtener_usuario(usuarios, user_id)
    usuario["nombre"] = nuevo_nombre
    return usuario


def eliminar_usuario(usuarios: list, user_id: int) -> None:
    """
    Elimina un usuario por ID.
    """
    usuario = obtener_usuario(usuarios, user_id)
    usuarios.remove(usuario)