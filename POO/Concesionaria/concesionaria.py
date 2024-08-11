'''
Definir la clase Automovil, que puede subclasificarse en AutoMediano o Camion.
Los autos medianos son capaces de estar habilitados luego de la adquisición de
un permiso en una fecha dada. Los camiones también podrán estar habilitados
luego de la adquisición de un permiso, pero éste sólo podrá expedirse con la
debida autorización previa de la concesionaria donde fue adquirido. Las
concesionarias de camiones verifican ciertas características del camión para
poder registrar al mismo. Este dato también es registrado dentro de la misma
concesionaria.
'''
from camion import Camion

class Concesionaria:
    def __init__(self):
        self.camiones = []
    
    def registrar_camion(self, camion):
        self.camiones.append(camion)
        
    def habilitar_camion(self, camion):
        camion.habilitar()
    
    def verificar_camion(self, camion):
        if camion.autorizacion:
            self.registrar_camion(camion)
        else:
            print('Camion no autorizado')
    
    def __str__(self):
        return f'Camiones: {self.camiones}'