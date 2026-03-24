from typing import TypeVar, Type, Optional
import tkinter as tk

T = TypeVar("T", bound="ViewModel")
class ViewModel:
    """
    Clase base para la lógica de negocio y el estado de la aplicación.
    
    Su única responsabilidad es gestionar los datos
    y notificar a las vistas registradas cuando estos cambian.

    COMO USAR:
    1. Heredar de esta clase: `class MiViewModel(ViewModel):`
    2. Definir las variables de estado en el `__init__`.
    3. Llamar a `self.notify("propiedad")` cada vez que cambies un dato.

    EJEMPLO:
    ```python
    class CounterViewModel(ViewModel):
        def __init__(self):
            super().__init__()
            self.count = 0

        def increment(self):
            self.count += 1
            self.notify("count")  # Notifica solo el cambio en 'count'
            
        def reset(self):
            self.count = 0
            self.notify()  # Sin argumentos notifica un refresco total
    ```
    """
    def __init__(self):
        self._listeners = []
        
    def add_listener(self, callback):
        self._listeners.append(callback)
        
    def remove_listener(self, callback):
        if callback in self._listeners:
            if callback in self._listeners:
                self._listeners.remove(callback)
                
    def notify(self, *args):
        for callback in self._listeners:
            callback(*args)
    
    @classmethod
    def search(cls: Type[T], node: tk.Widget) -> Optional[T]:
        """
        Busca una instancia de este ViewModel subiendo por los 
        nodos master de Tkinter.
        """
        current = node
        while current:
            if (hasattr(current, "vm") and isinstance(current.vm, cls)):
                return current.vm
            try:
                current = current.master
            except AttributeError:
                break    
        return None