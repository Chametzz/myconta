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

## ¿Cómo unirse al desarrollo?
Esta guía te ayudará a configurar tu entorno local y seguir el flujo de trabajo correcto con Git.

### Preparar repositorio
Sigue estos pasos en tu terminal para obtener el código y preparar tu espacio de trabajo:

1. **Clona el repositorio:**  
```bash 
git clone https://github.com/Chametzz/myconta.git
```

2. **Entrar a la carpeta:**  
```bash 
cd myconta
```

3. **Moverse a la rama de desarrollo:**  
```bash 
git checkout develop
```

4. **Crear tu rama de trabajo:**  
```bash 
git checkout -b nombre-de-tu-rama
```

### Instala las librerías del proyecto
Para asegurar que el proyecto cuente con todas las librerías necesarias, instala las dependencias listadas en el archivo `requirements.txt` ejecutando el siguiente comando en tu terminal:  
```bash
pip install -r requirements.txt
```

### Subir tus avances
Cuando termines una tarea sigue este orden para subir tus cambios. **Nunca hagas push directo a `main` o `develop`.**  

1. **Añadir todos los cambios**  
```bash 
git add .
```

2. **Verificar qué estás enviando:** (Opcional)   
```bash 
git status
```

3. **Confirmar cambios con un mensaje:**  
```bash 
git commit -m "Explicación corta de lo que hiciste"
```

4. **Subir los cambios al servidor:** 
```bash
git push origin nombre-de-tu-rama
```

### Mantén tu rama actualizada
Para evitar conflictos cuando quieras unir tu código con el de los demás, mantente sincronizado con la rama `develop`:

* **Descargar los últimos cambios del servidor:**  
```bash
git fetch
```

* **Traer los cambios de desarrollo a tu rama actual**  
```bash
git pull origin develop
```