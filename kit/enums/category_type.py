from enum import Enum


class CategoryType(Enum):
    INCOME = "ingreso"
    EXPENSE = "gasto"

    UNKNOWN = "desconocido"

    def __init__(self, label):
        self.label: str = label
