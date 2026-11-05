from funciones import  leer_productos, se_puede_vender, productos_bajo_minimo, cantidad_lacteos, almacen_menor_stock, descripcion_producto, tipo_menor_stock, procesar_pedido



productos = leer_productos()
print("a.", se_puede_vender(productos, 124))
print("b.", productos_bajo_minimo(productos))
print("c.", cantidad_lacteos(productos))
print("d.", almacen_menor_stock(productos))
print("e.", descripcion_producto(productos, 3148))
print("f.", tipo_menor_stock(productos))
total, vendidos = procesar_pedido(productos, [124, 3148, 124])
print("g.", total, vendidos)
