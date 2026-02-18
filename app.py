import tkinter as tk
from views.principal import Principal

class App(tk.Tk) :
    def __init__(self):
        super().__init__()
        self.title('Myconta')
        self.root = Principal(self)
        self.root.pack(fill="both", expand=True)
