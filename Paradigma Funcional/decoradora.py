'''
Se pide implementar una función decoradora acepta_no_valor que permita
adaptar una función con un único parámetro de cualquier tipo no nulo de forma
que devuelva la evaluación de esa función si el argumento recibido no es None.
De lo contrario, debe devolver None.
TIP: Se puede usar el hint de tipo de retorno de la decoradora como: Callable[[T |
None], R | None]. Ver Generics
'''

from collections.abc import Callable
from functools import wraps

def acepta_no_valor(f: Callable) -> Callable:
    @wraps(f)
    def wrapper(x):
        if x is None:
            return None
        return f(x)
    return wrapper

@acepta_no_valor
def cuadrado(x: int) -> int:
    return x ** 2

if __name__ == '__main__':
    print(cuadrado(2))
    print(cuadrado(None))
    