from kit.view_model import ViewModel
from models.account import Account

class AccountHubViewModel(ViewModel):
    accounts = []
    acuerdo = False
    
    def load_accounts(self):
        self.accounts = Account.select()
        # CARGA LAS CUENTAS
        self.notify('accounts')
    
    def david(self):
        self.acuerdo = not self.acuerdo
        self.notify('david')
    
    def llamada(self):
        print("hola")