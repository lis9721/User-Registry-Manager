from generador import generar_registros

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Generar 10 registros falsos")
        print("2. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            generar_registros()
            print("✅ Registros generados y guardados")
        elif opcion == "2":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    menu()