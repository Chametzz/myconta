import tkinter as tk
from core.ui.navigator import Navigator
from views.account_hub_view import AccountHubView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Myconta")
        self.root = Navigator(self)
        self.root.push(AccountHubView(self.root))
        self.root.pack(fill="both", expand=True)
