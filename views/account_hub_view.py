from kit.ui.view import View
from kit.color_schema import color_schema
import tkinter as tk
from tkinter import messagebox

class AccountHubView(View):
    
    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)
        
        self.config(bg=color_schema.SURFACE)
        self.create_topbar()
        
        self.accounts_frame = tk.Frame(self, bg=color_schema.SURFACE)
        self.accounts_frame.pack(expand=True)

        self.create_account("Cuenta 1", 0, 0)
        self.create_account("Cuenta 2", 0, 1)
        self.create_account("Cuenta 3", 0, 2)
        self.create_account("Cuenta 4", 0, 3)

    def create_topbar(self):
        frame = tk.Frame(self, bg=color_schema.SURFACE_CONTAINER)
        frame.pack(fill="x")

        titulo = tk.Label(
            frame,
            text="Elige una cuenta",
            bg=color_schema.SURFACE_CONTAINER,
            fg=color_schema.ON_SURFACE,
            font=("Arial", 16, "bold")
        )
        titulo.pack(side="left", padx=20, pady=10)

        boton_mas = tk.Button(
            frame,
            text="+",
            fg=color_schema.ON_SURFACE_VARIANT,
            bg=color_schema.SURFACE_CONTAINER,
            font=("Arial", 24, "bold"),
            borderwidth=0,
            activebackground=color_schema.SURFACE_CONTAINER_HIGH,
            command=self.add_account
        )
        boton_mas.pack(side="right", padx=10, pady=10)

        boton_settings = tk.Button(
            frame,
            text="⚙",
            fg=color_schema.ON_SURFACE_VARIANT,
            bg=color_schema.SURFACE_CONTAINER,
            font=("Arial", 24),
            borderwidth=0,
            activebackground=color_schema.SURFACE_CONTAINER_HIGH,
            command=self.settings
        )
        boton_settings.pack(side="right", pady=10)

    def create_account(self, text, row, column):
        boton = tk.Button(
            self.accounts_frame,
            text=text,
            bg=color_schema.PRIMARY_CONTAINER,
            fg=color_schema.ON_PRIMARY_CONTAINER,
            activebackground=color_schema.PRIMARY_FIXED_DIM,
            width=12,
            height=6,
            font=("Arial", 12, "bold"),
            relief="flat",
            command=lambda: self.select_account(text)
        )

        boton.grid(row=row, column=column, padx=40, pady=40)

    def select_account(self, text):
        messagebox.showinfo("Cuenta", f"Seleccionaste {text}")

    def add_account(self):
        from kit.ui.navigator import Navigator
        from views.account_editor_view import AccountEditorView
        from view_models.account_editor_view_model import AccountEditorViewModel
        Navigator.of(self).push(
            AccountEditorView(
                self.master,
                view_model=AccountEditorViewModel()
            )
        )

    def settings(self):
        messagebox.showinfo("Configuración", "Abrir configuración")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1024x768")
    root.title("Account Hub")

    app = AccountHubView(root)
    app.pack(fill="both", expand=True)

    root.mainloop()