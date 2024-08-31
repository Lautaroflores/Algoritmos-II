'''
Definir la función intercalar con recursión de pila, que
dadas dos listas de enteros, retorne una lista de
enteros que corresponda al intercalado elemento a
elemento de las dos listas dadas.
'''

from typing import List

from typing import List

def intercalar(xs: List[int], ys: List[int]) -> List[int]:
    def intercalar_aux(xs: List[int], ys: List[int], acc: List[int]) -> List[int]:
        if not xs and not ys:
            return acc
        elif not xs:
            return acc + ys
        elif not ys:
            return acc + xs
        else:
            return intercalar_aux(xs[1:], ys[1:], acc + [xs[0], ys[0]])

    return intercalar_aux(xs, ys, [])


    
# Pruebas
print(intercalar([1, 2, 3], [4, 5, 6])) # [1, 4, 2, 5, 3, 6]