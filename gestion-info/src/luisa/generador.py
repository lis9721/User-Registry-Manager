from faker import Faker
from utils import crear_cliente
from storage import guardar_datos

fake = Faker()

def generar_registros(cantidad=10):
    registros = []

    for i in range(cantidad):
        cliente = crear_cliente(
            nombre=fake.name(),
            telefono=fake.phone_number()
        )

        venta = {
            "id_venta": f"V{100 + i}",
            "fecha": fake.date(),
            "cliente": cliente,
            "productos": [
                {
                    "nombre": fake.word(),
                    "cantidad": fake.random_int(min=1, max=5),
                    "precio": fake.random_int(min=1000, max=50000)
                }
            ]
        }

        registros.append(venta)

    guardar_datos(registros)