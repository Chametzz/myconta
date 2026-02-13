from peewee import SqliteDatabase
from models.account import Account
from models.transaction import Transaction

db = SqliteDatabase('database.db')
"""Base de datos"""

def initialize_db():
    """
    Configura la conexión y crea las tablas si no existen
    """
    if db.is_closed():
        db.connect()
    db.create_tables([Account, Transaction], safe=True)