from models.app_config import AppConfig
from services.database import initialize_db
import locale

class AppService:
    def __init__(self):
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        AppConfig().apply()
        initialize_db()