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

# Testeo de las clases Pedido y Producto

from producto import Producto
from pedido import Pedido

# Crear productos
producto1 = Producto('Pizza', 10, 100)
producto2 = Producto('Pringles', 5, 50)
producto3 = Producto('Coca', 2, 200)

# Crear pedido
pedido1 = Pedido(1, [producto1, producto2], 'En preparación')
pedido2 = Pedido(2, [producto3], 'Entregado')
pedido3 = Pedido(3, [producto1, producto3], 'En preparación')

# Test
print(f'Stock de {producto1.nombre}: {producto1.cantidad_stock}')
print(f'Stock de {producto2.nombre}: {producto2.cantidad_stock}')
print(f'Stock de {producto3.nombre}: {producto3.cantidad_stock}')

print(f'Costo total del pedido 1: {pedido1.calcular_costo_total()}')
print(f'Costo total del pedido 2: {pedido2.calcular_costo_total()}')
print(f'Costo total del pedido 3: {pedido3.calcular_costo_total()}\n')

print(pedido1.actualizar_estado('Entregado'))

#Re-chequeo los stocks
print(f'\nStock de {producto1.nombre}: {producto1.cantidad_stock}')
print(f'Stock de {producto2.nombre}: {producto2.cantidad_stock}')
print(f'Stock de {producto3.nombre}: {producto3.cantidad_stock}')