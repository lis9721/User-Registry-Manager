from colorama import Fore, init
from crud import crear, listar, editar, eliminar

init(autoreset=True)

def mostrar_menu():
    print(Fore.CYAN + "\n--- MENÚ ---")
    print("1. Crear")
    print("2. Listar")
    print("3. Editar")
    print("4. Eliminar")
    print("5. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print(Fore.RED + "⚠️ Debes ingresar un número.")
            continue

        if opcion == 1:
            item = input("Ingrese dato: ")
            crear(item)
            print(Fore.GREEN + "✔️ Creado correctamente")

        elif opcion == 2:
            lista = listar()
            print(Fore.YELLOW + "\nLista de datos:")
            for i, item in enumerate(lista):
                print(f"{i}: {item}")

        elif opcion == 3:
            try:
                indice = int(input("Índice a editar: "))
                nuevo = input("Nuevo valor: ")
                if editar(indice, nuevo):
                    print(Fore.GREEN + "✔️ Editado")
                else:
                    print(Fore.RED + "Índice inválido")
            except ValueError:
                print(Fore.RED + "Entrada inválida")

        elif opcion == 4:
            try:
                indice = int(input("Índice a eliminar: "))
                if eliminar(indice):
                    print(Fore.GREEN + "✔️ Eliminado")
                else:
                    print(Fore.RED + "Índice inválido")
            except ValueError:
                print(Fore.RED + "Entrada inválida")

        elif opcion == 5:
            print(Fore.MAGENTA + "👋 Saliendo...")
            break

        else:
            print(Fore.RED + "Opción no válida")