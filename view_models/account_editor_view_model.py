from kit.view_model import ViewModel
from models.account import Account
class AccountEditorViewModel(ViewModel):
    account = Account(name = "", balance = 0,currency = "mxn")
    def __init__(self, account=None):
        super().__init__()
        if account is not None:
            self.account = account

    def change_account_name(self, value):
        pass
    def change_account_currency(self, value):
        pass
    def save_account(self):
        print('caca')
