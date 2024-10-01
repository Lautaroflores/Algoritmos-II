'''
Definir la función permutaciones, que dada una lista de
enteros, retorne una lista de listas de enteros, donde cada
lista es cada una de las posibles permutaciones de la lista
original, usando backtracking.
'''

def permutaciones (lista):
    def backtrack (lista, n, solucion, resultado):
        if n == len(lista):
            resultado.append(solucion[:])
            return
        for i in range(len(lista)):
            if lista[i] in solucion:
                continue
            solucion.append(lista[i])
            backtrack(lista, n+1, solucion, resultado)
            solucion.pop()
    resultado = []
    backtrack(lista, 0, [], resultado)
    return resultado

# Pruebas
print(permutaciones([1, 2, 3]))