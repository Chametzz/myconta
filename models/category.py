import peewee as pw
from kit.model_fields.enum_field import EnumField
from kit.enums.category_type import CategoryType
from services.database import db

class Category(pw.Model):
    """
    Modelo Category

    Representa una categoría utilizada para clasificar movimientos
    financieros y generar reportes estadísticos (por ejemplo: Comida,
    Transporte, Entretenimiento).

    Attributos:
        id (AutoField): Clave primaria única. Identificador autoincremental.
        name (CharField): Nombre de la categoría. Debe ser único.
        type (EnumField): Tipo de la categoría, para saber a que tipo de transacción clasifica
    """

    id = pw.AutoField()
    name = pw.CharField(unique=True)
    type = EnumField(enum_class=CategoryType, max_length=10)
 
    class Meta:
        database = db  # Vincula el modelo con la conexión a la base de datos
