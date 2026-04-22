from kit.view_model import ViewModel
from kit.enums.currency import Currency
from models.account import Account
import copy


class AccountEditorViewModel(ViewModel):
    def __init__(self, account: Account = None):
        super().__init__()
        if account is not None:
            self.account = copy.deepcopy(account)
        else:
            self.account = Account()
        self.currency_options = [c.name for c in Currency]
            

    def change_account_name(self, value: str):
        self.account.name = value

    def change_account_currency(self, value: Currency):
        self.account.currency = value

    def save_account(self):
        self.account.save()
