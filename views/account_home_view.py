from kit.ui.view import View
import tkinter as tk
from services.color_schema import color_schema


class AccountHomeView(View):
    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)
        self.config(bg=color_schema.SURFACE)
        self.top_bar = tk.Frame(self, bg=color_schema.SURFACE_CONTAINER)
        self.top_bar.pack(side=tk.TOP, fill=tk.X)
        self.title_label = tk.Label(
            self.top_bar,
            text="Tu saldo mensual es",
            font=("Arial", 16, "bold"),
            fg=color_schema.ON_SURFACE,
            bg=color_schema.SURFACE_CONTAINER,
        )
        self.title_label.pack(side=tk.LEFT, padx=10, pady=10)
