'''
Una editorial de libros y discos desea crear fichas que almacenen el título y el
precio de cada publicación. Definir la correspondiente clase Publicacion que
implemente los datos anteriores. Derive dos clases, una llamada Libro, que
contenga para cada libro el número de páginas, año de publicación y precio, y la
clase Disco, con la duración en minutos y precio. Programar una aplicación que
pruebe las clases.
'''

from publicacion import Publicacion

class Disco(Publicacion):
    def __init__(self, titulo:str, precio:float, duracion:int):
        super().__init__(titulo, precio)
        self.duracion = duracion

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor
    
    def __str__(self):
        return f'Título: {self.titulo}, Precio: {self.precio}, Duración: {self.duracion} minutos'