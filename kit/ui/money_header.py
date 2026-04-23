import tkinter as tk
from services.color_schema import color_schema
from typing import Callable

class MoneyHeader(tk.Frame):
    def __init__(
        self,
        master=None,
        balance_var: tk.StringVar = None,
        period_var: tk.StringVar = None,
        on_tap_prev: Callable[[], None] = None,
        on_tap_next: Callable[[], None] = None,
    ):
        super().__init__(master)
        self.config(bg=color_schema.SURFACE_CONTAINER, pady=20)
        
        # Configuramos pesos de columnas para que el centro se expanda
        self.columnconfigure(1, weight=1)

        # 1. SALDO TOTAL (Arriba, abarcando todas las columnas)
        self.lbl_balance = tk.Label(
            self,
            textvariable=balance_var, # Vinculación reactiva
            font=("Arial", 28, "bold"),
            bg=color_schema.SURFACE_CONTAINER,
            fg=color_schema.ON_SURFACE
        )
        # Columnspan=3 para que ocupe el ancho de los botones + periodo
        self.lbl_balance.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # 2. BOTÓN ANTERIOR
        self.prev_button = tk.Button(
            self,
            text="<",
            font=("Arial", 18, "bold"),
            bg=color_schema.SURFACE_CONTAINER,
            fg=color_schema.ON_SURFACE,
            activebackground=color_schema.SURFACE_CONTAINER_HIGH,
            borderwidth=0,
            command=on_tap_prev,
            cursor="hand2"
        )
        self.prev_button.grid(row=1, column=0, padx=20)

        # 3. MES Y AÑO (En medio de los botones)
        self.lbl_period = tk.Label(
            self,
            textvariable=period_var, # Vinculación reactiva
            font=("Arial", 14),
            bg=color_schema.SURFACE_CONTAINER,
            fg=color_schema.ON_SURFACE_VARIANT
        )
        self.lbl_period.grid(row=1, column=1)

        # 4. BOTÓN SIGUIENTE
        self.next_button = tk.Button(
            self,
            text=">",
            font=("Arial", 18, "bold"),
            bg=color_schema.SURFACE_CONTAINER,
            fg=color_schema.ON_SURFACE,
            activebackground=color_schema.SURFACE_CONTAINER_HIGH,
            borderwidth=0,
            command=on_tap_next,
            cursor="hand2"
        )
        self.next_button.grid(row=1, column=2, padx=20)