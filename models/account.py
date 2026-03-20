import peewee as pw
from kit.enums.currency import Currency
from kit.model_fields.enum_field import EnumField
from services.database import db


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
    name = pw.CharField()
    balance = pw.DecimalField(max_digits=20, decimal_places=2)
    currency = EnumField(Currency, max_length=10)

    class Meta:
        database = db
