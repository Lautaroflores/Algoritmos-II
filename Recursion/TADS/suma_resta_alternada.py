def suma_resta_alternada(lista, indice=0, acumulado=0):
    if indice == len(lista):
        return acumulado
    if indice == 0:
        return suma_resta_alternada(lista, indice + 1, lista[indice])
    elif indice != 0 and indice % 2 == 0:
        return suma_resta_alternada(lista, indice + 1, acumulado - lista[indice])
    else:
        return suma_resta_alternada(lista, indice + 1, acumulado + lista[indice])

# Ejemplo de uso
resultado = suma_resta_alternada([1, 2, 3, 4, 5])
print(resultado)  # Salida: -1
