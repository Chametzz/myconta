from models.transaction import Transaction
from peewee import fn
from decimal import Decimal

class TransactionRepository:
    @staticmethod
    def get_monthly_sum(account_id, month: int, year: int, include_income: bool = True, include_expense: bool = True):
        """
        Calcula la suma de transacciones según los filtros.
        - Si ambos son True: Devuelve el balance neto del mes.
        - Si solo include_income es True: Devuelve el total de ingresos.
        - Si solo include_expense es True: Devuelve el total de gastos.
        """
        query = Transaction.select(fn.SUM(Transaction.amount)).where(
            (Transaction.account == account_id),
            (fn.strftime('%m', Transaction.date) == f"{month:02d}"),
            (fn.strftime('%Y', Transaction.date) == str(year))
        )

        # Aplicamos filtros dinámicos según los parámetros
        if include_income and not include_expense:
            query = query.where(Transaction.amount > 0)
        elif include_expense and not include_income:
            query = query.where(Transaction.amount < 0)
        # Si ambos son True, no filtramos por signo (da el neto)
        # Si ambos son False, técnicamente daría 0

        result = query.scalar()
        return Decimal(result or 0).quantize(Decimal("0.00"))