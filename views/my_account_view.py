import tkinter as tk
from tkinter import messagebox

# -----------------------
# Ventana principal
# -----------------------
root = tk.Tk()
root.title("Mi cuenta")
root.geometry("500x350")
root.configure(bg="#d9d9d9")

# -----------------------
# Barra superior (titulo)
# -----------------------
header = tk.Frame(root, bg="#9e9e9e", height=60)
header.pack(fill="x")

titulo = tk.Label(
    header,
    text="Mi cuenta",
    bg="#9e9e9e",
    fg="white",
    font=("Arial", 20, "bold")
)
titulo.pack(side="left", padx=15, pady=10)

# -----------------------
# Contenedor principal
# -----------------------
contenedor = tk.Frame(root, bg="#d9d9d9")
contenedor.pack(fill="both", expand=True, padx=20, pady=20)

# -----------------------
# FUNCIONES
# -----------------------
def editar_cuenta():
    messagebox.showinfo("Editar", "Abrir ventana editar cuenta")

def eliminar_cuenta():
    confirmar = messagebox.askyesno(
        "Eliminar",
        "¿Seguro que deseas eliminar la cuenta?"
    )
    if confirmar:
        messagebox.showinfo("Cuenta", "Cuenta eliminada")

# -----------------------
# Botón EDITAR CUENTA
# -----------------------
btn_editar = tk.Button(
    contenedor,
    text="Editar cuenta        ➤",
    anchor="w",
    bg="black",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    padx=10,
    command=editar_cuenta
)
btn_editar.pack(fill="x", pady=8, ipady=8)

# -----------------------
# Botón ELIMINAR CUENTA
# -----------------------
btn_eliminar = tk.Button(
    contenedor,
    text="Eliminar cuenta        ✖",
    anchor="w",
    bg="#ff1a1a",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    padx=10,
    command=eliminar_cuenta
)
btn_eliminar.pack(fill="x", pady=8, ipady=8)

# -----------------------
root.mainloop()