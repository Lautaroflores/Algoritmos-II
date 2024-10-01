'''
Crear dentro del TAD ArbolBinario una función recursiva nivel, que dado un valor, retorne en
qué nivel se encuentra en el nodo del árbol. Si el valor no se encontrara en el árbol, retornar un
valor superior a la altura del árbol.
'''

#Asi se ve mejor. Tenia un monton de funciones que no usaba
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class NodoAB(Generic[T]):
    def __init__(self, dato: T):
        self.dato = dato
        self.si: Optional[NodoAB[T]] = None  # Subárbol izquierdo
        self.sd: Optional[NodoAB[T]] = None  # Subárbol derecho

    def __str__(self):
        return str(self.dato)
    
class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None

    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato)
        return t

    def es_vacio(self) -> bool:
        return self.raiz is None

    def insertar_si(self, subarbol: "ArbolBinario[T]") -> None:
        if self.raiz is None:
            raise ValueError("El árbol está vacío")
        self.raiz.si = subarbol.raiz

    def insertar_sd(self, subarbol: "ArbolBinario[T]") -> None:
        if self.raiz is None:
            raise ValueError("El árbol está vacío")
        self.raiz.sd = subarbol.raiz

    def altura(self) -> int:
        if self.raiz is None:
            return 0
        return 1 + max(self._altura(self.raiz.si), self._altura(self.raiz.sd))

    def _altura(self, nodo: Optional[NodoAB[T]]) -> int:
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.si), self._altura(nodo.sd))

    def __len__(self) -> int:
        if self.raiz is None:
            return 0
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo: Optional[NodoAB[T]]) -> int:
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.si) + self._contar_nodos(nodo.sd)

    def bfs(self) -> list[T]:
        if self.raiz is None:
            return []
        resultado = []
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.dato)
            if nodo.si is not None:
                cola.append(nodo.si)
            if nodo.sd is not None:
                cola.append(nodo.sd)
        return resultado

    def nivel(self, valor: T, nodo: Optional[NodoAB[T]] = None, nivel_actual: int = 0) -> int:
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return float('inf')
        
        if nodo.dato == valor:
            return nivel_actual

        nivel_izquierdo = self.nivel(valor, nodo.si, nivel_actual + 1) if nodo.si else float('inf')
        nivel_derecho = self.nivel(valor, nodo.sd, nivel_actual + 1) if nodo.sd else float('inf')
            
        return min(nivel_izquierdo, nivel_derecho)

# Ejemplo de uso
if __name__ == "__main__":
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n5.insertar_si(n8)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n3)
    
    print(f'Altura: {t.altura()}')
    print(f'Nodos: {len(t)}')

    print(f'BFS: {t.bfs()}')
    print(f'Nivel de 5: {t.nivel(5)}')
    print(f'Nivel de 3: {t.nivel(3)}')
    print(f'Nivel de 6: {t.nivel(6)}')