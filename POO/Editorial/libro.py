'''
Una editorial de libros y discos desea crear fichas que almacenen el título y el
precio de cada publicación. Definir la correspondiente clase Publicacion que
implemente los datos anteriores. Derive dos clases, una llamada Libro, que
contenga para cada libro el número de páginas, año de publicación y precio, y la
clase Disco, con la duración en minutos y precio. Programar una aplicación que
pruebe las clases.
'''
from publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, titulo:str, precio:float, numero_paginas:int, anio_publicacion:int):
        super().__init__(titulo, precio)
        self.numero_paginas = numero_paginas
        self.anio_publicacion = anio_publicacion

    @property
    def numero_paginas(self):
        return self._numero_paginas

    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @numero_paginas.setter
    def numero_paginas(self, valor):
        self._numero_paginas = valor

    @anio_publicacion.setter
    def anio_publicacion(self, valor):
        self._anio_publicacion = valor
