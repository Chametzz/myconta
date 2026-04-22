from kit.ui.view import View
from services.color_schema import color_schema
import tkinter as tk
from view_models.account_hub_view_model import AccountHubViewModel
from kit.ui.scrollable_wrap import ScrollableWrap
from view_models.account_dashboard_view_model import AccountDashboardViewModel
from views.account_dashboard_view import AccountDashboardView
from models.account import Account


class AccountHubView(View):
    vm: AccountHubViewModel

    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)

        self.topbar = tk.Frame(self)
        self.topbar.pack(fill="x")

        self.titulo = tk.Label(
            self.topbar, text="Elige una cuenta", font=("Arial", 16, "bold")
        )
        self.titulo.pack(side="left", padx=20, pady=10)

        self.boton_settings = tk.Button(
            self.topbar,
            text="⚙",
            font=("Arial", 24),
            borderwidth=0,
            command=self.go_to_settings,
            cursor="hand2",
        )
        self.boton_settings.pack(side="right", pady=10)

        self.boton_mas = tk.Button(
            self.topbar,
            text="+",
            font=("Arial", 24, "bold"),
            borderwidth=0,
            command=self.go_to_add_account,
            cursor="hand2",
        )
        self.boton_mas.pack(side="right", padx=10, pady=10)

        self.accounts_frame = ScrollableWrap(self)
        self.accounts_frame.pack(fill=tk.BOTH, expand=True)

        self.account_buttons = []

        self.update()

    def on_update(self, changed):
        if changed("color_schema"):
            self.config(bg=color_schema.SURFACE)
            self.topbar.config(bg=color_schema.SURFACE_CONTAINER)
            self.accounts_frame.config(bg=color_schema.SURFACE)

            self.titulo.config(
                bg=color_schema.SURFACE_CONTAINER, fg=color_schema.ON_SURFACE
            )

            self.boton_mas.config(
                fg=color_schema.ON_SURFACE_VARIANT,
                bg=color_schema.SURFACE_CONTAINER,
                activebackground=color_schema.SURFACE_CONTAINER_HIGH,
            )

            self.boton_settings.config(
                fg=color_schema.ON_SURFACE_VARIANT,
                bg=color_schema.SURFACE_CONTAINER,
                activebackground=color_schema.SURFACE_CONTAINER_HIGH,
            )

            for btn in self.account_buttons:
                btn.config(
                    bg=color_schema.PRIMARY_CONTAINER,
                    fg=color_schema.ON_PRIMARY_CONTAINER,
                    activebackground=color_schema.PRIMARY_FIXED_DIM,
                )

        if changed("accounts"):
            print("cambiaron las cuentas")
            self.accounts_frame.clear_items()
            self.account_buttons.clear()

            for acc in self.vm.accounts:
                btn = tk.Button(
                    self.accounts_frame.container,
                    text=f"{acc.name}",
                    width=16,
                    height=8,
                    font=("Arial", 12, "bold"),
                    relief="flat",
                    command=lambda a=acc: self.go_to_dashboard_account(account=a),
                    cursor="hand2",
                    bg=color_schema.PRIMARY_CONTAINER,
                    fg=color_schema.ON_PRIMARY_CONTAINER,
                    activebackground=color_schema.PRIMARY_FIXED_DIM,
                )
                self.account_buttons.append(btn)

            self.accounts_frame.reflow()

    def go_to_dashboard_account(self, account: Account):
        try:
            self.master.push(
                AccountDashboardView(
                    self.master, AccountDashboardViewModel(account=account)
                )
            )
        except:  # noqa: E722
            pass

    def go_to_add_account(self):
        from kit.ui.navigator import Navigator
        from views.account_editor_view import AccountEditorView
        from view_models.account_editor_view_model import AccountEditorViewModel

        Navigator.of(self).push(
            AccountEditorView(self.master, view_model=AccountEditorViewModel())
        )

    def go_to_settings(self):
        from kit.ui.navigator import Navigator
        from views.settings_view import SettingsView
        from view_models.settings_view_model import SettingsViewModel

        Navigator.of(self).push(
            SettingsView(self.master, view_model=SettingsViewModel())
        )

    def on_enter(self):
        self.vm.load_accounts()
