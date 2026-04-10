import json

ARCHIVO = "ventas.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r") as file:
            return json.load(file)
    except:
        return []

def guardar_datos(nuevos):
    data = cargar_datos()
    data.extend(nuevos)

    with open(ARCHIVO, "w") as file:
        json.dump(data, file, indent=4)