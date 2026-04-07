from kit.view_model import ViewModel
from models.account import Account
import datetime

class AccountHomeViewModel(ViewModel):
    def __init__(self, account: Account):
        super().__init__()
        self.account = account
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.income = self.account.get_monthly_income(self.month, self.year)