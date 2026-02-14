import peewee as pw

db = pw.Proxy()


def initialize_db():
    """
    Configura la conexión y crea las tablas si no existen
    """
    db.initialize(pw.SqliteDatabase("database.db"))

    from models.account import Account
    from models.transaction import Transaction

    if db.is_closed():
        db.connect()
        
    db.create_tables([Account, Transaction], safe=True)