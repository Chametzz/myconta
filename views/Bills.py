import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Crear/Editar cuenta")
ventana.geometry("400x250")

titulo = tk.Label(ventana, text="Crear/Editar cuenta", font=("Arial", 18))
titulo.pack(anchor="nw", padx=10, pady=10)

frame = tk.Frame(ventana)
frame.pack(anchor="nw", padx=10)

label_nombre = tk.Label(frame, text="Nombre")
label_nombre.grid(row=0, column=0, sticky="w")

entrada_nombre = tk.Entry(frame, width=30)
entrada_nombre.grid(row=1, column=0)

label_divisa = tk.Label(frame, text="Divisa")
label_divisa.grid(row=2, column=0, sticky="w")

combo_divisa = ttk.Combobox(frame, values=["USD", "MXN"])
combo_divisa.grid(row=3, column=0)

boton_guardar = tk.Button(frame, text="Guardar")
boton_guardar.grid(row=4, column=0, pady=10, sticky="w")

ventana.mainloop()