'''
Una editorial de libros y discos desea crear fichas que almacenen el título y el
precio de cada publicación. Definir la correspondiente clase Publicacion que
implemente los datos anteriores. Derive dos clases, una llamada Libro, que
contenga para cada libro el número de páginas, año de publicación y precio, y la
clase Disco, con la duración en minutos y precio. Programar una aplicación que
pruebe las clases.
'''

class Publicacion:
    def __init__(self, titulo:str, precio:float):
        self.titulo = titulo
        self.precio = precio

    @property
    def titulo(self):
        return self._titulo

    @property
    def precio(self):
        return self._precio

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @precio.setter
    def precio(self, valor):
        self._precio = valor    
    