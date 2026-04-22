import tkinter as tk
from tkinter import ttk
from kit.ui.view import View
from services.color_schema import color_schema
from view_models.account_editor_view_model import AccountEditorViewModel


class AccountEditorView(View):
    vm: AccountEditorViewModel

    def __init__(self, master, view_model=None):
        super().__init__(master, view_model)

        # --- AppBar (TopBar) ---
        self.top_bar = tk.Frame(self)
        self.top_bar.pack(fill="x")

        # Back Button
        self.back_button = tk.Button(
            self.top_bar,
            text="←",
            font=("Arial", 20),
            borderwidth=0,
            padx=15,
            command=lambda: self.master.pop(),
            cursor="hand2",
        )
        self.back_button.pack(side="left", pady=10)

        self.title_label = tk.Label(self.top_bar, font=("Arial", 16, "bold"))
        self.title_label.pack(side="left", padx=10, pady=10)

        # --- Form Container ---
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Name Field
        self.name_label = tk.Label(self.form_frame, text="Nombre", font=("Arial", 10))
        self.name_label.grid(row=0, column=0, sticky="w", pady=(10, 2))

        self.name_var = tk.StringVar()
        self.name_var.trace_add(
            "write", lambda *args: self.vm.change_account_name(self.name_var.get())
        )
        self.name_entry = tk.Entry(
            self.form_frame, width=35, relief="flat", textvariable=self.name_var
        )
        self.name_entry.grid(row=1, column=0, ipady=5, sticky="w")

        # Currency Field
        self.currency_label = tk.Label(
            self.form_frame, text="Divisa", font=("Arial", 10)
        )
        self.currency_label.grid(row=2, column=0, sticky="w", pady=(20, 2))

        self.currency_combo = ttk.Combobox(
            self.form_frame, values=self.vm.currency_options, state="readonly"
        )
        self.currency_combo.grid(row=3, column=0, sticky="w", ipady=3)

        def on_currency_selected(self, event):
            selected_str = self.currency_combo.get()

            from kit.enums.currency import Currency

            currency_enum = Currency[selected_str]

            self.vm.change_account_currency(currency_enum)

        self.currency_combo.bind("<<ComboboxSelected>>", on_currency_selected)

        # Save Button (Left Aligned)
        self.save_button = tk.Button(
            self.form_frame,
            text="Guardar",
            command=self.save_account,
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=25,
            pady=8,
            cursor="hand2",
        )
        self.save_button.grid(row=4, column=0, pady=40, sticky="w")

        self.update("color_schema", "title")

    def save_account(self):
        self.vm.save_account()
        self.master.pop()

    def on_update(self, changed):
        if changed("color_schema"):
            # Backgrounds
            self.config(bg=color_schema.SURFACE)
            self.form_frame.config(bg=color_schema.SURFACE)

            # AppBar and Navigation
            self.top_bar.config(bg=color_schema.SURFACE_CONTAINER)
            self.title_label.config(
                bg=color_schema.SURFACE_CONTAINER, fg=color_schema.ON_SURFACE
            )
            self.back_button.config(
                bg=color_schema.SURFACE_CONTAINER,
                fg=color_schema.ON_SURFACE_VARIANT,
                activebackground=color_schema.SURFACE_CONTAINER_HIGH,
            )

            # Labels and Fields
            label_style = {
                "bg": color_schema.SURFACE,
                "fg": color_schema.ON_SURFACE_VARIANT,
            }
            self.name_label.config(**label_style)
            self.currency_label.config(**label_style)

            # self.name_entry.config(
            #    bg=color_schema.SURFACE_CONTAINER_HIGHEST,
            #    fg=color_schema.ON_SURFACE,
            #    insertbackground=color_schema.PRIMARY
            # )

            # Save Button
            self.save_button.config(
                bg=color_schema.PRIMARY,
                fg=color_schema.ON_PRIMARY,
                activebackground=color_schema.PRIMARY_FIXED_DIM,
            )

        if changed("title"):
            view_title = (
                "Crear cuenta" if self.vm.account.id is None else "Editar cuenta"
            )
            self.title_label.config(text=view_title)
