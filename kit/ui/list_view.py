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

        self.container.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_frame_configure(self, event):
        """Actualiza la región de scroll al tamaño del contenedor."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        """Hace que el ancho del contenedor interno siga al ancho del Canvas."""
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def _on_mousewheel(self, event):
        """Scroll con la rueda del ratón (Windows)."""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def update_colors(self, bg_color):
        """Actualiza el fondo de todos los componentes del scroll."""
        self.configure(bg=bg_color)
        self.canvas.configure(bg=bg_color)
        self.container.configure(bg=bg_color)
        return self
    
    def build(self):
        for child in self.container.winfo_children():
            child.destroy()
            
        if self.item_builder:
            for i in range(self.item_count):
                item = self.item_builder(self.container, i)
                if item:
                    item.pack(fill='x', padx=5, pady=2)
        
        return self