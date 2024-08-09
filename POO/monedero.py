'''
Implemente una clase Monedero que permita gestionar la cantidad de dinero que
una persona dispone en un momento dado. La clase deberá tener un constructor
que permitirá crear un monedero con una cantidad de dinero inicial y deberá
definir un método para meter dinero en el monedero, otro para sacarlo y
finalmente, otro para consultar el disponible; solo podrá conocerse la cantidad de
dinero del monedero a través de este último método. Por supuesto, no se podrá
sacar más dinero del que haya en un momento dado en el monedero
'''

class Monedero:
    def __init__(self, cantidad_inicial):
        self.cantidad = cantidad_inicial
        
    def meter_dinero(self, cantidad):
        self.cantidad += cantidad
        return print(f'Se han ingresado {cantidad} euros')
        
    def sacar_dinero(self, cantidad):
        if cantidad > self.cantidad:
            print(f"Se quiso retirar {cantidad} Euros. No hay suficiente dinero")
        else:
            self.cantidad -= cantidad
            print(f'Se han retirado {cantidad} euros')
       
       
    def consultar_disponible(self):
        return self.cantidad
    
# Test
monedero = Monedero(1000)
print(f'Disponible: {monedero.consultar_disponible()}')
monedero.meter_dinero(500)
print(f'Disponible: {monedero.consultar_disponible()}')
monedero.sacar_dinero(200)
print(f'Disponible: {monedero.consultar_disponible()}')
monedero.sacar_dinero(2000)
print(f'Disponible: {monedero.consultar_disponible()}')
monedero.meter_dinero(1000)
print(f'Disponible: {monedero.consultar_disponible()}')
monedero.sacar_dinero(100)
print(f'Disponible: {monedero.consultar_disponible()}')