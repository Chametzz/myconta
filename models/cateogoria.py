import peewee as pw
from services.database import db


class Categoria(pw.Model):
    """
    Modelo Categoria

    Representa una categoría utilizada para clasificar movimientos
    financieros y generar reportes estadísticos (por ejemplo: Comida,
    Transporte, Entretenimiento).

    Attributos:
        id (AutoField): Clave primaria única. Identificador autoincremental.
        name (CharField): Nombre de la categoría. Debe ser único.
        icon (CharField): Referencia al ícono usado en la interfaz gráfica.
    """

    id = pw.AutoField()
    name = pw.CharField(unique=True)
    icon = pw.CharField()
 
    class Meta:
        database = db  # Vincula el modelo con la conexión a la base de datos
