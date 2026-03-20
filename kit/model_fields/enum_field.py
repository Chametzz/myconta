from peewee import CharField


class EnumField(CharField):
    def __init__(self, enum_class, max_length=..., *args, **kwargs):
        self.enum_class = enum_class
        super().__init__(max_length, *args, **kwargs)

    def db_value(self, value):
        """Prepara el valor para la base de datos"""
        if value is None:
            return None

        if isinstance(value, self.enum_class):
            return value.name

        return str(value)

    def python_value(self, value):
        """Convierte lo que viene de la DB al objeto Enum"""
        if value is None:
            return None

        try:
            return self.enum_class[value]
        except KeyError:
            return getattr(self.enum_class, "UNKNOWN", value)
