# Myconta

Es una aplicación de gestión financiera diseñada para el uso personal. Permite llevar el registro de gastos e ingresos en múltiples cuentas.  

Está desarrollada en **Python** utilizando **Tkinter.**

## Estructura del proyecto
La estructura del proyecto está construida bajo el patrón de diseño MVVM (Model-View-ViewModel). También incluye una capa adicional llamada services que se encarga de proveer la infraestructura necesaria para la aplicación.

```text
MYCONTA/
├── models/                 # Clases de datos
├── views/                  # Interfaces de usuario en Tkinter
├── viewmodels/             # Lógica que conecta Vistas y Modelos
├── services/               # Capa encargada de tareas externas
│   └── database.py         # Inicialización y referencia de la Base de Datos
├── app.py                  # Configuración y clase principal de la app Tkinter
├── main.py                 # Ejecución principal
├── .gitignore              # Archivos excluidos del control de versiones
├── requirements.txt        # Lista de librerías externas necesarias para el proyecto
└── README.md               # Documentación del proyecto
```

> [!IMPORTANT]
> **¿Eres nuevo en el proyecto?** Comienza revisando la **[Guía de Contribución](./docs/CONTRIBUTING.md)** para configurar tu entorno e instalar todas las dependencias necesarias.

## Contenido

* **[Modelos](./docs/MODELS.md)**
* **[Modelos de Vista](./docs/MODELS.md)**
* **[Vistas](./docs/VIEWS.md)**
* **Servicios:**
  * **[Base de Datos](./docs/DATABASE.md)**