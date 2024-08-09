'''
Una cadena de restaurantes llamada "Delicioso Sabor" desea implementar un sistema de gestión de pedidos
automatizado para mejorar la eficiencia en el manejo de sus ventas y optimizar el control de su inventario.
Requerimientos del Sistema:

1. Clase Producto:
○ Cada producto en el menú del restaurante debe ser representado por la clase Producto.
○ Los productos deben tener un nombre, precio unitario y cantidad inicial en stock.
○ Se debe poder actualizar la cantidad en stock de cada producto conforme se realicen pedidos.

2. Clase Pedido:
○ La clase Pedido debe registrar los detalles de cada pedido realizado por los clientes.
○ Cada pedido debe contener un número único de identificación, una lista de productos solicitados y su
estado actual.
○ Se debe calcular el costo total del pedido, aplicando un descuento global del 10% por defecto.
○ Se debe poder actualizar el estado de los pedidos a medida que progresan en su preparación y
entrega.
'''    
class Pedido:
    def __init__ (self, id, productos, estado):
        self.id = id
        self.productos = productos
        self.estado = estado
    
    def calcular_costo_total(self):
        costo_total = 0
        for producto in self.productos:
            costo_total += producto.precio_unidad
            producto.cantidad_stock -= 1
        costo_total *= 0.9
        return costo_total
    
    def actualizar_estado(self, estado):
        self.estado = estado
        return f'El estado del pedido {self.id} ha sido actualizado a {estado}'
    
    
    
    