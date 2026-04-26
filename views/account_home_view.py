from kit.ui.view import View
import tkinter as tk
from services.color_schema import color_schema
from kit.ui.money_header import MoneyHeader
from view_models.account_home_view_model import AccountHomeViewModel


class AccountHomeView(View):
    vm: AccountHomeViewModel

    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)
        self.config(bg=color_schema.SURFACE)

        self.top_bar = tk.Frame(self, bg=color_schema.SURFACE_CONTAINER)
        self.top_bar.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(
            self.top_bar,
            text="Tu saldo mensual es",
            font=("Arial", 16, "bold"),
            fg=color_schema.ON_SURFACE,
            bg=color_schema.SURFACE_CONTAINER,
        )
        self.title_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.money_header = MoneyHeader(
            self,
            self.vm.monthly_balance_text,
            self.vm.monthly_period_text,
            self.vm.prev_month,
            self.vm.next_month,
        )
        self.money_header.pack(fill=tk.X)

        self.income_expense_container = tk.Frame(
            self, bg=color_schema.SURFACE_CONTAINER
        )
        self.income_expense_container.pack(fill=tk.X)

        self.income_frame = tk.Frame(
            self.income_expense_container, bg=color_schema.SURFACE_CONTAINER_LOWEST
        )
        self.income_frame.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.X)

        self.income_label = tk.Label(
            self.income_frame,
            text="Ingresos",
            bg=color_schema.SURFACE_CONTAINER_LOWEST,
            fg=color_schema.ON_SURFACE,
            font=("Arial", 14, "bold"),
        )
        self.income_label.pack(anchor=tk.W, padx=15)

        self.income_data = tk.Label(
            self.income_frame,
            textvariable=self.vm.monthly_income_text,
            bg=color_schema.SURFACE_CONTAINER_LOWEST,
            fg=color_schema.ON_SURFACE,
            font=("Arial", 28, "bold"),
        )
        self.income_data.pack(anchor=tk.W, padx=15)

        self.expense_frame = tk.Frame(
            self.income_expense_container, bg=color_schema.SURFACE_CONTAINER_LOWEST
        )
        self.expense_frame.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.X)

        self.expense_label = tk.Label(
            self.expense_frame,
            text="Gastos",
            bg=color_schema.SURFACE_CONTAINER_LOWEST,
            fg=color_schema.ON_SURFACE,
            font=("Arial", 14, "bold"),
        )
        self.expense_label.pack(anchor=tk.W, padx=15)

        self.expense_data = tk.Label(
            self.expense_frame,
            textvariable=self.vm.monthly_expense_text,
            bg=color_schema.SURFACE_CONTAINER_LOWEST,
            fg=color_schema.ON_SURFACE,
            font=("Arial", 28, "bold"),
        )
        self.expense_data.pack(anchor=tk.W, padx=15)

        self.balance_footer_container = tk.Frame(self, bg=color_schema.SURFACE)
        self.balance_footer_container.pack(expand=True, fill=tk.BOTH)

        self.inner_balance_group = tk.Frame(
            self.balance_footer_container, bg=color_schema.SURFACE
        )
        self.inner_balance_group.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.current_balance_label = tk.Label(
            self.inner_balance_group,
            text="Tu saldo actual es",
            bg=color_schema.SURFACE,
            fg=color_schema.ON_SURFACE,
            font=("Arial", 14, "bold"),
        )
        self.current_balance_label.pack(side=tk.TOP)

        self.current_balance_data = tk.Label(
            self.inner_balance_group,
            textvariable=self.vm.current_balance_text,
            bg=color_schema.SURFACE,
            fg=color_schema.ON_SURFACE,
            font=("Arial", 28, "bold"),
        )
        self.current_balance_data.pack(side=tk.TOP)
