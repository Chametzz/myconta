class Auto: #Cristian i
    def __init__(self, marca, modelo, color, encendido, marcha_actual, kilometraje, temperatura, nivel_combustible, numero_serie, propietario):
     self.marca = marca
     self.modelo = modelo
     self.color = color 
     self.encendido = encendido
     self.marcha_actual = marcha_actual
     self.__kilometraje = kilometraje
     self.__temperatura = temperatura
     self._nivel_combustible = nivel_combustible
     self._numejor_serie = numero_serie
     self.__propietario = propietario
     
    @property
    def marca(self):
        return self.marca
    @marca.setter
    def marca(self,new_marca):
        self.marca = new_marca

    @property
    def modelo(self):
        return self.modelo
    @modelo.setter
    def modelo(self,new,modelo):
        self.modelo = new.modelo 
        
    @property
    def color(self):
        return self.color
    @color.setter
    def color(self,new,color):
        self.color = new.color 
        
    @property
    def encendido(self):
        return self.encendido
    @encendido.setter
    def encendido(self,new,encendido):
        self.encendido = new.encendido 
        
    @property
    def marcha_actual(self):
        return self.marcha_actual
    @marcha_actual.setter
    def marcha_actual(self,new,marcha_actual):
        self.marcha_actual = new.marcha_actual 
        
    @property
    def _kilometraje(self):
        return self._kilometraje
    @_kilometraje.setter
    def _kilometraje(self,new,_kilometraje):
        self._kilometraje = new._kilometraje
        
    @property
    def __temperatura(self):
        return self.__temperatura
    @__temperatura.setter
    def __temperatura(self,new,__temperatura):
        self.__temperatura = new.__temperatura