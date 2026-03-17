from enum import Enum
import winreg

class ColorSchema():
    """
    Representa un conjunto completo de colores basado en Material Design 3.
    Se utiliza para definir paletas tanto claras como oscuras.
    """
    light_schema = None
    dark_schema = None

    def __init__(
        self,
        primary,
        on_primary,
        primary_container,
        on_primary_container,
        primary_fixed,
        primary_fixed_dim,
        on_primary_fixed,
        on_primary_fixed_variant,
        secondary,
        on_secondary,
        secondary_container,
        on_secondary_container,
        secondary_fixed,
        secondary_fixed_dim,
        on_secondary_fixed,
        on_secondary_fixed_variant,
        tertiary,
        on_tertiary,
        tertiary_container,
        on_tertiary_container,
        tertiary_fixed,
        tertiary_fixed_dim,
        on_tertiary_fixed,
        on_tertiary_fixed_variant,
        error,
        on_error,
        error_container,
        on_error_container,
        surface,
        on_surface,
        surface_dim,
        surface_bright,
        surface_container_lowest,
        surface_container_low,
        surface_container,
        surface_container_high,
        surface_container_highest,
        on_surface_variant,
        outline,
        outline_variant,
        inverse_surface,
        on_inverse_surface,
        inverse_primary,
        shadow,
        scrim,
        surface_tint,
    ):
        # Primary
        self.PRIMARY = primary
        self.ON_PRIMARY = on_primary
        self.PRIMARY_CONTAINER = primary_container
        self.ON_PRIMARY_CONTAINER = on_primary_container
        self.PRIMARY_FIXED = primary_fixed
        self.PRIMARY_FIXED_DIM = primary_fixed_dim
        self.ON_PRIMARY_FIXED = on_primary_fixed
        self.ON_PRIMARY_FIXED_VARIANT = on_primary_fixed_variant

        # Secondary
        self.SECONDARY = secondary
        self.ON_SECONDARY = on_secondary
        self.SECONDARY_CONTAINER = secondary_container
        self.ON_SECONDARY_CONTAINER = on_secondary_container
        self.SECONDARY_FIXED = secondary_fixed
        self.SECONDARY_FIXED_DIM = secondary_fixed_dim
        self.ON_SECONDARY_FIXED = on_secondary_fixed
        self.ON_SECONDARY_FIXED_VARIANT = on_secondary_fixed_variant

        # Tertiary
        self.TERTIARY = tertiary
        self.ON_TERTIARY = on_tertiary
        self.TERTIARY_CONTAINER = tertiary_container
        self.ON_TERTIARY_CONTAINER = on_tertiary_container
        self.TERTIARY_FIXED = tertiary_fixed
        self.TERTIARY_FIXED_DIM = tertiary_fixed_dim
        self.ON_TERTIARY_FIXED = on_tertiary_fixed
        self.ON_TERTIARY_FIXED_VARIANT = on_tertiary_fixed_variant

        # Error
        self.ERROR = error
        self.ON_ERROR = on_error
        self.ERROR_CONTAINER = error_container
        self.ON_ERROR_CONTAINER = on_error_container

        # Surface
        self.SURFACE = surface
        self.ON_SURFACE = on_surface
        self.SURFACE_DIM = surface_dim
        self.SURFACE_BRIGHT = surface_bright
        self.SURFACE_CONTAINER_LOWEST = surface_container_lowest
        self.SURFACE_CONTAINER_LOW = surface_container_low
        self.SURFACE_CONTAINER = surface_container
        self.SURFACE_CONTAINER_HIGH = surface_container_high
        self.SURFACE_CONTAINER_HIGHEST = surface_container_highest
        self.ON_SURFACE_VARIANT = on_surface_variant

        # Utilities / Inverse
        self.OUTLINE = outline
        self.OUTLINE_VARIANT = outline_variant
        self.INVERSE_SURFACE = inverse_surface
        self.ON_INVERSE_SURFACE = on_inverse_surface
        self.INVERSE_PRIMARY = inverse_primary
        self.SHADOW = shadow
        self.SCRIM = scrim
        self.SURFACE_TINT = surface_tint

class ThemeMode(Enum):
    LIGHT = 'light'
    DARK = 'dark'
    SYSTEM = 'system'

light_schema = ColorSchema(
    primary="#32AE60",
    on_primary="#FFFFFF",
    primary_container="#A6F4B1",
    on_primary_container="#00210A",
    primary_fixed="#A6F4B1",
    primary_fixed_dim="#8BD797",
    on_primary_fixed="#00210A",
    on_primary_fixed_variant="#005221",
    secondary="#526350",
    on_secondary="#FFFFFF",
    secondary_container="#D5E8CF",
    on_secondary_container="#101F10",
    secondary_fixed="#D5E8CF",
    secondary_fixed_dim="#B9CCB4",
    on_secondary_fixed="#101F10",
    on_secondary_fixed_variant="#3B4B39",
    tertiary="#39656B",
    on_tertiary="#FFFFFF",
    tertiary_container="#BCEBF2",
    on_tertiary_container="#001F23",
    tertiary_fixed="#BCEBF2",
    tertiary_fixed_dim="#A1CED5",
    on_tertiary_fixed="#001F23",
    on_tertiary_fixed_variant="#1F4D53",
    error="#BA1A1A",
    on_error="#FFFFFF",
    error_container="#FFDAD6",
    on_error_container="#410002",
    surface="#F7FBF2",
    on_surface="#181D17",
    surface_dim="#D8DCD3",
    surface_bright="#F7FBF2",
    surface_container_lowest="#FFFFFF",
    surface_container_low="#F1F5EC",
    surface_container="#EBF0E7",
    surface_container_high="#E5EAE1",
    surface_container_highest="#DFE4DB",
    on_surface_variant="#424940",
    outline="#72796F",
    outline_variant="#C2C9BD",
    inverse_surface="#2D322B",
    on_inverse_surface="#EFF2E9",
    inverse_primary="#8BD797",
    shadow="#000000",
    scrim="#000000",
    surface_tint="#32AE60",
)

dark_schema = ColorSchema(
    primary="#8BD797",
    on_primary="#003914",
    primary_container="#005221",
    on_primary_container="#A6F4B1",
    primary_fixed="#A6F4B1",
    primary_fixed_dim="#8BD797",
    on_primary_fixed="#00210A",
    on_primary_fixed_variant="#005221",
    secondary="#B9CCB4",
    on_secondary="#253424",
    secondary_container="#3B4B39",
    on_secondary_container="#D5E8CF",
    secondary_fixed="#D5E8CF",
    secondary_fixed_dim="#B9CCB4",
    on_secondary_fixed="#101F10",
    on_secondary_fixed_variant="#3B4B39",
    tertiary="#A1CED5",
    on_tertiary="#00363C",
    tertiary_container="#1F4D53",
    on_tertiary_container="#BCEBF2",
    tertiary_fixed="#BCEBF2",
    tertiary_fixed_dim="#A1CED5",
    on_tertiary_fixed="#001F23",
    on_tertiary_fixed_variant="#1F4D53",
    error="#FFB4AB",
    on_error="#690005",
    error_container="#93000A",
    on_error_container="#FFDAD6",
    surface="#101510",
    on_surface="#E0E4DB",
    surface_dim="#101510",
    surface_bright="#363A34",
    surface_container_lowest="#0B0F0B",
    surface_container_low="#181D17",
    surface_container="#1C211B",
    surface_container_high="#272B25",
    surface_container_highest="#31362F",
    on_surface_variant="#C2C9BD",
    outline="#8C9388",
    outline_variant="#424940",
    inverse_surface="#E0E4DB",
    on_inverse_surface="#2D322B",
    inverse_primary="#32AE60",
    shadow="#000000",
    scrim="#000000",
    surface_tint="#8BD797",
)

theme_mode = ThemeMode.DARK

def get_color_schema():
    global theme_mode, color_schema, light_schema, dark_schema
    if theme_mode == ThemeMode.LIGHT:
        return light_schema
    elif theme_mode == ThemeMode.DARK:
        return dark_schema
    else:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            is_light, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return light_schema if is_light else dark_schema
        except Exception as e:
            print(e)
            return dark_schema

color_schema : ColorSchema = get_color_schema()

def update_color_schema():
    global color_schema
    color_schema = get_color_schema()