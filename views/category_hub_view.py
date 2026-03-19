import tkinter as tk
from kit.ui.view import View
from kit.color_schema import color_schema


class CategoryHubView(View):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg=color_schema.SURFACE)
        self.app_bar = tk.Frame(
            self, height=58, background=color_schema.SURFACE_CONTAINER
        )
        self.app_bar.pack(fill="x")
        self.back_button = tk.Button(
            self.app_bar,
            text="<-",
            font=("Arial", 24, "bold"),
            background=color_schema.SURFACE_CONTAINER,
            foreground=color_schema.ON_SURFACE_VARIANT,
            activebackground=color_schema.SURFACE_CONTAINER_HIGHEST,
            activeforeground=color_schema.ON_SURFACE,
            borderwidth=0,
        )
        self.back_button.pack(side="left")
        self.title = tk.Label(
            self.app_bar,
            text="Categorías",
            font=("Arial", 16, "bold"),
            background=color_schema.SURFACE_CONTAINER,
            foreground=color_schema.ON_SURFACE,
        )
        self.title.pack(side="left")
        self.add_button = tk.Button(
            self.app_bar,
            text=" + ",
            font=("Arial", 24, "bold"),
            background=color_schema.SURFACE_CONTAINER,
            foreground=color_schema.ON_SURFACE_VARIANT,
            activebackground=color_schema.SURFACE_CONTAINER_HIGHEST,
            activeforeground=color_schema.ON_SURFACE,
            borderwidth=0,
        )
        self.add_button.pack(side="right")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("CategoryHub")
    root.geometry("400x300")
    category_hub = CategoryHubView(root)
    category_hub.pack(fill="both", expand=True)
    root.mainloop()
