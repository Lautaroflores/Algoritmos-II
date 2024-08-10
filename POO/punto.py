'''
Implemente la clase Punto (pares de coordenadas de tipo float x, y). Defina
constructores y métodos para asignar valores a las coordenadas de los puntos,
retornar el valor de cada coordenada, y sumar dos puntos, retornando su
resultado. Definir un método booleano de igualdad entre dos puntos.
'''

class Punto:
    def __init__(self, x, y):
        self.x= x
        self.y=y
    
    def igualdad(self):
        if self.x == self.y:
            return True
        else:
            return False
    
    def suma(self):
        suma = self.x + self.y
        return f'Suma de coordenadas: {suma}'
    
   
    def __str__(self):
        return f'X: {self.x} || Y: {self.y}'
    

#Testeo
test = Punto(2.5, 4.2)
print(test)
print(test.suma())
print(test.igualdad())
