# Base de Datos
El módulo `services/database.py` centraliza la conexión con el motor de base de datos y se encarga de la creación de tablas.  
Actualmente, implementa **SQLite** como motor de base de datos y centraliza la lógica de inicialización del esquema mediante la creación automática de tablas.

# Registro de [Modelos](MODELS.md)
Cuando crees un archivo en `models/`, debes actualizar `initialize_db()` siguiendo estos pasos:
1. Importa la clase dentro de la función (no al principio del archivo).
2. Registro en la Lista: Añade la clase a la lista de `create_tables`.

>[!CAUTION]
>Nunca importes modelos fuera de `intialize_db()`. Hacerlo causará un fallo inmediato en el arranque de la aplicación debido a dependencias circulares con el objeto db.