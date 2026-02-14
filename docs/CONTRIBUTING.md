# Guía de Contribución
Esta guía te ayudará a configurar tu entorno local y seguir el flujo de trabajo correcto con Git.

### Prepara el repositorio
Sigue estos pasos en tu terminal para obtener el código y preparar tu espacio de trabajo:

1. **Clona el repositorio:**  
```bash 
git clone https://github.com/Chametzz/myconta.git
```

2. **Entra a la carpeta:**  
```bash 
cd myconta
```

3. **Muévete a la rama de desarrollo:**  
```bash 
git checkout develop
```

4. **Crea tu rama de trabajo:**  
```bash 
git checkout -b nombre-de-tu-rama
```

### Instala las librerías del proyecto
Para asegurar que el proyecto cuente con todas las librerías necesarias, instala las dependencias listadas en el archivo `requirements.txt` ejecutando el siguiente comando en tu terminal:  
```bash
pip install -r requirements.txt
```

### Sube tus avances
Cuando termines una tarea sigue este orden para subir tus cambios. **Nunca hagas push directo a `main` o `develop`.**  

1. **Añade todos los cambios**  
```bash 
git add .
```

2. **Verifica qué estás enviando:** (Opcional)   
```bash 
git status
```

3. **Confirma cambios con un mensaje:**  
```bash 
git commit -m "Explicación corta de lo que hiciste"
```

4. **Sube los cambios al servidor:** 
```bash
git push origin nombre-de-tu-rama
```

### Mantén tu rama actualizada
Para evitar conflictos cuando quieras unir tu código con el de los demás, mantente sincronizado con la rama `develop`:

* **Descarga los últimos cambios del servidor:**  
```bash
git fetch
```

* **Trae los cambios de desarrollo a tu rama actual**  
```bash
git pull origin develop
```
