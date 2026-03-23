from kit.view_model import ViewModel
from models.app_config import AppConfig
from services.color_schema import ThemeMode

class SettingsViewModel(ViewModel):
    
    def __init__(self):
        super().__init__()
        self.app_config = AppConfig()
        self.theme_mode_options = {
            'Por defecto': ThemeMode.SYSTEM,
            'Claro': ThemeMode.LIGHT,
            'Oscuro': ThemeMode.DARK
        }
        
    def change_theme_mode(self, value: ThemeMode):
        self.app_config.theme_mode = value
        self.app_config.save()