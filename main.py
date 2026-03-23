from services.app_service import AppService
from app import App

#NOTE: Para usar el entorno de pruebas:
#1. Crear 'test_enviroment.py' en la raíz.
#2. Definir 'class TestEnviroment:'.
#3. El código de prueba debe ir en el __init__.

if __name__ == "__main__":
    AppService()
    root = App()
    root.mainloop()
