from service import *
from storage import cargar_datos, guardar_datos


def menu():
    usuarios = cargar_datos()

    while True:
        print("\n1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Seleccione: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                crear_usuario(usuarios, nombre)
                guardar_datos(usuarios)

            elif opcion == "2":
                for u in listar_usuarios(usuarios):
                    print(u)

            elif opcion == "3":
                user_id = int(input("ID: "))
                nombre = input("Nuevo nombre: ")
                actualizar_usuario(usuarios, user_id, nombre)
                guardar_datos(usuarios)

            elif opcion == "4":
                user_id = int(input("ID: "))
                eliminar_usuario(usuarios, user_id)
                guardar_datos(usuarios)

            elif opcion == "5":
                break

            else:
                print("Opción inválida")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()