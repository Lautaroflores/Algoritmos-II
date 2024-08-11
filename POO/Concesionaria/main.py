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
from datetime import date
from concesionaria import Concesionaria
from camion import Camion
from automovilMediano import AutoMediano

if __name__ == '__main__':
    auto = AutoMediano('Ford', 'Fiesta')
    auto.habilitar(date.today())
    print(auto)
    
    camion = Camion('Scania', 'R420')
    print(camion)
    
    concesionaria = Concesionaria()
    concesionaria.habilitar_camion(camion)
    camion.autorizar()
    print(f'Camion despues de pasar por consecionaria:\n{camion}')