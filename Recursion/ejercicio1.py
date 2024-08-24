'''
a. Una función recursiva digitos, que dado un número entero, retorne su cantidad de
dígitos.
b. Una función recursiva reversa_num que, dado un número entero, retorne su imagen
especular. Por ejemplo: reversa_num(345) = 543
c. Una función recursiva suma_digitos que, dado un número entero, retorne la suma de
sus dígitos.
d. Una función recursiva que retorne los dos valores anteriores a la vez como un par,
aprovechando la recursión. (retorne tanto la suma de los dígitos como el número
invertido a la vez)
'''

def digitos(n: int) -> int:
    if n < 10:
        return 1
    return 1 + digitos(n // 10)

def reversa_num(n: int) -> int:
    if n < 10:
        return n
    return (n % 10) * 10 ** digitos(n // 10) + reversa_num(n // 10)

def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

def digitos_reversa_suma(n: int) -> tuple[int, int]:
    if n < 10:
        return 1, n
    return suma_digitos(n), reversa_num(n)

if __name__ == '__main__':
    n = 12
    print(digitos(n))
    
    reversa = 345
    print(reversa_num(reversa))
    
    suma = 123
    print(suma_digitos(suma))
    
    print(digitos_reversa_suma(123))