import peewee as pw
from kit.enums.currency import Currency
from kit.model_fields.enum_field import EnumField
from services.database import db
from peewee import fn
from decimal import Decimal

class Account(pw.Model):
    """
    Representa una entidad financiera o fuente de dinero.

    Attributes:
            id (AutoField): Clave primaria única. Se genera automáticamente para
                identificar cada cuenta en la base de datos.
            name (CharField): Nombre de la cuenta.
            balance (DecimalField): El saldo actual disponible en la cuenta.
            currency (CharField): Código de moneda de la cuenta (Ej. 'MXN', 'USD').
                Sirve para gestionar transacciones en diferentes divisas.
            transactions (list[Transaction]): Colección de movimientos asociados.
                Este atributo es accesible gracias al backref definido en Transaction.
    """

    id = pw.AutoField()
    name = pw.CharField(default="")
    balance = pw.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    currency = EnumField(Currency, max_length=10, default=Currency.USD)

    class Meta:
        database = db

    def get_monthly_total_income(self, month: int, year: int):
        from models.transaction import Transaction
        query = (self.transactions
                 .select(fn.SUM(Transaction.amount))
                 .where(
                     (Transaction.amount > 0) &
                     (fn.strftime('%m', Transaction.date) == f"{month:02d}") &
                     (fn.strftime('%Y', Transaction.date) == str(year))
                 )
                 .scalar()) # Retorna directamente el valor numérico (o None)

        return Decimal(query or 0).quantize(Decimal("0.00"))
    
    def get_monthly_total_expense(self, month: int, year: int):
        from models.transaction import Transaction
        query = (self.transactions
                 .select(fn.SUM(Transaction.amount))
                 .where(
                     (Transaction.amount < 0) &
                     (fn.strftime('%m', Transaction.date) == f"{month:02d}") &
                     (fn.strftime('%Y', Transaction.date) == str(year))
                 )
                 .scalar()) # Retorna directamente el valor numérico (o None)

        return Decimal(query or 0).quantize(Decimal("0.00"))
