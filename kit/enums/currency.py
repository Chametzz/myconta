from enum import Enum


class Currency(Enum):
    ARS = ("Peso Argentino", "$")
    BOB = ("Boliviano", "Bs")
    CLP = ("Peso Chileno", "$")
    COP = ("Peso Colombiano", "$")
    CRC = ("Colón Costarricense", "₡")
    CUP = ("Peso Cubano", "$")
    DOP = ("Peso Dominicano", "$")
    EUR = ("Euro", "€")
    GTQ = ("Quetzal", "Q")
    HNL = ("Lempira", "L")
    MXN = ("Peso Mexicano", "$")
    NIO = ("Córdoba", "C$")
    PAB = ("Balboa", "B/.")
    PEN = ("Sol", "S/")
    PYG = ("Guaraní", "₲")
    USD = ("Dólar", "$")
    UYU = ("Peso Uruguayo", "$U")
    VES = ("Bolívar Soberano", "Bs.S")
    
    UNKNOWN = ("Desconocido", "?")
    
    def __init__(self, label, symbol):
        self.label = label
        self.symbol = symbol
