from kit.ui.view import View
from view_models.account_dashboard_view_model import AccountDashboardViewModel
import tkinter as tk
from kit.ui.dispatcher import Dispatcher
from services.color_schema import color_schema
from views.account_home_view import AccountHomeView

class AccountDashboardView(View):
    vm: AccountDashboardViewModel

    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)
        # SIDE BAR
        self.side_bar = tk.Frame(self)
        self.body = Dispatcher(self)

        self.title = tk.Label(self.side_bar, font=("Arial", 24, "bold"), padx=10, pady=10)

        self.navs = [
            ("Inicio", lambda: AccountHomeView(self.body)),
            ("Ingresos", lambda: tk.Frame(self.body)),
            ("Gastos", lambda: tk.Frame(self.body)),
            ("Análisis", lambda: tk.Frame(self.body)),
            ("Mi cuenta", lambda: tk.Frame(self.body)),
        ]
        self.nav_buttons = [
            tk.Button(self.side_bar, text=label, cursor="hand2")
            for label, builder in self.navs
        ]
        self.nav_buttons.append(
            tk.Button(
                self.side_bar,
                text="Regresar <",
                command=self.master.pop,
                cursor="hand2",
            )
        )

        self.body.setup([builder for label, builder in self.navs])

        self.side_bar.pack(side=tk.LEFT, fill=tk.Y)
        self.title.pack()
        for nb in self.nav_buttons:
            nb.config(font=("Arial", 16, "bold"))
            nb.pack(fill=tk.X, padx=5, pady=2)
        self.body.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.update()

    def on_update(self, changed):
        if changed("account.name"):
            self.title.config(text=self.vm.account.name)

        if changed("color_schema"):
            self.config(bg=color_schema.SURFACE)
            self.side_bar.config(bg=color_schema.SURFACE_CONTAINER_LOW)
            self.title.config(
                bg=color_schema.SURFACE_CONTAINER_LOW,
                fg=color_schema.ON_SURFACE,
            )
            for nb in self.nav_buttons:
                nb.config(
                    bg=color_schema.SURFACE_CONTAINER,
                    fg=color_schema.ON_SURFACE_VARIANT,
                    activebackground=color_schema.SURFACE_CONTAINER_HIGHEST,
                    activeforeground=color_schema.ON_SURFACE,
                )
            self.body.config(bg=color_schema.SURFACE)
