import tkinter as tk
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.title("Configuración")
ventana.geometry("360x500")
ventana.config(bg="#eaeaea")#cambia el color del fondoo

# Funciones
def accion(texto):
    messagebox.showinfo("Opción", f"Seleccionaste: {texto}") # muestra una ventanita con el mensaje 

def crear_seccion(titulo):
    label = tk.Label(
        ventana,
        text=titulo,
        bg="#eaeaea",
        fg="blue",
        font=("Arial", 11, "bold")
    )
    label.pack(anchor="w", padx=20, pady=(15,5))
 ##pone de color los subtitulos  y lo alinia a la izquierda 

def crear_opcion(texto):
    frame = tk.Frame(ventana, bg="white")
    frame.pack(fill="x", padx=15, pady=2)## se crea un contenedor para que le boton y las flechas esten juntos 

    boton = tk.Button(
        frame,
        text=texto,
        anchor="w",
        bg="white",
        relief="flat",
        padx=15,
        pady=12,
        font=("Arial", 11),
        command=lambda: accion(texto)#ejecuta el boton cuando se le da click 
    )
    boton.pack(side="left", fill="x", expand=True)

    flecha = tk.Label(
        frame,
        text=">",
        bg="white",
        fg="gray",
        font=("Arial", 12, "bold")
    ) 
    flecha.pack(side="right", padx=10)
#solamente crea las flechas en los botones 

titulo = tk.Label( #crea todo en la pantalla , toda la interfaz grafica se crea aqui 
    ventana,
    text="Configuración",
    bg="#eaeaea",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

crear_opcion("Correo Electrónico")
crear_opcion("Mis cuentas")

crear_seccion("Descargas")
crear_opcion("Historial de Gastos e ingresos")

crear_seccion("Cuenta")
crear_opcion("Cerrar sesión")
crear_opcion("Cambiar de cuenta")
crear_opcion("Eliminar cuenta")

ventana.mainloop()