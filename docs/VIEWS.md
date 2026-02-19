# Views
Esta sección describe las vistas  ubicadas en `views/`.

# Definición: ¿Qué es Tkinter?

Tkinter (abreviatura de Tk interface) es el kit de herramientas de interfaz gráfica de usuario predeterminado de Python. Actúa como un "envoltorio" que permite a Python comunicarse con Tk, un sistema de ventanas que crea los elementos visuales que vemos en pantalla. Es la librería más utilizada para aplicaciones de escritorio sencillas debido a su ligereza y facilidad de uso.

# ¿Por qué estamos usando Tkinter para "Myconta"?

El equipo ha decidido utilizar Tkinter por las siguientes razones clave:

**Integración Nativa:** Al ser la librería estándar de Python, no requiere instalaciones complejas ni dependencias externas pesadas, lo que facilita que todos los miembros del equipo puedan ejecutar el código sin errores de configuración.

**Facilidad para Prototipado:** Como tus diseños están basados en formularios claros (entradas de texto, menús y botones), Tkinter permite "dibujar" estos elementos con muy pocas líneas de código, acelerando el paso del papel a la aplicación funcional.

**Bajo Consumo de Recursos:** Myconta es una app de administración financiera que debe ser rápida. Tkinter es extremadamente ligero, lo que garantiza que la app abra instantáneamente y no consuma mucha memoria RAM del usuario.

**Multiplataforma:** El código que tus compañeros programen funcionará igual de bien en Windows, macOS o Linux, lo que hace que nuestra app sea accesible para cualquier usuario de escritorio.


# Implementación de las vistas (haciendo uso de tk.frame más ejemplo)
Las vistas en el proyecto hace referencia a los `tk.Frame` que contiene tkinter

# Cátalogo de Vistas (Los diseños de las vistas descritas)

## Vista 1. Pantalla Principal (Dashboard/Home)

**-Objetivo:** Mostrar un resumen rápido de los ingresos, gastos y ahorros del mes actual o cualquier fecha que el usuario desea consultar, permitiendo la navegación hacia las demás funciones.

**-Contexto:** Esta vista se alimenta de la base de datos de transacciones del usuario.

**Encabezado y Filtros**

**-Selector de Fecha (Arriba a la izquierda):** Un botón con forma de cápsula que dice "Febrero 2026".

**-Interacción:** Al tocarlo, debería abrir un "Date Picker" o selector de mes/año para que el usuario consulte meses pasados.

**-Saludo/Mensaje:** Texto "¡Hola! Registremos tus finanzas". Es un elemento de bienvenida dinámico.

**-Icono de Perfil (Arriba a la derecha):** Círculo para la foto del usuario o acceso rápido a ajustes de cuenta.

**Resumen de Saldos (Tarjetas Superiores)
Se divide en dos contenedores principales:**

**-Tarjeta de Ingresos:** Muestra el texto "Ingresos" y el monto acumulado (ej. $0.00). Sugerencia: Usar color verde para el monto.

**-Tarjeta de Gastos:** Muestra el texto "Gastos" y el monto restado (ej. -$0.00). Sugerencia: Usar color rojo para el monto.

**Sección de Ahorro (Panel Central)
Título con Info: "Tu ahorro" acompañado de un icono de información (i) que puede explicar cómo se calcula.**

Panel Dividido:

**-Total:** El ahorro histórico acumulado por el usuario.

**-Mensual:** El ahorro logrado específicamente en el mes seleccionado (Ingresos - Gastos).


**Barra de Navegación Inferior (Tab Bar)Esta es la parte más importante para la estructura de la app**

Consta de 5 botones:

**1.-Home:** Regresa a esta vista principal (Estado activo por defecto).

**2.-Ingresos:** Lleva al formulario para registrar una nueva entrada de dinero.

**3.-Gastos:** Lleva al formulario para registrar una salida de dinero.

**4.-Mi análisis :** Muestra estadísticas visuales (ej. gastos por categoría), y te da la opción de descargar un balance en pdf.

**5.-Mi Cuenta:** Acceso al perfil, configuración, cambio de cuenta y crear cuenta nueva y personalización.

## Vista 2. Vista de ingresos (Income view)

Esta es la pantalla que aparece al presionar el icono de "Ingresos" en la barra de navegación inferior.

**-Indicador de Total:** Muestra el texto "Tus ingresos al día", seguido del monto total y el mes actual (ej. $0.00 MXN Febrero 2026).

**-Selector Lateral:** Flechas < y > para navegar entre diferentes días o periodos.

**-Botón de Acción (+):** Ubicado en la parte superior derecha. Al presionarlo, redirige a la vista completa de "Entrance View" (Formulario de nuevo ingreso).

Pestañas de Detalle:

**-Tu historial:** Lista cronológica de los ingresos registrados.

**-Tus categorías:** Resumen de ingresos agrupados por tipo.

## Vista 3. Formulario de Nuevo Ingreso ("Entrance" View)

Es una vista completa para capturar los datos. Se recomienda que los programadores usen campos de validación para asegurar que no se guarden datos vacíos.

Detalle de Campos: Vista de Formulario (Entrance View)

**Campo: Monto**

Acción / Descripción: Pregunta al usuario: "¿Cuál es el monto de tu ingreso?".

Tipo de Componente: Campo de entrada numérico (Keyboard tipo decimal).

**-Campo: Nombre**

Acción / Descripción: Pregunta al usuario: "¿Qué nombre le quieres dar?".

Tipo de Componente: Campo de texto libre (ejemplo: "Pago quincena").

**Campo: Origen del ingreso**

Acción / Descripción: Pregunta al usuario: "¿El ingreso lo recibiste en?".

Tipo de Componente: Menú desplegable (Dropdown) con opciones fijas: Débito, Crédito, Efectivo.

**Campo: Cuenta destino**

Acción / Descripción: Pregunta al usuario: "¿En cuál tarjeta/cuenta recibiste el ingreso?".

Tipo de Componente: Menú desplegable dinámico que muestra la lista de cuentas creadas previamente por el usuario.

**Campo: Categoría**

Acción / Descripción: Indica: "Categoría de tu ingreso".

Tipo de Componente: Es otra  vista que, al activarse, despliega la Lista de Categorías (Salarios, Bonos, etc.). Que más adelante sera describida.

**Campo: Frecuencia**

Acción / Descripción: Pregunta al usuario: "¿Cada cuánto recibes este ingreso?".

Tipo de Componente: Campo de texto o selector de periodo (único, semanal, quincenal, mensual).

**Campo: Fecha**

Acción / Descripción: Indica: "Fecha de tu ingreso".

Tipo de Componente: Selector de fecha (Calendar picker / Date picker).

**Elemento: Botón Agregar**

Acción / Descripción: Finaliza el proceso y guarda el registro en la base de datos local o en la nube.

Tipo de Componente: Botón de acción (Call to Action).

## Vista 4. Vista de Selección y Creación de Categorías (Ingresos)

**Objetivo:** Permitir al usuario elegir una categoría existente para su ingreso o crear una nueva personalizada.

**Origen:** Se despliega al tocar el campo "Categoría de tu ingreso" en el formulario de Entrance View.

**A. Lista de Categorías Predefinidas**

El programador debe incluir estas opciones iniciales en un listado vertical (Scroll View):

1. Aguinaldo
2. Bonos
3. Emprendimiento
4. Intereses y Dividendos
5. Otros
6. Propinas
7. Regalos
8. Salarios

**B. Sección "Agregar nueva categoría"**

Ubicada en la parte inferior de la lista para no interrumpir el flujo visual:

**-Botón (+):** Al presionarlo, debe disparar un evento para abrir una ventana emergente o un cuadro de diálogo (Pop-up).

**C. Ventana Emergente: Nueva Categoría
Título/Instrucción: "¿Qué nombre le quieres dar a tu categoría?".**

**-Campo de entrada:** Espacio de texto libre para que el usuario escriba el nombre.

**-Botón Guardar:** Acción: Al hacer clic, el nuevo nombre debe almacenarse en la base de datos de categorías del usuario.

**Comportamiento:** La ventana se cierra y la nueva categoría debe aparecer automáticamente seleccionada en el formulario anterior.

## Vista 5. Formulario "Nueva Tarjeta/Cuenta"

**-Objetivo:** Permitir al usuario dar de alta una nueva cuenta o tarjeta en el sistema para que esté disponible en sus registros financieros.

**Origen:** Se accede a esta vista tras presionar el botón de "Agregar tarjeta/cuenta (+)" dentro del menú de selección de cuenta.

**Elementos Visuales y Funcionales**

Basado en el diseño, estos son los componentes que el programador debe implementar:

**-Campo:** Nombre de tarjeta/cuenta

Instrucción: Aparece el texto descriptivo "*Nombre de tarjeta/cuenta".

Componente: Cuadro de texto (Input) para entrada libre.

Ejemplo de uso: El usuario escribe "Nómina Santander" o "Efectivo Personal".

**-Campo:** Tipo de tarjeta

Pregunta: "¿Qué tipo de tarjeta es?".

Componente: Menú desplegable (Dropdown) con dos opciones fijas: Débito y Crédito.

Interacción: Al seleccionar una opción, el valor queda guardado para la configuración de la cuenta.

**-Botón:** Guardar

Ubicación: Parte inferior del formulario.

Acción: Al presionar "Guardar", se debe realizar lo siguiente:

Validar que el nombre no esté vacío.

Almacenar la nueva cuenta en la base de datos local.

**Cerrar la vista y regresar al usuario al formulario de registro (Entrance View) con la nueva cuenta ya seleccionada por defecto.**

**Notas:**

Diseño de interfaz: Esta vista debe mantener la coherencia visual con el resto de la app (mismas fuentes y estilos de botones).

Botón de cancelar: Se recomienda incluir una opción para regresar sin guardar, por si el usuario entró por error.

## Vista 6. Mi Cuenta (Profile and settings)

**-Objetivo:** Permitir al usuario gestionar su información personal, revisar historiales, descargar reportes y administrar su sesión.

Origen: Se accede presionando el icono de usuario ("Mi Cuenta") en el extremo derecho de la barra de navegación inferior.

**Estructura de la Interfaz (Lista de Opciones)**

Cada elemento debe funcionar como un botón que redirige a una sub-vista o ejecuta una acción:

**Correo Electrónico:**

Función: Muestra el correo vinculado o permite editar los datos de contacto.

Componente: Ítem de lista con flecha de navegación >.

**Mis cuentas:**

Función: Ver el listado de todas las tarjetas y cuentas de efectivo dadas de alta.

Componente: Ítem de lista con flecha de navegación >.

**Sección: Descargas (Título de Grupo)**

Historial de Gastos e Ingresos:

Función: Generar o visualizar un reporte detallado de todos los movimientos realizados.

Componente: Ítem de lista con flecha de navegación >.

**Sección: Cuenta (Título de Grupo)**

**-Cerrar sesión:**

Función: Finalizar la sesión actual del usuario.

Componente: Ítem de lista con flecha de navegación >.

**-Cambiar de cuenta:**

Interacción Especial: Según tu diagrama, al presionar aquí se abre un Menú de Selección con dos opciones:

Iniciar con cuenta existente: Redirige al Login.

Crear cuenta nueva: Redirige al flujo de Registro.

**Eliminar cuenta:**

Función: Borrar permanentemente el perfil y los datos del usuario.

Componente: Ítem de lista con flecha de navegación >. (Se recomienda que el programador añada una alerta de confirmación antes de borrar).

## Vista 7. Análisis de mis Finanzas

**-Objetivo:** Proporcionar al usuario una visión visual y comparativa de sus movimientos financieros para facilitar la toma de decisiones.

Origen: Se accede presionando el icono de "Gráfica" (ahora Análisis) en la barra de navegación inferior.

**Elementos Visuales y Funcionales**

**Título de la Vista:** "Análisis de mis Finanzas".

**Buscador de Fecha:**

Texto guía: "Busquemos una fecha...".

Componente: Barra de búsqueda con icono de lupa.

Lógica: Permite filtrar los datos de las gráficas por periodos específicos (mes, año o rango personalizado).

Secciones de Gráficas (Contenedores)
El programador debe implementar dos áreas principales de visualización:

**-Gastos vs Presupuestos:**

Función: Comparar cuánto planeaba gastar el usuario contra lo que realmente ha gastado.

Tipo de gráfica sugerida: Gráfica de barras comparativas.

**-Gastos por Categoría:**

Función: Mostrar en qué conceptos se está yendo el dinero (Comida, Renta, etc.).

Tipo de gráfica sugerida: Gráfica de pastel (Doughnut chart).

**-Acción de Exportación**

Botón: "Descargar Balance"

Comportamiento: Al presionar, la app debe generar un reporte resumen de los datos visualizados.

Formato de salida: El archivo debe exportarse y guardarse automáticamente en el dispositivo como un documento PDF.

## Vista 8. Gastos (Expense view)