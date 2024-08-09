'''
La cadena de restaurantes "Delicias del Mar" desea mejorar su sistema de gestión de sus sucursales i
Requerimientos Funcionales:
1. Clase Restaurante:
○ Definir una clase llamada Restaurante que contenga como atributos: nombre del restaurante, ciudad
donde se encuentra y número de empleados.
○ Implementar un métodoobtener_numero_sucursales() que retorne el número total de sucursales de la
cadena.
○ Implementar un método calcular_costo_operativo(empleado_promedio) que calcule el costo
mensual de operación de una sucursal. Considerar un salario promedio mensual por empleado de $2000.
Crear instancias de la clase Restaurante para representar diferentes sucursales con sus respectivos nombres,
ciudades y número de empleados.
Usar el método obtener_numero_sucursales() para obtener y mostrar el número total de sucursales de la cadena.
Usar el método calcular_costo_operativo() para calcular y mostrar el costo mensual de operación de cada
sucursal creada.
'''

class Restaurante:
    
    total_sucursales = 0
    
    def __init__(self, nombre, ciudad, numero_empleados):
        self.nombre = nombre
        self.ciudad = ciudad
        self.numero_empleados = numero_empleados
        Restaurante.total_sucursales += 1
        
    @classmethod    
    def obtener_numero_sucursales(cls):
        return  cls.total_sucursales
    
    def calcular_costo_operativo(self):
        salario_promedio = 2000
        return self.numero_empleados * salario_promedio
    
#--Testeo

#---Creo sucursales
sucursal1 = Restaurante('Delicias del Mar', 'Mar del Plata', 10)
sucursal2 = Restaurante('Delicias del Mar', 'Mar del Plata', 20)

#---Numero total de sucursales
print(f'Numero total de sucursales: {Restaurante.obtener_numero_sucursales()}')

#---Costo operativo
print(f'Costo operativo de la sucursal 1: {sucursal1.calcular_costo_operativo()}')
print(f'Costo operativo de la sucursal 2: {sucursal2.calcular_costo_operativo()}')

