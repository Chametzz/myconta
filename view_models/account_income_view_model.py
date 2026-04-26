from kit.view_model import ViewModel
import tkinter as tk
from models.account import Account
from decimal import Decimal
import datetime
from repositories.transaction_repository import TransactionRepository
from utils.formatters import format_money
import calendar


class AccountIncomeViewModel(ViewModel):
    def __init__(self, account: Account):
        super().__init__()
        self.account = account

        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.monthly_period_text = tk.StringVar(value="")

        self.monthly_income = Decimal("0.00")
        self.monthly_income_text = tk.StringVar(value="")

    def update_monthly_data(self):
        self.monthly_income = TransactionRepository.get_monthly_sum(
            self.account.id, self.month, self.year, True, False
        )
        self.monthly_period_text.set(
            f"{calendar.month_name[self.month].capitalize()} {self.year}"
        )

    def update_monthly_text(self):
        self.monthly_income_text.set(
            format_money(self.monthly_income, self.account.currency)
        )

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.update_monthly_data()

    def prev_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.update_monthly_data()
