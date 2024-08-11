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
class TipoDeViaje:
    
    def __init__(self, tipo):
        self.tipo = tipo
        
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        if valor not in ['diesel', 'electrico', 'alta velocidad']:
            raise Exception('El tipo de viaje debe ser diesel, electrico o alta velocidad')
        self._tipo = valor