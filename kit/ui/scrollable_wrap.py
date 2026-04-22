import tkinter as tk
from tkinter import ttk

class ScrollableWrap(tk.Frame):
    def __init__(self, master, **kwargs):
        # Extraemos el fondo inicial para que todo sea consistente desde el inicio
        bg_color = kwargs.get("bg", kwargs.get("background", "#ffffff"))
        super().__init__(master, **kwargs)
        
        # 1. Configuración del Canvas (el Viewport)
        self.canvas = tk.Canvas(self, highlightthickness=0, bg=bg_color)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        # 2. El Frame contenedor (donde van los botones/cuadritos)
        self.container = tk.Frame(self.canvas, bg=bg_color)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.container, anchor="nw")
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Layout
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # 3. Bindings corregidos
        self.container.bind("<Configure>", self._update_scroll_region)
        self.canvas.bind("<Configure>", self._on_resize)
        
        # Solo bindiar el MouseWheel cuando el ratón entra al widget
        self.bind('<Enter>', self._bind_mousewheel)
        self.bind('<Leave>', self._unbind_mousewheel)

    def _update_scroll_region(self, event):
        # Actualiza el área de desplazamiento al tamaño real del contenido
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_resize(self, event):
        # Forzamos que el contenedor interno mida lo mismo que el canvas para el wrap
        self.canvas.itemconfig(self.canvas_window, width=event.width)
        self.reflow()

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        # Soporte para Windows y macOS
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def reflow(self):
        """Reubica los hijos en un grid dinámico según el ancho disponible."""
        self.update_idletasks()
        width = self.canvas.winfo_width()
        if width <= 1: return
        
        # Ajusta column_width según el tamaño de tus cards (ancho + padding)
        column_width = 160 
        cols = max(1, width // column_width)
        
        for i, child in enumerate(self.container.winfo_children()):
            child.grid(row=i // cols, column=i % cols, padx=10, pady=10)

    def clear_items(self):
        """Limpia el contenedor para refrescar datos."""
        for widget in self.container.winfo_children():
            widget.destroy()
        self._update_scroll_region(None)

    def config(self, cnf=None, **kw):
        """Propaga el cambio de color de fondo a los elementos internos."""
        bg = kw.get("bg") or kw.get("background")
        if bg:
            self.canvas.config(bg=bg)
            self.container.config(bg=bg)
        return super().config(cnf, **kw)
    
    configure = config # Alias para consistencia