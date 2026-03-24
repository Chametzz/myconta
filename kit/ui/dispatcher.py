from tkinter import Frame
from typing import Callable, List, Optional


class Dispatcher(Frame):
    views: List[Frame] = []

    def __init__(self, master=None):
        super().__init__(master)
        self.index: int = 0
        self.builders: List[Callable[[], Frame]] = []
        self.views: List[Optional[Frame]] = []

    def setup(self, builders: List[Callable[[], Frame]], initial_index=0):
        if not builders:
            return
        self.builders = builders
        self.views = [None for _ in self.builders]
        self.safe_start = initial_index if 0 <= initial_index < len(builders) else 0
        self.dispatch(self.safe_start)

    def dispatch(self, index):
        if not self.builders or not (0 <= index < len(self.builders)):
            return

        if self.views[self.index] is not None:
            self.views[self.index].pack_forget()

        self.index = index
        if self.views[index] is None:
            self.views[index] = self.builders[index]()
            self.views[index].pack_propagate(False)

        self.views[index].pack(fill="both", expand=True)
