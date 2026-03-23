from models.app_config import AppConfig
from services.database import initialize_db

class AppService:
    def __init__(self):
        AppConfig().apply()
        initialize_db()