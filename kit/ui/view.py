from tkinter import Frame
from kit.view_model import ViewModel
from typing import Callable
from services.color_schema import color_schema, color_schema_add_listener, color_schema_remove_listener

class View(Frame):
    """
    Esta clase automatiza la sincronización entre el ViewModel y la UI

    COMO USAR:
    1. Heredar de esta clase: `class MiVistaView(View)`
    2. **IMPORTANTE:** Definir el tipo de ViewModel para tener autocompletado:
    `vm: MiVistaViewModel`
    3. Definir widgets en el `__init__`.
    4. SOBRESCRIBIR el método `on_update(self, changed)`

    FLUJO DE DATOS:
    ViewModel.notify('prop') -> View.update('prop') -> View.on_update(changed)

    EJEMPLO:
    ```python
    #PASO 1
    class HomeView(View):
        
        #PASO 2
        vm: HomeViewModel
        
        #PASO 3
        def __init__(self, master, view_model):
            super().__init__(master, view_model)
            
            self.lbl_titulo = Label(self)
            self.lbl_titulo.pack() 

        #PASO 4
        def on_update(self, changed):
            if changed("titulo"):
                self.label.config(text=self.vm.titulo)
    ```
    """

    # Se recomienda que en las visas se agregue el vm : ViewModel de la ViewModel respectivo de la vista para facilitar la programación de la vista
    vm: ViewModel = None

    def __init__(self, master, view_model=None):
        """
        Args:
            master: El contenedor o padre de la instancia.
            view_model: Instancia de ViewModel que alimentará a esta vista.
        """
        super().__init__(master)
        self.vm = view_model
        if self.vm is not None:
            # Se suscribe el método update para que la vista pueda reaccionar al viewmodel.
            self.vm.add_listener(self.update)
        # Suscripción automática al esquema de colores
        color_schema_add_listener(self.update)

    def on_enter(self):
        pass
    
    def on_exit(self):
        pass
    
    def update(self, *args):
        """
        Prepara la lógica con la intención de actualizar los componentes gráficos de una vista.
        Tiene una función interna 'changed' que permite determinar si un argumento específico ha cambiado, en caso de que no haya argumentos actualizará toda la interfaz.
        Args:
            *args: Lista de nombres de propiedades que han cambiado.
                   Si está vacío, se asume una actualización total.
        """

        def changed(arg):
            return not args or arg in args

        self.on_update(changed)

    def on_update(self, changed: Callable[[str], bool]):
        """
        Método destinado a ser sobrescrito por el programador.
        Aquí es donde se define la lógica de actualización de la vista.

        ```python
        #Ejemplo de uso
        def on_update(self, changed):
            if changed("titulo"):
                self.label.config(text=self.vm.titulo)
        ```

        Args:
            changed (Callable[[str], bool]): Función que recibe el nombre de una propiedad y devuelve True si debe actualizarse el widget asociado.
        """
        pass
    
    def destroy(self):
        # Limpiar suscripciones
        color_schema_remove_listener(self.update)
        if self.vm:
            self.vm.remove_listener(self.update)
        super().destroy()