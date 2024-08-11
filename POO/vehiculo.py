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

#No hacer de vuelta esto, separar cada clase en un archivo distinto

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
    
'''
b) Crear dos subclases Auto y Moto, que hereden de la clase Vehiculo. Las subclases deben incluir
un constructor que llame al constructor de la superclase y también deben sobrescribir el método
calcularCostoAlquiler(int dias) de la siguiente manera:
● Para Auto, el costo de alquiler se calcula incrementando un 20% el costo común.
● Para Moto, el costo de alquiler se calcula con un descuento del 15% respecto al vehículo.
'''    
class Auto (Vehiculo):
    def __init__(self, marca: str, modelo: str, precioBase: float):
        super().__init__(marca, modelo, precioBase)

    def calcularCostoAlquiler(self) -> float:
        return super().calcularCostoAlquiler() + super().calcularCostoAlquiler()*0.2
    
class Moto (Vehiculo):
    def __init__(self, marca: str, modelo: str, precioBase: float):
        super().__init__(marca, modelo, precioBase)

    def calcularCostoAlquiler(self) -> float:
        return super().calcularCostoAlquiler() + super().calcularCostoAlquiler()*0.15
    
    
if __name__ == '__main__':
    try:
        
        vehiculo = Vehiculo('Porsche', 'Carrera GT', 5000.5)
        vehiculo.dias = 5
        costo    = vehiculo.calcularCostoAlquiler()
        print(f'{vehiculo}. El costo por {vehiculo.dias} días es de: ${costo}')   
        
        
        auto = Auto('Mercedes Benz', 'SSK', 5000.5)
        auto.dias = 5
        costoAuto = auto.calcularCostoAlquiler()
        print(f'{auto}. El costo por {auto.dias} días es de: ${costoAuto} ')
        
        moto = Moto('Suzuki', 'Hayabusa', 5000.5)
        moto.dias = 5
        costoMoto = moto.calcularCostoAlquiler()
        print(f'{moto}. El costo por {moto.dias} es de ${costoMoto}')
    except Exception as e:
        print (e)  