import tkinter as tk


class Navigator(tk.Frame):
    """
    Gestor de navegación basado en una pila (Stack).
    Instancia automáticamente las vistas asegurando la jerarquía de Tkinter.

    ```
    root = tk.Tk()
    nav = Navigator(root, HomeView)
    nav.pack(fill="both", expand=True)
    root.mainloop()
    ```
    """

    def __init__(
        self, master, initial_view, view_args=None, view_kwargs=None, *args, **kwargs
    ):
        """
        :param master: Widget padre donde se alojará el Navigator.
        :param initial_view: La clase de la primera vista que se debe mostrar.
        :param view_args: Lista o tupla de argumentos posicionales para la vista inicial.
        :param view_kwargs: Diccionario de argumentos nombrados para la vista inicial.
        :param args: Argumentos posicionales para el tk.Frame (Navigator).
        :param kwargs: Argumentos nombradas para el tk.Frame (Navigator) como fb, relief, etc.
        """
        super().__init__(master, *args, **kwargs)

        self.stack = []

        v_args = view_args if view_args else []
        v_kwargs = view_kwargs if view_kwargs else {}

        self.push(initial_view, *v_args, **v_kwargs)

    def push(self, view_class, *args, **kwargs):
        """
        Instancia una nueva vista, la agrega a la pila y la despliega.
        Llama a `on_exit()` en la vista que se oculta y a `on_enter()` en la nueva.

        ```
        nav = Navigator(root, HomeView)
        nav.pack(fill="both", expand=True)
        nav.push(SettingsView)
        ```

        :param view_class: La clase de la vista a instanciar.
        :param args/kwargs: Argumentos adicionales para el constructor de la vista.
        """

        if self.stack:
            if hasattr(self.stack[-1], "on_exit"):
                self.stack[-1].on_exit()
            self.stack[-1].pack_forget()

        try:
            new_view = view_class(self, *args, **kwargs)
        except TypeError as e:
            raise TypeError(f"Error al instanciar {view_class.__name__}. ") from e

        new_view.pack(fill="both", expand=True)
        self.stack.append(new_view)

        if hasattr(new_view, "on_enter"):
            new_view.on_enter()

    def pop(self):
        """
        Destruye la vista actual y restaura la anterior en la pila.
        Llama a `on_exit()` en la vista eliminada y a `on_enter` en la que reaparece.
        ```
        nav = Navigator(root, HomeView)
        nav.pack(fill="both", expand=True)
        nav.push(SettingsView)
        nav.pop()
        ```
        """
        if len(self.stack) > 1:
            view_to_remove = self.stack.pop()

            if hasattr(view_to_remove, "on_exit"):
                view_to_remove.on_exit()

            view_to_remove.destroy()

            previous_view = self.stack[-1]
            previous_view.pack(fill="both", expand=True)

            if hasattr(previous_view, "on_enter"):
                previous_view.on_enter()


# EJEMPLO
class _NavigatorPage(tk.Frame):
    """
    Clase de ejemplo para testear la navegación.
    Muestra cómo usar grid dentro de una vista y cómo llamar al Navigator.
    """
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master)
        # Usamos **kwargs para recibir 'num' y cualquier config de tk.Frame
        self.num = kwargs.get("num", 1)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.label = tk.Label(self, text=f"Página #{self.num}")
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.previous_page = tk.Button(
            self, text="<- Página anterior", command=self.change_to_previous_page
        )
        self.next_page = tk.Button(
            self, text="Página siguiente ->", command=self.change_to_next_page
        )

        if self.num > 1:
            self.previous_page.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
            self.next_page.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        else:
            self.next_page.grid(
                row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5
            )

    def on_enter(self):
        print(f"Entrando a la página #{self.num}")

    def on_exit(self):
        print(f"Saliendo de la página #{self.num}")

    def change_to_previous_page(self):
        self.master.pop()

    def change_to_next_page(self):
        self.master.push(_NavigatorPage, num=self.num + 1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Navigator")
    root.geometry("400x300")
    nav = Navigator(root, _NavigatorPage, num=1)
    nav.pack(fill="both", expand=True)
    root.mainloop()
