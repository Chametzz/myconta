import json
import os
from services.color_schema import ThemeMode, change_theme_mode
from services.storage import Storage


class AppConfig:
    _file_name = "app_config.json"
    _allowed_keys = ["theme_mode"]
    
    @property
    def theme_mode(self):
        try:
            return ThemeMode[self._theme_mode]
        except (KeyError, AttributeError):
            return ThemeMode.SYSTEM
    
    @theme_mode.setter
    def theme_mode(self, value : ThemeMode):
        self._theme_mode = value.name

    def __init__(self):
        self._theme_mode = ThemeMode.SYSTEM.name
        
        full_path = os.path.join(Storage.directory, self._file_name)
        if os.path.exists(full_path):
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    
                    for key, value in data.items():
                        if key in self._allowed_keys:
                            internal_key = f"_{key}"
                            setattr(self, internal_key, value)
            except Exception as e:
                print(f"ERROR AL LEER CONFIGURACIÓN: {e}")                

    def save(self):
        full_path = os.path.join(Storage.directory, self._file_name)
        data = {key: getattr(self, f"_{key}") for key in self._allowed_keys}
        
        try:
            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error al guardar: {e}")
        finally:
            self.apply()
    
    def apply(self):
        print(self.theme_mode)
        change_theme_mode(self.theme_mode)
        print(self._theme_mode)
        print("Aplicando cambios")
            
