from kit.view_model import ViewModel
from models.account import Account
import datetime
import tkinter as tk

class AccountHomeViewModel(ViewModel):
    
    def __init__(self, account: Account):
        super().__init__()
        self.account = account
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        #self.income = self.account.get_monthly_income(self.month, self.year)
        self.balance_text = tk.StringVar(value="asdasd")
        self.period_text = tk.StringVar(value="asdad")