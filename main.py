import importlib
import importlib.util
from services.database import initialize_db
from app import App

#NOTE: Para usar el entorno de pruebas:
#1. Crear 'test_enviroment.py' en la raíz.
#2. Definir 'class TestEnviroment:'.
#3. El código de prueba debe ir en el __init__.

if __name__ == "__main__":
    while True:
        option = input("Quieres abrir el entorno de pruebas [Y/N] ").upper()
        if option == "Y":
            test_module_name = "test_enviroment"
            test_lib = importlib.util.find_spec(test_module_name)
            if test_lib is not None:
                test_module = importlib.import_module(test_module_name)
                print("Iniciando el entorno de pruebas...")
                test_class_name = "TestEnviroment"
                test_class_instance = getattr(test_module, test_class_name)
                if test_class_instance:
                    test_class_instance()
                else:
                    print(f"No se encontró la clase '{test_class_name}'.")
                break
            else:
                print(f"No se encontró el archivo '{test_module_name}.py'.")
        elif option == "N":
            print("Iniciando App Principal...")
            initialize_db()
            root = App()
            root.mainloop()
            break
        else:
            print(f"'{option}' no es válido. Intenta de nuevo, por favor.")
