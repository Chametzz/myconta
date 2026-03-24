import tkinter as tk
from typing import Callable, Optional

class ListView(tk.Frame):
    def __init__(
        self,
        master=None,
        item_count: int = 0,
        item_builder: Optional[Callable[[tk.Frame, int], tk.Frame]] = None,
        height=200,
        width=300,
        **kwargs
    ):
        super().__init__(master, **kwargs)
        
        self.item_count = item_count
        self.item_builder = item_builder

        self.canvas = tk.Canvas(self, height=height, width=width, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        self.container = tk.Frame(self.canvas)
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.container, anchor="nw")

        # Configuración de eventos
        self.container.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Layout
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # --- SOLUCIÓN AL BIND_ALL ---
        # Solo hacemos scroll si el mouse está sobre la lista
        self.canvas.bind("<Enter>", lambda _: self.canvas.bind_all("<MouseWheel>", self._on_mousewheel))
        self.canvas.bind("<Leave>", lambda _: self.canvas.unbind_all("<MouseWheel>"))

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def _on_mousewheel(self, event):
        # El scroll solo funciona si el canvas es más grande que la ventana
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def update_colors(self, bg_color):
        """Actualiza el fondo de todos los componentes de forma cohesiva."""
        self.configure(bg=bg_color)
        self.canvas.configure(bg=bg_color)
        self.container.configure(bg=bg_color)
        # Opcional: si usas ttk, podrías estilar la scrollbar aquí
        return self
    
    def build(self, item_count: int = None):
        if item_count is not None:
            self.item_count = item_count
        
        # Limpieza segura
        for child in self.container.winfo_children():
            child.destroy()
            
        if self.item_builder:
            for i in range(self.item_count):
                item = self.item_builder(self.container, i)
                if item:
                    item.pack(fill='x', padx=5, pady=2)
        
        # --- CRUCIAL: Actualizar el área de scroll después de construir ---
        self.container.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        return self