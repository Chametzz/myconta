import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
from decimal import Decimal

from services.database import initialize_db
from models.transaction import Transaction
from models.category import Category
from models.account import Account

from kit.enums.category_type import CategoryType
from services.color_schema import color_schema, color_schema_add_listener


class IncomeView(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        initialize_db()

        self.config(bg=color_schema.SURFACE)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)

        self.create_header()
        self.create_panels()

        color_schema_add_listener(self.on_theme_change)

        self.update_view()

    # ---------------- HEADER ----------------
    def create_header(self):
        header = tk.Frame(self, bg=color_schema.SURFACE_CONTAINER)
        header.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Label(
            header,
            text="Tus ingresos",
            font=("Arial", 22, "bold"),
            fg=color_schema.ON_SURFACE,
            bg=color_schema.SURFACE_CONTAINER
        ).pack(side="left", padx=20, pady=10)

        tk.Button(
            header,
            text="+",
            font=("Arial", 18, "bold"),
            bg=color_schema.PRIMARY,
            fg=color_schema.ON_PRIMARY,
            command=self.add_income
        ).pack(side="right", padx=20)

        self.total_label = tk.Label(
            self,
            text="$0.00",
            font=("Arial", 28, "bold"),
            fg=color_schema.PRIMARY,
            bg=color_schema.SURFACE
        )
        self.total_label.grid(row=1, column=0, columnspan=2, pady=10)

    # ---------------- PANELES ----------------
    def create_panels(self):

        # HISTORIAL
        self.history_container = tk.Frame(self, bg=color_schema.SURFACE_CONTAINER)
        self.history_container.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        # CATEGORÍAS
        self.category_container = tk.Frame(self, bg=color_schema.SURFACE_CONTAINER)
        self.category_container.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

    # ---------------- AGREGAR INGRESO ----------------

    def add_income(self):

        descripcion = simpledialog.askstring("Ingreso", "Descripción:")
        if not descripcion:
            return

        try:
            monto = Decimal(simpledialog.askstring("Ingreso", "Monto:"))
        except:
            messagebox.showerror("Error", "Monto inválido")
            return

        #  CUENTA
        cuentas = list(Account.select())
        if not cuentas:
            messagebox.showerror("Error", "No hay cuentas registradas")
            return

        cuenta = cuentas[0]  # luego puedes hacer selector

        # CATEGORÍA (SOLO INCOME)
        categorias = list(
            Category.select().where(Category.type == CategoryType.INCOME)
        )

        if not categorias:
            messagebox.showerror("Error", "No hay categorías de ingreso")
            return

        categoria = categorias[0]

        # CREAR TRANSACCIÓN
        Transaction.create(
            description=descripcion,
            amount=monto,
            account=cuenta,
            category=categoria,
            date=datetime.now()
        )

        # ACTUALIZAR BALANCE
        cuenta.balance += monto
        cuenta.save()

        self.update_view()

    # ---------------- ACTUALIZAR UI ----------------

    def update_view(self):

        for w in self.history_container.winfo_children():
            w.destroy()

        for w in self.category_container.winfo_children():
            w.destroy()

        total = 0
        categorias = {}

        ingresos = (
            Transaction
            .select()
            .join(Category)
            .where(Category.type == CategoryType.INCOME)
        )

        for ingreso in ingresos:
            total += float(ingreso.amount)

            # -------- CARD HISTORIAL --------
            card = tk.Frame(
                self.history_container,
                bg=color_schema.SURFACE_CONTAINER_HIGH,
                bd=1
            )
            card.pack(fill="x", padx=10, pady=5)

            tk.Label(card, text=ingreso.description,
                     bg=color_schema.SURFACE_CONTAINER_HIGH,
                     fg=color_schema.ON_SURFACE).pack(side="left", padx=5)

            tk.Label(card, text=f"${ingreso.amount}",
                     bg=color_schema.SURFACE_CONTAINER_HIGH,
                     fg=color_schema.ON_SURFACE).pack(side="right", padx=5)

            # -------- CATEGORÍAS --------
            cat_name = ingreso.category.name if ingreso.category else "Sin categoría"

            categorias[cat_name] = categorias.get(cat_name, 0) + float(ingreso.amount)

        # -------- PANEL CATEGORÍAS --------
        for cat, monto in categorias.items():
            frame = tk.Frame(self.category_container, bg=color_schema.SECONDARY_CONTAINER)
            frame.pack(fill="x", padx=10, pady=5)

            tk.Label(frame, text=cat,
                     bg=color_schema.SECONDARY_CONTAINER,
                     fg=color_schema.ON_SECONDARY_CONTAINER).pack(side="left", padx=5)

            tk.Label(frame, text=f"${monto}",
                     bg=color_schema.SECONDARY_CONTAINER,
                     fg=color_schema.ON_SECONDARY_CONTAINER).pack(side="right", padx=5)

        self.total_label.config(text=f"${total:.2f}")

    # ---------------- CAMBIO DE TEMA ----------------

    def on_theme_change(self, _):
        self.config(bg=color_schema.SURFACE)
        self.update_view()


# TEST
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    app = IncomeView(root)
    app.pack(fill="both", expand=True)

    root.mainloop()