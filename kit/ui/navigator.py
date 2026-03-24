from tkinter import Frame

class Navigator(Frame):
    """
    Gestor de navegación basado en una pila (Stack) de Frames.
    
    Permite cambiar entre diferentes vistas manteniendo un historial, 
    lo que facilita la creación de flujos de usuario (adelante/atrás).
    
    COMO USAR:
    1. Instanciar el Navigator: `nav = Navigator(root)`
    2. Crear una vista: `vista = HomeView(nav, vm)`
    3. Mostrarla: `nav.push(vista)`
    """

    def __init__(self, master):
        """
        Inicializa el contenedor de navegación.
        
        Args:
            master: El widget padre donde se renderizarán las vistas.
        """
        super().__init__(master)
        self.stack = []  # Pila de objetos View (Frames)
    
    def push(self, view: Frame):
        """
        Agrega una nueva vista a la pila y la muestra en pantalla.
        
        Si existe una vista previa, oculta su contenido y dispara 
        su método 'on_exit' si existe.
        
        Args:
            view: La instancia de la vista (Frame) que se desea mostrar.
        """
        if self.stack:
            # Notificar a la vista actual que va a ser pausada/oculta
            if hasattr(self.stack[-1], "on_exit"):
                self.stack[-1].on_exit()
            self.stack[-1].pack_forget()
        
        # Mostrar la nueva vista
        view.pack_propagate(False)
        view.pack(fill='both', expand=True)
        self.stack.append(view)
        
        # Notificar a la nueva vista que ha entrado en pantalla
        if hasattr(view, 'on_enter'):
            view.on_enter()
    
    def pop(self):
        """
        Elimina la vista actual (la destruye) y regresa a la anterior.
        
        Ejecuta los ciclos de vida 'on_exit' de la vista que sale y 
        'on_enter' de la vista que recupera el foco.
        """
        if len(self.stack) > 1:
            # Extraer y limpiar la vista superior
            view_to_remove = self.stack.pop()
            if hasattr(view_to_remove, 'on_exit'):
                view_to_remove.on_exit()
            
            view_to_remove.destroy() # Liberamos memoria
            
            # Recuperar la vista anterior de la pila
            previous_view = self.stack[-1]
            previous_view.pack_propagate(False)
            previous_view.pack(fill='both', expand=True)
            
            # Notificar que vuelve a estar activa
            if hasattr(previous_view, 'on_enter'):
                previous_view.on_enter()
    
    @classmethod
    def of(cls, context : Frame) -> 'Navigator':
        """
        Busca hacia arriba en el árbol de widgets hasta encontrar 
        la instancia del Navigator.
        """
        current = context
        while current is not None:
            if isinstance(current, cls):
                return current
            current = current.master
            
        raise LookupError(f"No se encontró Navigator en {context}")