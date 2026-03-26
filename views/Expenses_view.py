import tkinter as tk
from tkinter import simpledialog, messagebox
from services.database import Expense, initialize


class GastosView(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#9e9e9e")

        initialize()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)

        self.create_header()
        self.create_panels()
        self.update_view()

    # ---------------- HEADER ----------------
    def create_header(self):
        header = tk.Frame(self, bg="#9e9e9e")
        header.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Label(
            header,
            text="Tus gastos",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="#9e9e9e"
        ).pack(side="left", padx=20, pady=10)

        tk.Button(
            header,
            text="+",
            font=("Arial", 18, "bold"),
            command=self.add_expense
        ).pack(side="right", padx=20)

        self.total_label = tk.Label(
            self,
            text="$0.00",
            font=("Arial", 28),
            fg="white",
            bg="#9e9e9e"
        )
        self.total_label.grid(row=1, column=0, columnspan=2, pady=10)

        tk.Label(
            self,
            text="Mes actual",
            font=("Arial", 14),
            fg="white",
            bg="#9e9e9e"
        ).grid(row=2, column=0, columnspan=2)

    # ---------------- PANELES ----------------
    def create_panels(self):

        # HISTORIAL
        self.history_frame = tk.Frame(self, bg="#cfcfcf")
        self.history_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        tk.Label(
            self.history_frame,
            text="Historial",
            font=("Arial", 16, "bold"),
            bg="#cfcfcf"
        ).pack(pady=5)

        self.history_container = tk.Frame(self.history_frame, bg="#cfcfcf")
        self.history_container.pack(fill="both", expand=True)

        # CATEGORÍAS
        self.category_frame = tk.Frame(self, bg="#cfcfcf")
        self.category_frame.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

        tk.Label(
            self.category_frame,
            text="Categorías",
            font=("Arial", 16, "bold"),
            bg="#cfcfcf"
        ).pack(pady=5)

        self.category_container = tk.Frame(self.category_frame, bg="#cfcfcf")
        self.category_container.pack(fill="both", expand=True)

    # ---------------- FUNCIONES ----------------

    def add_expense(self):
        concepto = simpledialog.askstring("Gasto", "Concepto:")
        if not concepto:
            return

        try:
            monto = float(simpledialog.askstring("Gasto", "Monto:"))
        except:
            messagebox.showerror("Error", "Monto inválido")
            return

        categoria = simpledialog.askstring("Gasto", "Categoría:")
        fecha = simpledialog.askstring("Gasto", "Fecha:")

        Expense.create(
            concepto=concepto,
            monto=monto,
            categoria=categoria,
            fecha=fecha
        )

        self.update_view()

    def update_view(self):

        # limpiar
        for w in self.history_container.winfo_children():
            w.destroy()

        for w in self.category_container.winfo_children():
            w.destroy()

        total = 0
        categorias = {}

        for gasto in Expense.select():
            total += gasto.monto

            # -------- HISTORIAL (tarjetas) --------
            card = tk.Frame(self.history_container, bg="#444", bd=1, relief="solid")
            card.pack(fill="x", padx=10, pady=5)

            tk.Label(card, text=gasto.concepto, bg="#444", fg="white").grid(row=0, column=0, sticky="w", padx=5)
            tk.Label(card, text=f"${gasto.monto}", bg="#444", fg="white").grid(row=0, column=1, padx=5)

            tk.Label(card, text=gasto.categoria, bg="#444", fg="white").grid(row=1, column=0, sticky="w", padx=5)
            tk.Label(card, text=gasto.fecha, bg="#444", fg="white").grid(row=1, column=1, padx=5)

            tk.Button(
                card,
                text="X",
                command=lambda id=gasto.id: self.delete_expense(id)
            ).grid(row=0, column=2, padx=5)

            # -------- CATEGORÍAS --------
            if gasto.categoria not in categorias:
                categorias[gasto.categoria] = 0

            categorias[gasto.categoria] += gasto.monto

        # mostrar categorías
        for cat, monto in categorias.items():
            cat_card = tk.Frame(self.category_container, bg="#444", bd=1, relief="solid")
            cat_card.pack(fill="x", padx=10, pady=5)

            tk.Label(cat_card, text=cat, bg="#444", fg="white").pack(side="left", padx=10)
            tk.Label(cat_card, text=f"${monto}", bg="#444", fg="white").pack(side="right", padx=10)

        self.total_label.config(text=f"${total:.2f}")

    def delete_expense(self, expense_id):
        Expense.delete_by_id(expense_id)
        self.update_view()


# TEST
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    app = GastosView(root)
    app.pack(fill="both", expand=True)

    root.mainloop()