import json
import os

ARCHIVO = "data.json"

# UTILIDADES

def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("Error al leer el archivo.")
        return []

def guardar_datos(datos):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
    except:
        print("Error al guardar los datos.")

# CREATE

def crear_producto():
    datos = cargar_datos()
    
    try:
        id_producto = input("ID: ").strip()
        
        # Validación: ID único
        if any(p["id"] == id_producto for p in datos):
            print("❌ Error: El ID ya existe.")
            return
        
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        producto = {
            "id": id_producto,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        datos.append(producto)
        guardar_datos(datos)
        print("✅ Producto creado correctamente.")

    except ValueError:
        print("❌ Error: Precio o cantidad inválidos.")

# READ

def listar_productos():
    datos = cargar_datos()
    
    if not datos:
        print("⚠️ No hay productos.")
        return
    
    # Uso de lambda para ordenar por nombre
    datos_ordenados = sorted(datos, key=lambda x: x["nombre"])

    for p in datos_ordenados:
        print(f'ID: {p["id"]} | Nombre: {p["nombre"]} | Precio: {p["precio"]} | Cantidad: {p["cantidad"]}')

def buscar_producto():
    datos = cargar_datos()
    termino = input("Buscar por nombre: ").lower()

    # List comprehension para filtrar
    resultados = [p for p in datos if termino in p["nombre"].lower()]

    if resultados:
        for p in resultados:
            print(p)
    else:
        print("❌ No se encontraron resultados.")

# UPDATE


def actualizar_producto():
    datos = cargar_datos()
    id_producto = input("ID a actualizar: ")

    for p in datos:
        if p["id"] == id_producto:
            try:
                p["nombre"] = input("Nuevo nombre: ")
                p["precio"] = float(input("Nuevo precio: "))
                p["cantidad"] = int(input("Nueva cantidad: "))
                
                guardar_datos(datos)
                print("✅ Producto actualizado.")
                return
            except ValueError:
                print("❌ Error: Datos inválidos.")
                return

    print("❌ Error: ID no encontrado.")

# DELETE

def eliminar_producto():
    datos = cargar_datos()
    id_producto = input("ID a eliminar: ")

    # List comprehension para eliminar
    nuevos_datos = [p for p in datos if p["id"] != id_producto]

    if len(nuevos_datos) == len(datos):
        print("❌ Error: ID no encontrado.")
    else:
        guardar_datos(nuevos_datos)
        print("✅ Producto eliminado.")

# MENÚ

def menu():
    while True:
        print("\n--- CRUD PRODUCTOS ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()