from kit.view_model import ViewModel
from models.account import Account

class AccountDashboardViewModel(ViewModel):
    def __init__(self, account : Account):
        super().__init__()
        self.account = account