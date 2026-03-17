import tkinter as tk
from tkinter import messagebox

class SelectAccount(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#dcdcdc")

        self.create_topbar()

        self.accounts_frame = tk.Frame(self, bg="#dcdcdc")
        self.accounts_frame.pack(expand=True)

     
        self.create_account("Cuenta 1", 0, 0)
        self.create_account("Cuenta 2", 0, 1)
        self.create_account("Cuenta 3", 0, 2)
        self.create_account("Cuenta 4", 0, 3)


    def create_topbar(self):
        frame = tk.Frame(self, bg="#9e9e9e")
        frame.pack(fill="x")

        titulo = tk.Label(
            frame,
            text="Elige una cuenta",
            bg="#9e9e9e",
            fg="white",
            font=("Arial", 16, "bold")
        )
        titulo.pack(side="left", padx=20, pady=10)

        boton_mas = tk.Button(
            frame,
            text="+",
            font=("Arial", 14, "bold"),
            command=self.add_account
        )
        boton_mas.pack(side="right", padx=10, pady=10)

        boton_settings = tk.Button(
            frame,
            text="*",
            font=("Arial", 14),
            command=self.settings
        )
        boton_settings.pack(side="right", pady=10)


    def create_account(self, text, row, column):

        boton = tk.Button(
            self.accounts_frame,
            text="Cuenta",
            bg="black",
            fg="white",
            width=12,
            height=6,
            font=("Arial", 12),
            command=lambda: self.select_account(text)
        )

        boton.grid(row=row, column=column, padx=40, pady=40)


    def select_account(self, text):
        messagebox.showinfo("Cuenta", f"Seleccionaste {text}")


    def add_account(self):
        pass 


    def settings(self):
        messagebox.showinfo("Configuración", "Abrir configuración")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1024x780")
    app = SelectAccount(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
    #ajustar que la pantantalla se ajuste cuando se agrande o se minimize la pantalla y no se junte 
