from enum import Enum
import winreg
from typing import Optional, cast
from dataclasses import dataclass


@dataclass
class ColorSchema:
    """
    Representa un conjunto completo de colores basado en Material Design 3.
    Se utiliza para definir paletas tanto claras como oscuras.
    """
    # Primary
    PRIMARY: str
    ON_PRIMARY: str
    PRIMARY_CONTAINER: str
    ON_PRIMARY_CONTAINER: str
    PRIMARY_FIXED: str
    PRIMARY_FIXED_DIM: str
    ON_PRIMARY_FIXED: str
    ON_PRIMARY_FIXED_VARIANT: str
    
    # Secondary
    SECONDARY: str
    ON_SECONDARY: str
    SECONDARY_CONTAINER: str
    ON_SECONDARY_CONTAINER: str
    SECONDARY_FIXED: str
    SECONDARY_FIXED_DIM: str
    ON_SECONDARY_FIXED: str
    ON_SECONDARY_FIXED_VARIANT: str
    
    # Tertiary
    TERTIARY: str
    ON_TERTIARY: str
    TERTIARY_CONTAINER: str
    ON_TERTIARY_CONTAINER: str
    TERTIARY_FIXED: str
    TERTIARY_FIXED_DIM: str
    ON_TERTIARY_FIXED: str
    ON_TERTIARY_FIXED_VARIANT: str
    
    # Error
    ERROR: str
    ON_ERROR: str
    ERROR_CONTAINER: str
    ON_ERROR_CONTAINER: str
    
    # Surface
    SURFACE: str
    ON_SURFACE: str
    SURFACE_DIM: str
    SURFACE_BRIGHT: str
    SURFACE_CONTAINER_LOWEST: str
    SURFACE_CONTAINER_LOW: str
    SURFACE_CONTAINER: str
    SURFACE_CONTAINER_HIGH: str
    SURFACE_CONTAINER_HIGHEST: str
    ON_SURFACE_VARIANT: str
    
    # Utilities / Inverse
    OUTLINE: str
    OUTLINE_VARIANT: str
    INVERSE_SURFACE: str
    ON_INVERSE_SURFACE: str
    INVERSE_PRIMARY: str
    SHADOW: str
    SCRIM: str
    SURFACE_TINT: str


class ThemeMode(Enum):
    LIGHT = 'light'
    DARK = 'dark'
    SYSTEM = 'system'


LIGHT_SCHEMA = ColorSchema(
    PRIMARY="#32AE60",
    ON_PRIMARY="#FFFFFF",
    PRIMARY_CONTAINER="#A6F4B1",
    ON_PRIMARY_CONTAINER="#00210A",
    PRIMARY_FIXED="#A6F4B1",
    PRIMARY_FIXED_DIM="#8BD797",
    ON_PRIMARY_FIXED="#00210A",
    ON_PRIMARY_FIXED_VARIANT="#005221",
    SECONDARY="#526350",
    ON_SECONDARY="#FFFFFF",
    SECONDARY_CONTAINER="#D5E8CF",
    ON_SECONDARY_CONTAINER="#101F10",
    SECONDARY_FIXED="#D5E8CF",
    SECONDARY_FIXED_DIM="#B9CCB4",
    ON_SECONDARY_FIXED="#101F10",
    ON_SECONDARY_FIXED_VARIANT="#3B4B39",
    TERTIARY="#39656B",
    ON_TERTIARY="#FFFFFF",
    TERTIARY_CONTAINER="#BCEBF2",
    ON_TERTIARY_CONTAINER="#001F23",
    TERTIARY_FIXED="#BCEBF2",
    TERTIARY_FIXED_DIM="#A1CED5",
    ON_TERTIARY_FIXED="#001F23",
    ON_TERTIARY_FIXED_VARIANT="#1F4D53",
    ERROR="#BA1A1A",
    ON_ERROR="#FFFFFF",
    ERROR_CONTAINER="#FFDAD6",
    ON_ERROR_CONTAINER="#410002",
    SURFACE="#F7FBF2",
    ON_SURFACE="#181D17",
    SURFACE_DIM="#D8DCD3",
    SURFACE_BRIGHT="#F7FBF2",
    SURFACE_CONTAINER_LOWEST="#FFFFFF",
    SURFACE_CONTAINER_LOW="#F1F5EC",
    SURFACE_CONTAINER="#EBF0E7",
    SURFACE_CONTAINER_HIGH="#E5EAE1",
    SURFACE_CONTAINER_HIGHEST="#DFE4DB",
    ON_SURFACE_VARIANT="#424940",
    OUTLINE="#72796F",
    OUTLINE_VARIANT="#C2C9BD",
    INVERSE_SURFACE="#2D322B",
    ON_INVERSE_SURFACE="#EFF2E9",
    INVERSE_PRIMARY="#8BD797",
    SHADOW="#000000",
    SCRIM="#000000",
    SURFACE_TINT="#32AE60",
)

DARK_SCHEMA = ColorSchema(
    PRIMARY="#8BD797",
    ON_PRIMARY="#003914",
    PRIMARY_CONTAINER="#005221",
    ON_PRIMARY_CONTAINER="#A6F4B1",
    PRIMARY_FIXED="#A6F4B1",
    PRIMARY_FIXED_DIM="#8BD797",
    ON_PRIMARY_FIXED="#00210A",
    ON_PRIMARY_FIXED_VARIANT="#005221",
    SECONDARY="#B9CCB4",
    ON_SECONDARY="#253424",
    SECONDARY_CONTAINER="#3B4B39",
    ON_SECONDARY_CONTAINER="#D5E8CF",
    SECONDARY_FIXED="#D5E8CF",
    SECONDARY_FIXED_DIM="#B9CCB4",
    ON_SECONDARY_FIXED="#101F10",
    ON_SECONDARY_FIXED_VARIANT="#3B4B39",
    TERTIARY="#A1CED5",
    ON_TERTIARY="#00363C",
    TERTIARY_CONTAINER="#1F4D53",
    ON_TERTIARY_CONTAINER="#BCEBF2",
    TERTIARY_FIXED="#BCEBF2",
    TERTIARY_FIXED_DIM="#A1CED5",
    ON_TERTIARY_FIXED="#001F23",
    ON_TERTIARY_FIXED_VARIANT="#1F4D53",
    ERROR="#FFB4AB",
    ON_ERROR="#690005",
    ERROR_CONTAINER="#93000A",
    ON_ERROR_CONTAINER="#FFDAD6",
    SURFACE="#101510",
    ON_SURFACE="#E0E4DB",
    SURFACE_DIM="#101510",
    SURFACE_BRIGHT="#363A34",
    SURFACE_CONTAINER_LOWEST="#0B0F0B",
    SURFACE_CONTAINER_LOW="#181D17",
    SURFACE_CONTAINER="#1C211B",
    SURFACE_CONTAINER_HIGH="#272B25",
    SURFACE_CONTAINER_HIGHEST="#31362F",
    ON_SURFACE_VARIANT="#C2C9BD",
    OUTLINE="#8C9388",
    OUTLINE_VARIANT="#424940",
    INVERSE_SURFACE="#E0E4DB",
    ON_INVERSE_SURFACE="#2D322B",
    INVERSE_PRIMARY="#32AE60",
    SHADOW="#000000",
    SCRIM="#000000",
    SURFACE_TINT="#8BD797",
)


class _ColorSchemaManager:
    
    _instance: Optional['_ColorSchemaManager'] = None
    _theme_mode: ThemeMode = ThemeMode.SYSTEM
    _listeners = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def add_listener(self, callback):
        if callback not in self._listeners:
            self._listeners.append(callback)
    
    def remove_listener(self, callback):
        if callback in self._listeners:
            self._listeners.remove(callback)
    
    def _notify(self):
        """Avisa a todas las vistas que el color_schema cambió."""
        for callback in self._listeners:
            # Llamamos al update de la vista pasando "color_schema"
            callback("color_schema")
    @property
    def theme_mode(self) -> ThemeMode:
        return self._theme_mode
    
    @theme_mode.setter
    def theme_mode(self, value: ThemeMode):
        self._theme_mode = value
        self._notify()
    
    def get_current_schema(self) -> ColorSchema:
        if self._theme_mode == ThemeMode.LIGHT:
            return LIGHT_SCHEMA
        elif self._theme_mode == ThemeMode.DARK:
            return DARK_SCHEMA
        else: 
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
                )
                is_light, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                return LIGHT_SCHEMA if is_light else DARK_SCHEMA
            except Exception as e:
                print(f"Error al leer tema del sistema: {e}")
                return DARK_SCHEMA

_manager = _ColorSchemaManager()

def color_schema_add_listener(callback):
    _manager.add_listener(callback)

def color_schema_remove_listener(callback):
    _manager.remove_listener(callback)

def change_theme_mode(value: ThemeMode) -> None:
    _manager.theme_mode = value

#def change_theme_mode(value: ThemeMode) -> None:
#    _manager.theme_mode = value
#    global color_schema
#    color_schema = _manager.get_current_schema()

class _ColorSchemaProxy:
    def __getattr__(self, name: str) -> str:
        return getattr(_manager.get_current_schema(), name)
    
    def __getitem__(self, key: str) -> str:
        return getattr(_manager.get_current_schema(), key)


color_schema = cast(ColorSchema, _ColorSchemaProxy())

