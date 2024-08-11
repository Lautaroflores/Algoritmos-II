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

b) Sin especializar la clase Viaje, relacionándola con la clase TipoDeViaje, que está especializada por cada tipo
de viaje
'''
from tipoDeViaje import TipoDeViaje

class Viaje:
    def __init__(self, origen, destino, distancia, cantidad_estaciones, cantidad_vagones, pasajeros, tipo_de_viaje):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.cantidad_estaciones = cantidad_estaciones
        self.cantidad_vagones = cantidad_vagones
        self.pasajeros = pasajeros
        self.tipo_de_viaje = tipo_de_viaje
    
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
    def pasajeros(self):
        return self._pasajeros
    
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
        
    
    @pasajeros.setter
    def pasajeros(self, valor):
        self._pasajeros = valor
        
    def tiempoDeDemora(self):
        if self.tipo_de_viaje.tipo == 'diesel':
            return self.distancia * self.cantidad_estaciones / 2 + (self.cantidad_estaciones + self.pasajeros) / 10
        elif self.tipo_de_viaje.tipo == 'electrico':
            return self.distancia * self.cantidad_estaciones / 2
        elif self.tipo_de_viaje.tipo == 'alta velocidad':
            return self.distancia / 10
        else:
            raise Exception('El tipo de viaje no es correcto')
        
    def __str__ (self):
        return f'Viaje de {self._origen} a {self._destino} con {self._cantidad_vagones} vagones y una capacidad de {self._pasajeros} pasajeros y de una tecnologia {self.tipo_de_viaje.tipo}'
        
if __name__ == '__main__':
    try:
        tipo = TipoDeViaje('diesel')
        viaje = Viaje('Buenos Aires', 'Rosario', 300, 5, 10, 100, tipo)
        tiempo = viaje.tiempoDeDemora()
        print(f'{viaje}. El tiempo de demora es de {tiempo} minutos')
        
        tipo = TipoDeViaje('electrico')
        viaje = Viaje('Buenos Aires', 'Rosario', 300, 5, 10, 100, tipo)
        tiempo = viaje.tiempoDeDemora()
        print(f'{viaje}. El tiempo de demora es de {tiempo} minutos')
        
        tipo = TipoDeViaje('alta velocidad')
        viaje = Viaje('Buenos Aires', 'Rosario', 300, 5, 10, 100, tipo)
        tiempo = viaje.tiempoDeDemora()
        print(f'{viaje}. El tiempo de demora es de {tiempo} minutos')
        
    except Exception as e:
        print(e)