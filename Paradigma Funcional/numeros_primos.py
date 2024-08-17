'''
Implementar una función generadora que permita producir todos los números
primos uno a uno.
Nota: Un número es primo si no es divisible por ningún número entre 2 y su raíz
cuadrada
'''

from collections.abc import Iterator

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos() -> Iterator[int]:
    n = 2
    while True:
        if es_primo(n):
            yield n
        n += 1
        
if __name__ == '__main__':
    primos = numeros_primos()
    for _ in range (10):
        print(next(primos))
