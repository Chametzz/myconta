from decimal import Decimal
from kit.enums.currency import Currency

def format_money(amount: Decimal, currency: Currency) -> str:
    """
    Convierte un valor numérico en una representación visual financiera.
    Ejemplo: 1500.5 -> "$1,500.50MXN"
    """
    value_formatted = f"{amount:,.2f}"
    return f"{currency.symbol}{value_formatted} {currency.name}"
    