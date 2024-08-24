'''
Definir la función desde_hasta recursiva que dados dos números enteros retorne
una lista de números consecutivos donde el primer elemento de la lista resultante
sea el primer elemento dado, y el último elemento de la lista resultante sea el
segundo elemento dado.
Redefinir las funciones sumatoria y factorial utilizando desde_hasta.
'''

def desde_hasta(desde: int, hasta: int) -> list[int]:
    if desde == hasta:
        return [desde]
    return [desde] + desde_hasta(desde + 1, hasta)

def sumatoria(desde: int, hasta: int) -> int:
    return sum(desde_hasta(desde, hasta))

def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)

if __name__ == '__main__':
    numeros=desde_hasta(1,5)
    print(numeros)
    
    print(sumatoria(1,5))
    print(factorial(5))
