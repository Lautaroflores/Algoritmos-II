'''
Implemente la clase Hora que contenga miembros datos separados para almacenar
horas, minutos y segundos. Un constructor inicializará estos datos en 0 y otro a valores
dados. Una función miembro deberá visualizar la hora en formato hh:mm:ss. Otra
función miembro sumará dos objetos de tipo hora, retornando la hora resultante.
Realizar otra versión de la suma que asigne el resultado de la suma en el primer objeto
hora.
'''

class Hora:
    
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.normalizar()
        
    def normalizar(self):
       
        if self.segundos >= 60:
            self.segundos -= 60
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos -= 60
            self.horas += 1
    
        
    def __str__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'
    
    def sumar(self, otra_hora):
        segundos = self.segundos + otra_hora.segundos
        minutos = self.minutos + otra_hora.minutos
        horas = self.horas + otra_hora.horas
        
        hora_nueva = Hora(horas, minutos, segundos)
        hora_nueva.normalizar()
        return hora_nueva
    
    def sumar_inplace(self, otra_hora):
        self.segundos += otra_hora.segundos
        self.minutos += otra_hora.minutos
        self.horas += otra_hora.horas
        return self.normalizar()
    
    
def main():
    hora1 = Hora(10, 30, 45)
    hora2 = Hora(5, 45, 30)
    hora3 = Hora()
    
    print (f'La hora 1 es: {hora1}')
    print (f'La hora 2 es: {hora2}')
    print (f'La hora 3 es: {hora3}')
    
    hora3 = hora1.sumar(hora2)
    print (f'La suma de la hora 1 y hora 2 es: {hora3}')


if __name__ == "__main__":
 main()