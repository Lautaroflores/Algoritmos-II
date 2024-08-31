'''
Escribir una función recursiva de cola que tome un
número entero positivo como entrada y devuelva la
suma de sus dígitos. Por ejemplo, la suma de los
dígitos de 123 sería 1 + 2 + 3 = 6.
'''

def suma_entero(n: int, acumulado=0) -> int:
    if n == 0:
        return acumulado
    else:
        return suma_entero(n // 10, acumulado + n % 10)
    
# Ejemplo de uso
resultado = suma_entero(123)
print(resultado)