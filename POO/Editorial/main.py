'''
Una editorial de libros y discos desea crear fichas que almacenen el título y el
precio de cada publicación. Definir la correspondiente clase Publicacion que
implemente los datos anteriores. Derive dos clases, una llamada Libro, que
contenga para cada libro el número de páginas, año de publicación y precio, y la
clase Disco, con la duración en minutos y precio. Programar una aplicación que
pruebe las clases.
'''

from disco import Disco
from libro import Libro
from publicacion import Publicacion


if __name__ == '__main__':
    libro = Libro('El principito', 500, 100, 1943)
    disco = Disco('The Wall', 1000, 120)
    
    print(libro)
    print(disco)
    
    
