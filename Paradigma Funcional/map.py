'''
A través del uso del map, dada una lista de cadenas generar una nueva lista
que devuelva la cantidad que tiene de cierta letra (pasada como argumento)
cada elemento.
Por ejemplo, si queremos contar la letra 'a' en ['casa', 'hogar', 'espacio',
'cuento'] deberíamos obtener [2, 1, 1, 0].
'''

def contar_letra(lista: list[str], letra: str) -> list[int]:
    return list(map(lambda x: x.count(letra), lista))

if __name__ == '__main__':
    lista = ['casa', 'hogar', 'espacio', 'cuento']
    letra = 'a'
    print(contar_letra(lista, letra))