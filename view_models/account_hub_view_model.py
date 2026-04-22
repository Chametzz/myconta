from kit.view_model import ViewModel
from models.account import Account
from typing import List
class AccountHubViewModel(ViewModel):
    accounts : List[Account] = []
    def __init__(self):
        super().__init__()
        self.load_accounts()
        
    def load_accounts(self):
        self.accounts.clear()
        print("Cargando cuentas...")
        for acc in Account.select():
            self.accounts.append(acc)
            print(f"Account name: {acc.name}")
        self.notify("accounts")
        