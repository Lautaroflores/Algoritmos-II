from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato

    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self._head.dato), parcial)
            return actual
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()

    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)

    def eliminar(self, valor: T):
        def _eliminar_interna(actual: ListaGenerica, previo: ListaGenerica, valor: T):
            if not actual.es_vacia():
                if actual.head() == valor:
                    previo._head.sig = actual._head.sig
                else:
                    _eliminar_interna(actual._head.sig, actual, valor)

        if not self.es_vacia():
            if self.head() == valor:
                self._head = self._head.sig._head
            else:
                _eliminar_interna(self._head.sig, self, valor)

    def ultimo(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            if self._head.sig.es_vacia():
                return self._head.dato
            else:
                return self._head.sig.ultimo()

    def concat(self, ys: ListaGenerica) -> ListaGenerica:
        if self.es_vacia():
            return ys
        else:
            actual = copy(self)
            actual._head.sig = self._head.sig.concat(ys)
            return actual
        
    def join(self, separador: str = '') -> str:
        if self.es_vacia():
            return ''
        else:
            if self._head.sig.es_vacia():
                return str(self._head.dato)
            else:
                return str(self._head.dato) + separador + self._head.sig.join(separador)
        
    def index(self, valor: T) -> int:
        def _index_interna(actual: ListaGenerica, contador: int, valor: T) -> int:
            if actual.es_vacia():
                return -1
            else:
                if actual.head() == valor:
                    return contador
                else:
                    return _index_interna(actual._head.sig, contador + 1, valor)

        return _index_interna(self, 0, valor)
        
    def existe(self, valor: T) -> bool:
        return self.index(valor) != -1

    def __repr__(self):
        elementos = []
        actual = self._head
        while actual is not None and not actual.sig.es_vacia():
            elementos.append(repr(actual.dato))
            actual = actual.sig._head
        if actual is not None:
            elementos.append(repr(actual.dato))
        return f'Lista([{", ".join(elementos)}])'

        
    def __eq__(self, otra: ListaGenerica) -> bool:
        if self.es_vacia() and otra.es_vacia():
            return True
        elif self.es_vacia() or otra.es_vacia():
            return False
        else:
            return self.head() == otra.head() and self.tail() == otra.tail()
    
    def __len__(self) -> int:
        if self.es_vacia():
            return 0
        else:
            return 1 + len(self.tail())
        
    def __getitem__(self, i: int) -> T:
        if i == 0:
            return self.head()
        else:
            return self.tail()[i - 1]

if __name__ == '__main__':
    xs: Lista[int] = Lista()
    
    print(f'xs es vacia? {xs.es_vacia()}')	# True
    
    # Operaciones basicas
    xs.insertar(4)
    xs.insertar(10)
    xs.insertar(20)
    ys: Lista[int] = xs.tail()
    ys.insertar(9)
    ys.eliminar(10)
    ys.insertar(8)
    zs: Lista[int] = ys.copy()
    zs.eliminar(8)
    zs.eliminar(9)
    
    print(f'xs: {xs}')						# [20, 10, 4]
    print(f'ys: {ys}')						# [8, 9, 4]
    print(f'xs es vacia? {xs.es_vacia()}')	# False
    print(f'ultimo(xs): {xs.ultimo()}')		# 4
    print(f'len(xs): {len(ys)}')			# 3, ver __len__
    print(f'xs[1]: {xs[1]}')				# 10, ver __getitem__

    # Consumiendo como iterable
    for x in xs:
        print(x)	# 20 -> 10 -> 4

    # Otras operaciones
    print(f'xs.concat(ys): {xs.concat(ys)}')		# [20, 10, 4, 8, 9, 4]
    print(f'ys.join(" -> "): {ys.join(" -> ")}')	# 8 -> 9 -> 4
    print(f'xs.index(4): {xs.index(4)}')			# 2
    print(f'xs.existe(10): {xs.existe(10)}')        # True
    print(f'xs == zs? {xs == zs}')                  # False
    zs.insertar(10)
    zs.insertar(20)
    print(f'xs == zs? {xs == zs}')                  # True
    