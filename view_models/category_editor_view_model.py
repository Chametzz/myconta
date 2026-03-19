from kit.view_model import ViewModel
from models.category import Category
from typing import Optional


class CategoryEditorViewModel(ViewModel):
    def __init__(self, category: Optional[Category] = None):
        super().__init__()

        if category is None:
            self.category = Category(name="", type="income")
        else:
            self.category = category
