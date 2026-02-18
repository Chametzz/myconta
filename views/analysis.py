import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry # Requiere: pip install tkcalendar

class Analysis (tk.Frame):
    """ 
    Gestor analitico de los gastos,presupuestos y los gastos por categoria, mismo que incluye un calendario para una busqueda mas comoda 
    """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="white")
        
        # Estilo para los botones y elementos
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10))
        style.configure("TFrame", background="white")

        # --- TÍTULO PRINCIPAL ---
        self.lbl_titulo = tk.Label(
            self, text="Análisis de mis finanzas", 
            font=("Arial", 18, "bold"), bg="white", fg="#333"
        )
        self.lbl_titulo.pack(pady=(10, 20), anchor="w", padx=20)

        # --- FRAME BÚSQUEDA (CON CALENDARIO) ---
        self.frame_busqueda = tk.Frame(self, bg="white", highlightbackground="#ccc", highlightthickness=1)
        self.frame_busqueda.pack(fill="x", padx=20, pady=10)

        tk.Label(self.frame_busqueda, text="Busquemos una fecha...", bg="white", font=("Arial", 10)).pack(side="left", padx=10, pady=10)
        
        # Calendario desplegable (DateEntry)
        # Este componente incluye las flechas laterales para cambiar de mes automáticamente
        self.cal = DateEntry(self.frame_busqueda, width=12, background='darkblue',
                             foreground='white', borderwidth=2, locale='es_ES')
        self.cal.pack(side="left", padx=10)

        self.btn_lupa = tk.Button(self.frame_busqueda, text="Q", font=("Arial", 10, "bold"), 
                                  bg="#f0f0f0", width=3, relief="groove")
        self.btn_lupa.pack(side="right", padx=10)

        # --- PANELES CENTRALES ---
        # Panel 1: Gastos VS Presupuestos
        self.panel_presupuestos = tk.LabelFrame(
            self, text="Gastos VS Presupuestos", font=("Arial", 12, "bold"),
            bg="white", relief="solid", bd=1, labelanchor="n"
        )
        self.panel_presupuestos.pack(fill="both", expand=True, padx=20, pady=10)
        
        tk.Label(self.panel_presupuestos,font=("Arial", 10, "underline"), bg="white").pack(anchor="w", padx=10, pady=5)
        tk.Label(self.panel_presupuestos, text="[Área de Gráfico]", fg="grey", bg="white").pack(expand=True)

        # Panel 2: Gastos por Categoría
        self.panel_categorias = tk.LabelFrame(
            self, text="Gastos por categoría", font=("Arial", 12, "bold"),
            bg="white", relief="solid", bd=1, labelanchor="n"
        )
        self.panel_categorias.pack(fill="both", expand=True, padx=20, pady=10)
        tk.Label(self.panel_categorias, text="[Área de Gráfico]", fg="grey", bg="white").pack(expand=True)

        # --- SECCIÓN INFERIOR (FOOTER) ---
        self.frame_footer = tk.Frame(self, bg="white")
        self.frame_footer.pack(fill="x", padx=20, pady=(10, 20))

        # Contenedor para el botón de descarga y la flecha
        self.cont_descarga = tk.Frame(self.frame_footer, bg="white")
        self.cont_descarga.pack(side="left")

        self.btn_descargar = tk.Button(
            self.cont_descarga, text="Descargar Balance", 
            font=("Arial", 11), bg="#f9f9f9", relief="solid", bd=1, padx=20, pady=5
        )
        self.btn_descargar.pack()

        # Recuadro PDF a la derecha
        self.frame_pdf = tk.Frame(self.frame_footer, highlightbackground="#ccc", highlightthickness=1, bg="white", padx=10, pady=10)
        self.frame_pdf.pack(side="right")
        
        tk.Label(self.frame_pdf, text="Descargar Balance\ncomo PDF?", 
                 font=("Arial", 10), bg="white", justify="center").pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MyConta - Análisis Financiero")
    root.geometry("550x700")
    root.configure(bg="white")
    
    app = Analysis(root)
    app.pack(fill="both", expand=True)
    
    root.mainloop()