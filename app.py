import tkinter as tk
from kit.ui.navigator import Navigator
from views.account_hub_view import AccountHubView
from view_models.account_hub_view_model import AccountHubViewModel


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Myconta")
        self.root = Navigator(self)
        self.root.push(AccountHubView(self.root, view_model=AccountHubViewModel()))
        self.root.pack(fill="both", expand=True)
