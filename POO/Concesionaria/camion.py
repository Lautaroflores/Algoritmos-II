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
from automovil import Automovil

class Camion(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.permiso = False
        self.autorizacion = False
        
    def habilitar(self):
        self.permiso = True
        
    def autorizar(self):
        self.autorizacion = True
        
    def __str__(self):
        return f'{self.marca} {self.modelo} - Permiso: {self.permiso} - Autorizacion: {self.autorizacion}'