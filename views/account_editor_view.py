import tkinter as tk
from tkinter import ttk
from kit.ui.view import View
from view_models.account_editor_view_model import AccountEditorViewModel

class AccountEditorView(View):
    vm: AccountEditorViewModel
    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)

        self.titulo = tk.Label(self, font=("Arial", 18))
        self.titulo.pack(anchor="nw", padx=10, pady=10)

        self.frame = tk.Frame(self)
        self.frame.pack(anchor="nw", padx=10)

        self.label_nombre = tk.Label(self.frame, text="Nombre")
        self.label_nombre.grid(row=0, column=0, sticky="w")

        self.entrada_nombre = tk.Entry(self.frame, width=30)
        self.entrada_nombre.grid(row=1, column=0)

        self.label_divisa = tk.Label(self.frame, text="Divisa")
        self.label_divisa.grid(row=2, column=0, sticky="w")

        self.combo_divisa = ttk.Combobox(self.frame, values=["usd", "mxn"])
        self.combo_divisa.grid(row=3, column=0)

        self.boton_guardar = tk.Button(self.frame, text="Guardar", command=self.vm.save_account)
        self.boton_guardar.grid(row=4, column=0, pady=10, sticky="w")
        self.update()
    
    def on_update(self, changed):
        if changed('title'):
            if self.vm.account.id is None:
                self.titulo.config(text='Crear cuenta')
            else:
                self.titulo.config(text='Editar cuenta')