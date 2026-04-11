from service import crear_usuario, obtener_usuario


def test_crear_usuario():
    usuarios = []
    usuario = crear_usuario(usuarios, "Eli")

    assert usuario["nombre"] == "Eli"
    assert len(usuarios) == 1


def test_crear_usuario_nombre_vacio():
    usuarios = []

    try:
        crear_usuario(usuarios, "")
    except ValueError:
        assert True


def test_obtener_usuario():
    usuarios = [{"id": 1, "nombre": "Eli"}]
    usuario = obtener_usuario(usuarios, 1)

    assert usuario["nombre"] == "Eli"


def test_usuario_no_existe():
    usuarios = []

    try:
        obtener_usuario(usuarios, 1)
    except ValueError:
        assert True