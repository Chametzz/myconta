import tkinter as tk
from tkinter import messagebox

class MyAccount(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_option("Correo Electrónico")
        self.create_option("Mis cuentas")

        self.create_section("Descargas")
        self.create_option("Historial de Gastos e ingresos")

        self.create_section("Cuenta")
        self.create_option("Cerrar sesión")
        self.create_option("Cambiar de cuenta")
        self.create_option("Eliminar cuenta")


    def create_section(self, text):
        label = tk.Label(
            self,
            text=text,
            bg="#eaeaea",
            fg="blue",
            font=("Arial", 11, "bold")
        )
        label.pack(anchor="w", padx=20, pady=(15,5))
    
    def create_option(self, text):
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="x", padx=15, pady=2)## se crea un contenedor para que le boton y las flechas esten juntos 

        boton = tk.Button(
            frame,
            text=text,
            anchor="w",
            bg="white",
            relief="flat",
            padx=15,
            pady=12,
            font=("Arial", 11),
            command=lambda: self.action(text)#ejecuta el boton cuando se le da click 
        )
        boton.pack(side="left", fill="x", expand=True)

        flecha = tk.Label(
            frame,
            text=">",
            bg="white",
            fg="gray",
            font=("Arial", 12, "bold")
        ) 
        flecha.pack(side="right", padx=10)
        
    def action(self, text):
        messagebox.showinfo("Opción", f"Seleccionaste: {text}") # muestra una ventanita con el mensaje 
    
#Test
if __name__ == "__main__":
    root = tk.Tk()
    my_account = MyAccount(root)
    my_account.pack(fill="both", expand=True)
    root.mainloop()