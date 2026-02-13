# Myconta

Es una aplicación de gestión financiera diseñada para el uso personal. Permite registrar gastos e ingresos en múltiples cuentas.

### Estructura del proyecto

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