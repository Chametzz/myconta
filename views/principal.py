import tkinter as tk
from tkinter import ttk

try:
    from views.my_account import MyAccount
except ModuleNotFoundError:
    from my_account import MyAccount

try:
    from views.analysis import Analysis
except ModuleNotFoundError:
    from analysis import Analysis

import tkinter as tk

class GestorPerfiles(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyConta - Seleccionar Perfil")
        self.geometry("800x500")
        self.configure(bg="black") # Estilo oscuro tipo Netflix

        # Contenedor principal que se centra
        self.main_frame = tk.Frame(self, bg="black")
        self.main_frame.pack(expand=True)

        self.titulo = tk.Label(
            self.main_frame, 
            text="¿Quién está usando MyConta?", 
            fg="white", bg="black", 
            font=("Arial", 24)
        )
        self.titulo.pack(pady=40)

        # Frame para los cuadraditos
        self.grid_perfiles = tk.Frame(self.main_frame, bg="black")
        self.grid_perfiles.pack()

        # Datos de ejemplo
        perfiles = ["Personal", "Negocio", "Ahorros", "Hijos"]
        
        for i, nombre in enumerate(perfiles):
            self.crear_perfil(nombre, i)

    def crear_perfil(self, nombre, columna):
        # Cada perfil es un frame con un botón y un texto
        frame_item = tk.Frame(self.grid_perfiles, bg="black", padx=15)
        frame_item.grid(row=0, column=columna)

        # El "Cuadradito" (representado por un botón)
        btn = tk.Button(
            frame_item, 
            width=15, height=7, 
            bg="#333333", # Gris oscuro
            activebackground="#666666", 
            relief="flat",
            command=lambda: print(f"Cargando {nombre}...")
        )
        btn.pack()

        # Etiqueta del nombre
        lbl = tk.Label(
            frame_item, 
            text=nombre, 
            fg="gray", bg="black", 
            font=("Arial", 12)
        )
        lbl.pack(pady=10)

        # Efecto visual simple al pasar el mouse
        btn.bind("<Enter>", lambda e, l=lbl: l.config(fg="white"))
        btn.bind("<Leave>", lambda e, l=lbl: l.config(fg="gray"))

class Principal(tk.Frame):
    """
    Esta es la vista principal del programa donde se despliegan las secciones para poder administrar los asientos contables de tu cuenta.
    """
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        self.body = tk.Frame(self, relief="solid", bd=1)
        self.body.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))

        self.bottom_navigation_bar = tk.Frame(self)
        self.bottom_navigation_bar.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=10
        )

        for i in range(5):
            self.bottom_navigation_bar.columnconfigure(i, weight=1, uniform="nav")
        self.bottom_navigation_bar.rowconfigure(0, weight=1)

        destinations = [
            (tk.Frame, "Principal", 0),
            (tk.Frame, "Ingresos", 1),
            (tk.Frame, "Gastos", 2),
            (Analysis, "Análisis", 3),
            (MyAccount, "Mi cuenta", 4),
        ]

        for view_class, text, col in destinations:
            btn = ttk.Button(
                self.bottom_navigation_bar,
                text=text,
                command=lambda v=view_class: self.set_body_view(v),
            )
            btn.grid(row=0, column=col, sticky="nsew", padx=1, pady=0)

    def set_body_view(self, view_class, *args, **kwargs):
        """
        Despliega una vista sobre el body.
        
        :param view_class: La clase de la vista a desplegar
        :param args/kwargs: Parámetros para la vista a desplegar
        """
        for widget in self.body.winfo_children():
            widget.destroy()
            if hasattr(widget, "on_exit"):
                widget.on_exit()

        try:
            new_view = view_class(self.body, *args, **kwargs)
        except TypeError as e:
            raise TypeError(f"Error al desplegar {view_class.__name__}.") from e

        new_view.pack(fill="both", expand=True)
        if hasattr(new_view, "on_enter"):
            new_view.on_enter()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    app = Principal(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
