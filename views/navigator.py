import tkinter as tk


class Navigator(tk.Frame):
    """
    Gestor de navegación de frames basado en una pila (Stack) para Tkinter.
    
    Ejemplo de uso:
    >>> root = tk.Tk()
    >>> # 1. Crear el Navigator primero
    >>> nav = Navigator(root)
    >>> nav.pack(fill="both", expand=True)
    
    >>> # 2. Crear el frame inicial usando el navigator como master y cargarlo
    >>> home = tk.Frame(nav, bg="white")
    >>> nav.push(home)
    
    >>> # 3. Navegar a otra pantalla (Push)
    >>> settings = tk.Frame(nav, bg="blue")
    >>> nav.push(settings)
    
    >>> # 4. Regresar a la pantalla anterior (Pop)
    >>> nav.pop()
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.stack = []
        tk.Frame()

    def push(self, frame: tk.Frame):
        """
        Agrega un nuevo frame a la pila y lo despliega.
        
        Nota:
            Es imperativo que el parámetro 'frame' haya sido instanciado 
            teniendo a este Navigator como su 'master'. De lo contrario, 
            se producirá un error de jerarquía.
        
        :param frame: Instancia a mostrar. Debe ser hijo del Navigator.
        :type frame: tk.Frame
        :raises ValueError: Si el master del frame no coincide con la instancia del Navigator.
        """
        if frame.master != self:
            raise ValueError(
                f"¡ERROR DE JERARQUÍA! El frame {type(frame).__name__}"
                f"debe tener como master el Navigator, no a {frame.master}"
            )
        
        if self.stack:
            self.stack[-1].pack_forget()

        frame.pack(fill="both", expand=True)
        self.stack.append(frame)

    def pop(self):
        """
        Destruye el frame actual y restaura el anterior en la pila.
        
        Si solo existe un frame en el historial, la operación se ignora mantener la integridad de la interfaz.
        """
        if len(self.stack):
            view_to_remove = self.stack.pop()
            view_to_remove.destroy()
            self.stack[-1].pack(fill="both", expand=True)
