import tkinter as tk
from tkinter import ttk
from kit.ui.view import View
from view_models.settings_view_model import SettingsViewModel
class SettingsView(View):
    vm: SettingsViewModel
    def __init__(self, master, view_model=None, *args, **kwargs):
        super().__init__(master, view_model, *args, **kwargs)
        
        self.bg_color = "#f0eef5"
        self.fg_color = "black"

        # ===== Contenedor principal =====  
        self.container = tk.Frame(self, bg=self.bg_color)
        self.container.pack(fill="both", expand=True)

        # ===============================
        # BARRA SUPERIOR
        # ===============================
        header = tk.Frame(self.container, bg="#2f3b4c", height=60)
        header.pack(fill="x")

        header.grid_columnconfigure(1, weight=1)

        # 🔹 Botón regresar (AHORA IZQUIERDA)
        back_btn = tk.Button(
            header,
            text="← Regresar",
            bg="#ff5757",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.regresar
        )
        back_btn.grid(row=0, column=0, padx=15, pady=10, sticky="w")

        # 🔹 Título
        title = tk.Label(
            header,
            text="Configuración",
            font=("Arial", 18, "bold"),
            bg="#2f3b4c",
            fg="white"
        )
        title.grid(row=0, column=1, sticky="w", padx=10)

        # ===============================
        # CONTENIDO
        # ===============================

        # ===== Categorías =====
        cat_frame = tk.Frame(self.container, bg=self.bg_color)
        cat_frame.pack(fill="x", padx=20, pady=15)

        cat_label = tk.Label(
            cat_frame,
            text="Categorías",
            font=("Arial", 12, "bold"),
            bg="#2f3b4c",
            fg="white",
            padx=10,
            pady=5
        )
        cat_label.pack(fill="x")

        # ===== Modo de pantalla =====
        mode_frame = tk.Frame(self.container, bg=self.bg_color)
        mode_frame.pack(fill="x", padx=20, pady=10)

        mode_text = tk.Label(
            mode_frame,
            text="Modo de pantalla",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.fg_color
        )
        mode_text.pack(anchor="w")

        self.mode_var = tk.StringVar()

        self.mode_combo = ttk.Combobox(
            mode_frame,
            textvariable=self.mode_var,
            state="readonly",
            values=[key for key, value in self.vm.theme_mode_options.items()],
        )
        self.mode_combo.pack(fill="x", pady=5)
        self.mode_combo.current(0)
        self.mode_combo.bind('<<ComboboxSelected>>', self.on_select_theme_mode)
        # 🔹 BOTÓN GUARDAR
        save_btn = tk.Button(
            self.container,
            text="Guardar cambios",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.guardar_cambios
        )
        save_btn.pack(pady=20)
    def on_select_theme_mode(self, event=None):
        selected = self.mode_combo.get()
        self.vm.change_theme_mode(self.vm.theme_mode_options[selected])
    # ===============================
    # CAMBIAR TEMA
    # ===============================
    def aplicar_tema(self, modo):
        if modo == "Oscuro":
            self.bg_color = "#1e1e1e"
            self.fg_color = "white"
        else:
            self.bg_color = "#eef1f5"
            self.fg_color = "black"

        self.container.config(bg=self.bg_color)

        # actualizar todos los hijos
        for widget in self.container.winfo_children():
            try:
                widget.config(bg=self.bg_color, fg=self.fg_color)
            except:
                pass

    # ===============================
    # GUARDAR CAMBIOS
    # ===============================
    def guardar_cambios(self):
        modo = self.mode_var.get()
        self.aplicar_tema(modo)
        print(f"Tema cambiado a: {modo}")

    # ===============================
    # BOTÓN REGRESAR
    # ===============================
    def regresar(self):
        print("Regresando...")
        self.master.destroy()

    def on_enter(self):
        print("Entraste a Configuración")

    def on_exit(self):
        print("Saliste de Configuración")


# ===============================
# PRUEBA
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")

    settings = SettingsView(root)
    settings.pack(fill="both", expand=True)

    root.mainloop()