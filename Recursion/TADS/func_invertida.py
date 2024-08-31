'''
Implementa una función que invierta una
cadena utilizando recursión de cola
'''

def func_invertida(cadena: str, indice=0, invertida='') -> str:
    if indice == len(cadena):
        return invertida
    else:
        return func_invertida(cadena, indice + 1, cadena[indice] + invertida)
    
# Ejemplo de uso
resultado = func_invertida('Hello world!')
print(resultado) 