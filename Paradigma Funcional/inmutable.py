'''
Implementar una versión de un conjunto de elementos de cualquier tipo que
sea inmutable. Podemos apoyarnos en la tuple de Python. El conjunto se
crea con una cantidad de elementos variables y luego ya no puede
modificarse.
'''
from dataclasses import dataclass

class Inmutable:
    __slots__ = ('numero', 'elementos')
    def __init__(self, numero,y):
        self.numero = numero
        self.elementos = elementos # type: ignore
        
    def __str__(self):
        return f'{self.numero} {self.elementos}'
    
    def __delattr__(self, name: str) -> None:
        raise Exception('No se puede eliminar atributos')
    
    def __setattr__(self, name: str, value) -> None:
        raise Exception('No se puede modificar atributos')
    
if __name__ == '__main__':
    try:
        inmutable = Inmutable(12,3)
        print(inmutable)
        del inmutable.numero
        inmutable.numero = 2
        print(inmutable)
    except Exception as e:
        print(e)