# Models
Esta sección describe los modelos de datos.

## ORM (Object-Relational Mapping o Mapeo Objeto-Relacional): Peewee
Para interactuar con la base de datos (SQLite), utilizamos [Peewee](https://docs.peewee-orm.com/en/latest/), un ORM ligero para Python.

**¿Qué hace Peewee?**
* Permite definir tablas como clases de Python.
* Evita escribir SQL manualmente para operaciones comunes.

> [!TIP]
> Para trabajar con estos modelos, es importante conocer el funcionamiento de las consultas en [Peewee](https://docs.peewee-orm.com/en/latest/). Puedes consultar la [Guía Rápida de Peewee](https://docs.peewee-orm.com/en/latest/peewee/quickstart.html#querying) para aprender a buscar, filtrar y ordenar registros de los modelos.

## Implementación de modelos
Para mantener la coherencia en la base de datos y el funcionamiento del ORM, todos los modelos deben implementarse siguiendo estrictamente las siguientes indicaciones:

### Requisitos de definición
Cada clase de modelo debe heredar de `pw.Model` y vincularse a la base de datos mediante una clase interna `Meta`, asignando la instancia de `db` (importada desde `services.database`) al atributo database.

> [!IMPORTANT]
> **Documentación obligatoria**: Para asegurar la legibilidad del código, es necesario explicar qué representa el modelo y listar detalladamente sus atributos dentro del *docstring* de la clase.

```python
import peewee as pw
from services.database import db

class MyNewModel(pw.Model):
    """
    Descripción breve del modelo
    Attributes:
        campo1 (Tipo): Descripción del uso
        campo2 (Tipo): Descripción del uso
    """

    class Meta:
            database = db  # Vincula el modelo con la conexión a la base de datos
```
### Estándar de Campos y Tipos
Utilizamos los siguientes tipos de datos de Peewee para asegurar la integridad de la información y la consistencia en la base de datos:

#### Identificadores y Texto
* **Llave Primaria:** Usa siempre `pw.AutoField()`. Se encarga de crear un identificador único, entero y autoincremental para cada registro.
* **Texto Corto:** Usa `pw.CharField()`. Ideal para nombres, títulos o categorías (máximo 255 caracteres por defecto).
* **Texto Largo:** Usa `pw.TextField()`. Utilízalo para notas, comentarios extensos o descripciones que puedan superar un párrafo.

#### Números y Finanzas
* **Dinero (Obligatorio):** Usar `pw.DecimalField(max_digits=10, decimal_places=2)`. **Nunca uses FloatField** para valores monetarios, ya que los errores de redondeo binario pueden causar descuadres en las cuentas.
* **Números Enteros:** Usa `pw.IntegerField()` para contadores o valores que no requieran decimales.
* **Valores Booleanos:** Usa `pw.BooleanField()` para estados tipo Sí/No (ej. `is_active`, `is_verified`).

#### Fechas y Relaciones
* **Fechas y Tiempo:** Usa `pw.DateTimeField()`. Es recomendable pasar `default=datetime.datetime.now` para registrar automáticamente el momento de creación.
* **Relaciones (FK):** Usa `pw.ForeignKeyField(ModeloPadre, backref='nombre_plural', on_delete='CASCADE')`.
    * **Backref:** El nombre debe ser en plural (ej. `transactions`), ya que representa la colección de objetos relacionados que "viven" en el modelo padre.
    * **Integridad:** Define siempre el comportamiento de borrado (`on_delete`).



#### Configuración de Atributos (Constraints)
Para mejorar la calidad de los datos, utiliza estos parámetros adicionales cuando sea necesario:
* `null=False`: Para campos obligatorios (valor por defecto en Peewee).
* `unique=True`: Para campos que no deben repetirse (ej. nombre de una cuenta única).
* `default=valor`: Para asignar un valor automático si no se proporciona uno.