'''
Definir la función desde_hasta con recursión de cola que
dados dos números enteros retorne una lista de números
consecutivos donde el primer elemento de la lista
resultante sea el primer elemento dado, y el último
elemento de la lista resultante sea el segundo elemento
dado
'''
from typing import List

def desde_hasta(desde: int, hasta: int) -> List[int]:
    def _desde_hasta(desde: int, hasta: int, resultado: List[int]) -> List[int]:
        if desde > hasta:
            return resultado
        else:
            return _desde_hasta(desde, hasta - 1, [hasta]+ resultado)

    return _desde_hasta(desde, hasta, [])

# Pruebas
print(desde_hasta(1, 5)) # [1, 2, 3, 4, 5]