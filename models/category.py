import peewee as pw
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
    """

    id = pw.AutoField()
    name = pw.CharField(unique=True)
    type = pw.CharField()
 
    class Meta:
        database = db  # Vincula el modelo con la conexión a la base de datos
