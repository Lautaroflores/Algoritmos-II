'''
a) Crear una clase Vehiculo con los siguientes atributos y métodos:
● Atributos:
○ marca (String)
○ modelo (String)
○ precioBase (double).
● Métodos:
○ Un constructor que acepte la marca, modelo y precio base del vehículo.
○ Un método calcularCostoAlquiler(int dias) que calcule el costo de alquiler del vehículo
durante el número de días especificado. El costo se calcula como precioBase * dias.
'''

from typing import Any


class Vehiculo:
    
    def __init__(self, marca: str, modelo: str, precioBase: float):
        self.marca      = marca
        self.modelo     = modelo
        self.precioBase = precioBase
        self.dias = 1
        
    
    @property
    def dias(self):
        return self._dias
    
    @dias.setter
    def dias(self, valor:int):
        if valor <=0:
            raise Exception('Los dias deben ser enteros positivos')
        self._dias = valor
        
    
    def calcularCostoAlquiler(self) -> float:
        return self.precioBase * self._dias
    
    def __str__(self):
        return f'{self.marca} {self.modelo} tiene un precio de ${self.precioBase}'
    
if __name__ == '__main__':
    try:
        vehiculo = Vehiculo('Porsche', 'Carrera GT', 5000.5)
        vehiculo.dias = 5
        costo    = vehiculo.calcularCostoAlquiler()
        print(f'{vehiculo}. El costo por {vehiculo.dias} días es de: ${costo}')   
    except Exception as e:
        print (e)  