'''
Una empresa ferroviaria administra viajes en tren entre dos estaciones terminales de su red.
Un viaje tiene asociado un trayecto (desde una estación terminal de origen a una de destino, con una distancia
determinada y una cantidad de estaciones), una cierta cantidad de vagones y una capacidad máxima de
pasajeros.
También posee qué tipo de viaje corresponde en relación a sus características técnicas, si es un viaje con
tecnología diesel, si es eléctrico o si es de alta velocidad (esto es independiente del trayecto recorrido).
● Viaje diesel: El tiempo de demora promedio -en minutos- es la distancia en kilómetros multiplicada por la
cantidad de estaciones dividido 2 sumada a la cantidad de estaciones y de pasajeros dividido 10.
● Viaje eléctrico: El tiempo de demora promedio -en minutos- es la distancia en kilómetros multiplicada por la
cantidad de estaciones dividido 2.
● Viaje de alta velocidad: El tiempo de demora promedio -en minutos-es la distancia en kilómetros dividido
10.
Definir dentro de la clase Viaje el método tiempoDeDemora, que retorne la cantidad de minutos que tarda en
efectuar su recorrido con las siguientes variantes:
a) Especializando la clase Viaje en función del tipo de viaje.
'''

class Viaje:
    
#-- Constructor --
    def __init__(self, origen, destino, distancia, cantidad_estaciones, cantidad_vagones, capacidad_maxima_pasajeros, tecnologia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.cantidad_estaciones = cantidad_estaciones
        self.cantidad_vagones = cantidad_vagones
        self.capacidad_maxima_pasajeros = capacidad_maxima_pasajeros
        self.tecnologia = tecnologia
        
#-- Propiedades --

    @property
    def destino(self):
        return self._destino
    
    @property
    def origen(self):
        return self._origen
    
    @property
    def cantidad_estaciones(self):
        return self._cantidad_estaciones
   
    @property
    def cantidad_vagones(self):
        return self._cantidad_vagones
    
    @property
    def capacidad_maxima_pasajeros(self):
        return self._capacidad_maxima_pasajeros
    
    @property
    def tecnologia(self):
        return self._tecnologia
    
    @property
    def distancia(self):
        return self._distancia
    
    
#-- Setters --
   
    @origen.setter
    def origen(self, valor):
        self._origen = valor
    
    @destino.setter
    def destino(self, valor):
        self._destino = valor
        
    @distancia.setter
    def distancia(self, valor):
        self._distancia = valor
        
    @cantidad_estaciones.setter
    def cantidad_estaciones(self, valor):
        self._cantidad_estaciones = valor
    
    @cantidad_vagones.setter
    def cantidad_vagones(self, valor):
        self._cantidad_vagones = valor
        
    
    @capacidad_maxima_pasajeros.setter
    def capacidad_maxima_pasajeros(self, valor):
        self._capacidad_maxima_pasajeros = valor
        
    @tecnologia.setter
    def tecnologia(self, valor):
        if valor in ['diesel', 'electrico', 'alta velocidad']:
            self._tecnologia = valor
        else:
            raise Exception('Tecnologia no valida')
        
    def __str__ (self):
        return f'Viaje de {self._origen} a {self._destino} con {self._cantidad_vagones} vagones y una capacidad de {self._capacidad_maxima_pasajeros} pasajeros y de una tecnologia {self._tecnologia}'
        
#-- Metodos --
        
    def tiempoDeDemora(self) -> float:
        if self.tecnologia == 'diesel':
            return self._distancia * self._cantidad_estaciones / 2 + self._cantidad_estaciones + self._capacidad_maxima_pasajeros / 10
        elif self.tecnologia == 'electrico':
            return self._distancia * self._cantidad_estaciones / 2
        else:
            return self._distancia / 10 
        

if __name__ == '__main__':
    try:
        viaje = Viaje('casa', 'trabajo',5, 100, 10, 100, 'diesel')
        viaje.tecnologia = 'diesel'
        print(viaje)
        print(viaje.tiempoDeDemora())
        
    except Exception as e:
        print(e)