from kit.ui.view import View
from services.color_schema import color_schema
import tkinter as tk
from tkinter import messagebox

class AccountHubView(View):
    
    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)
        
        self.topbar = tk.Frame(self)
        self.topbar.pack(fill="x")

        self.titulo = tk.Label(
            self.topbar,
            text="Elige una cuenta",
            font=("Arial", 16, "bold")
        )
        self.titulo.pack(side="left", padx=20, pady=10)

        self.boton_settings = tk.Button(
            self.topbar,
            text="⚙",
            font=("Arial", 24),
            borderwidth=0,
            command=self.settings
        )
        self.boton_settings.pack(side="right", pady=10)

        self.boton_mas = tk.Button(
            self.topbar,
            text="+",
            font=("Arial", 24, "bold"),
            borderwidth=0,
            command=self.add_account
        )
        self.boton_mas.pack(side="right", padx=10, pady=10)

        self.accounts_frame = tk.Frame(self)
        self.accounts_frame.pack(expand=True)

        self.account_buttons = []
        self.create_account("Cuenta 1", 0, 0)
        self.create_account("Cuenta 2", 0, 1)
        self.create_account("Cuenta 3", 0, 2)
        self.create_account("Cuenta 4", 0, 3)

        self.update("color_schema")

    def create_account(self, text, row, column):
        boton = tk.Button(
            self.accounts_frame,
            text=text,
            width=12,
            height=6,
            font=("Arial", 12, "bold"),
            relief="flat",
            command=lambda: self.select_account(text)
        )
        boton.grid(row=row, column=column, padx=40, pady=40)
        self.account_buttons.append(boton)

    def on_update(self, changed):
        if changed("color_schema"):
            self.config(bg=color_schema.SURFACE)
            self.topbar.config(bg=color_schema.SURFACE_CONTAINER)
            self.accounts_frame.config(bg=color_schema.SURFACE)
            
            self.titulo.config(
                bg=color_schema.SURFACE_CONTAINER,
                fg=color_schema.ON_SURFACE
            )
            
            self.boton_mas.config(
                fg=color_schema.ON_SURFACE_VARIANT,
                bg=color_schema.SURFACE_CONTAINER,
                activebackground=color_schema.SURFACE_CONTAINER_HIGH
            )
            
            self.boton_settings.config(
                fg=color_schema.ON_SURFACE_VARIANT,
                bg=color_schema.SURFACE_CONTAINER,
                activebackground=color_schema.SURFACE_CONTAINER_HIGH
            )

            for btn in self.account_buttons:
                btn.config(
                    bg=color_schema.PRIMARY_CONTAINER,
                    fg=color_schema.ON_PRIMARY_CONTAINER,
                    activebackground=color_schema.PRIMARY_FIXED_DIM
                )

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
        from kit.ui.navigator import Navigator
        from views.settings_view import SettingsView
        from view_models.settings_view_model import SettingsViewModel
        Navigator.of(self).push(
            SettingsView(
                self.master,
                view_model=SettingsViewModel()
            )
        )