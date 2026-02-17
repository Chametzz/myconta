import peewee as pw
from services.database import db
from models.account import Account
from models.category import  category


class Transaction(pw.Model):
    """
    Representa un movimiento financiero (ingreso o egreso).

    Attributes:
        id (AutoField): Identificador único autoincremental (Llave Primaria).
        account (ForeignKeyField): Referencia a la cuenta (Account) que realizó el movimiento.
        amount (DecimalField): Valor monetario de la operación.
        description (CharField): Breve resumen del movimiento.
        date (DateTimeField): Fecha y hora en la que se efectuó la operación.
    """

    id = pw.AutoField()
    account = pw.ForeignKeyField(Account, backref="transactions", on_delete="CASCADE")
    amount = pw.DecimalField(max_digits=20, decimal_places=2)
    description = pw.CharField()
    date = pw.DateTimeField()

    class Meta:
        database = db
       
        category = pw.ForeignKeyField(
        Category,
        backref='transactions',
        null=True,
        on_delete='SET NULL'
    )
