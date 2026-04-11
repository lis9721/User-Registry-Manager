# ⚙ User Registry Manager

Este sistema CRUD permite gestionar el ciclo de vida de usuarios mediante consola, garantizando la persistencia de datos en archivos JSON.

## 📋 Descripción

Permite registrar, consultar, actualizar y eliminar usuarios de una organización. Los datos se guardan automáticamente en `data/records.json`. Incluye generación de usuarios de prueba con **Faker** para la generación masiva de perfiles de prueba y validación de flujos.

## ✒ Estructura del proyecto

```
User-Registry-Manager/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── users.json              # base de datos de usuarios
│
└── src/
    ├── main.py                 # punto de entrada
    │
    ├── ui/
    │   └── menu.py             # interfaz (menú consola)
    │
    ├── core/
    │   ├── service.py          # lógica CRUD usuarios
    │   ├── file_manager.py     # manejo JSON
    │   └── validators.py       # validaciones
    │
    ├── models/
    │   └── user.py             # estructura del usuario
    │
    ├── utils/
    │   └── helpers.py          # funciones auxiliares
    │
    ├── integrations/
    │   └── faker_data.py       # generación de datos fake
    │
    └── __pycache__/            # NO subir
```

## ⚙️ Requisitos

- Python 3.10 o superior
- pip

## 🚀 Cómo correr el programa

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/gestion-info.git
cd gestion-info
```

### 2. Crea un entorno virtual (recomendado)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta el programa

```bash
cd src
python main.py
```

## 🧩 Funcionalidades

| Opción | Descripción |
|--------|-------------|
| `[1]` Crear usuario | Ingresa nombre, email, edad y rol |
| `[2]` Listar usuarios | Muestra todos los usuarios en tabla |
| `[3]` Actualizar usuario | Edita campos por ID |
| `[4]` Eliminar usuario | Elimina por ID con confirmación |
| `[5]` Generar con Faker | Crea N usuarios de prueba automáticamente |
| `[0]` Salir | Termina el programa |

## 🏷️ Tags de módulos

| Tag | Descripción |
|-----|-------------|
| `m0-setup` | Estructura base y "Sistema listo" |

## 📦 Librerías externas

- [`faker`](https://faker.readthedocs.io/) — Generación de datos falsos realistas en español
