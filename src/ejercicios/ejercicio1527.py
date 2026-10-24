"""ejercicio  1527 control de inventario y ventas de Supermercado Coto
carga los productos en un diccionario con el codigo como clave y
resuelve las consultas de stock, tipos y descripciones. Procesa un
pedido de ejemplo calculando el monto a pagar y los productos
vendidos, y reduce el stock de lo vendido.
"""

from funciones import (
    cargar_productos,
    codigo_menor_stock,
    contar_tipo,
    procesar_pedido,
    productos_bajo_minimo,
    se_puede_vender,
    tipo_menor_stock,
)

productos: dict = cargar_productos()
pedido: list = [124, 3148, 124, 124]

print(se_puede_vender(productos, 124))

print(productos_bajo_minimo(productos))

print(contar_tipo(productos, "lácteo"))

print(codigo_menor_stock(productos, "almacén"))

if 3148 in productos:
    print(productos[3148][1])
else:
    print("No existe un producto con codigo 3148")

print(tipo_menor_stock(productos))

venta: tuple = procesar_pedido(productos, pedido)
print(f"Monto total a pagar: {venta[0]}")
print(f"Productos vendidos: {venta[1]}")
