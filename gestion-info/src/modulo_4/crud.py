from data import datos

def crear(item):
    datos.append(item)

def listar():
    return datos

def editar(indice, nuevo_item):
    if 0 <= indice < len(datos):
        datos[indice] = nuevo_item
        return True
    return False

def eliminar(indice):
    if 0 <= indice < len(datos):
        datos.pop(indice)
        return True
    return False