'''
Ejercicio: Función de orden superior
1)Implementar una función llamada wrapper que reciba por parámetro a otra función f sin
argumentos, la ejecute e imprima en pantalla el mensaje de ejecución: "Ejecutada f()".
'''
from typing import Callable
def wrapper(f: Callable):
    return f()

def funcion():
    print('Ejecutada f()')
    
if __name__ == '__main__':
    wrapper(funcion)


'''
2)Extender la función wrapper de forma que pueda aceptar cualquier función con
argumentos variables y se puedan pasar también desde la función wrapper para que se
invoquen en f. Por ejemplo, si f acepta 3 argumentos, éstos deberían también pasarse a
wrapper para que se invoque f(arg1, arg2, arg3) dentro.

'''

def wrapper(f: Callable, *args):
    return f(*args)

def funcion(*args):
    print(f'Ejecutada f({args})')
    
if __name__ == '__main__':
    wrapper(funcion, 1, 2, 3)