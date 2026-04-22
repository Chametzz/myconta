import tkinter as tk
from services.color_schema import color_schema
from typing import List, Tuple, Callable

# Alias para mejorar la legibilidad del tipo complejo
ActionList = List[Tuple[str, Callable[[], None]]]

class AppBar(tk.Frame):
    def __init__(
        self,
        master=None,
        title: str = "",
        can_go_back: bool = False,
        actions: ActionList = None,
    ):
        # Heredamos de tk.Frame, este será el contenedor de la barra
        super().__init__(master, bg=color_schema.SURFACE_CONTAINER, height=64)
        self.pack_propagate(False) # Mantiene la altura fija de la barra
        
        # 1. Botón de Regreso (Izquierda)
        if can_go_back:
            self.back_button = tk.Button(
                self,
                text="←", # Usamos un símbolo más estándar
                font=("Arial", 18),
                borderwidth=0,
                bg=color_schema.SURFACE_CONTAINER,
                fg=color_schema.ON_SURFACE_VARIANT,
                activebackground=color_schema.SURFACE_CONTAINER_HIGH,
                padx=15,
                command=self._on_back_press,
                cursor="hand2",
            )
            self.back_button.pack(side=tk.LEFT, fill="y")

        # 2. Título (Izquierda, después del botón)
        self.title_label = tk.Label(
            self,
            text=title,
            font=("Arial", 16, "bold"),
            bg=color_schema.SURFACE_CONTAINER,
            fg=color_schema.ON_SURFACE,
        )
        self.title_label.pack(side=tk.LEFT, padx=15)

        # 3. Acciones (Derecha)
        if actions:
            for text, command in actions:
                btn = tk.Button(
                    self,
                    text=text,
                    font=("Arial", 20), # Ajustado para iconos o texto corto
                    borderwidth=0,
                    bg=color_schema.SURFACE_CONTAINER,
                    fg=color_schema.ON_SURFACE_VARIANT,
                    activebackground=color_schema.SURFACE_CONTAINER_HIGH,
                    command=command,
                    cursor="hand2",
                    padx=10
                )
                btn.pack(side=tk.RIGHT, fill="y", padx=5)

    def _on_back_press(self):
        """Lógica para regresar en el Navigator."""
        from kit.ui.navigator import Navigator
        Navigator.of(self).pop()