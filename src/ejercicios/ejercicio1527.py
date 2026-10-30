"""Registra los productos de un supermercado mediante un diccionario.
La carga finaliza al ingresar el código -1.

El programa:
- Verifica si se puede vender el producto 124.
- Lista los productos bajo el stock mínimo.
- Cuenta los productos lácteos.
- Busca el producto de almacén con menor stock.
- Consulta la descripción del producto 3148.
- Determina qué tipo de producto tiene menos unidades.
- Procesa un pedido, calcula el total, descuenta el stock
  vendido y muestra los códigos vendidos."""



from funciones import (
    puede_vender,
    productos_bajo_stock,
    contar_lacteos,
    almacen_menor_stock,
    buscar_descripcion,
    tipo_menor_stock,
    procesar_pedido
)

productos = {}


while True:
    entrada = input("Codigo del producto (-1 para terminar: ")

    try:
        codigo = int(entrada)
    except ValueError:
        print("Error: ingresá un código numérico.")
        continue

    if codigo == -1:
        break

    tipo = input("Tipo de producto: ").strip().lower()
    descripcion = input("Descripción: ")
    
    try:
        stock = int(input("Stock actual: "))
        stock_minimo = int(input("Stock mínimo: "))
        precio = float(input("Precio unitario: "))
    except ValueError:
        print("Error: stock, stock mínimo y precio deben ser números.")
        continue

    productos[codigo] = {
        "tipo": tipo,
        "descripcion": descripcion,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "precio": precio
    }

print("\na. ¿Se puede vender el producto 124?")

if puede_vender(productos, 124):
    print("Sí, se puede vender.")
else:
    print("No se puede vender.")


print("\nb. Productos por debajo del stock mínimo:")

bajo_stock = productos_bajo_stock(productos)

if bajo_stock:
    for codigo, descripcion in bajo_stock:
        print("Código:", codigo, "- Descripción:", descripcion)
else:
    print("No hay productos por debajo del mínimo.")



print("\nc. Cantidad de productos lácteos:",
      contar_lacteos(productos))



print("\nd. Producto de almacén con menor stock:")

resultado = almacen_menor_stock(productos)

if resultado is not None:
    print("Código:", resultado[0])
    print("Descripción:", resultado[1])
else:
    print("No hay productos de almacén.")


print("\ne. Descripción del producto 3148:")

descripcion = buscar_descripcion(productos, 3148)

if descripcion is not None:
    print(descripcion)
else:
    print("El producto no existe.")



print("\nf. Tipo con menor stock total:")

tipo = tipo_menor_stock(productos)

if tipo is not None:
    print(tipo)
else:
    print("No hay productos registrados.")


print("\ng. Procesar pedido")

pedido = []

while True:
    entrada = input("Código a comprar (0 para terminar): ")

    try:
        codigo = int(entrada)
    except ValueError:
        print("Error: ingresá un código numérico.")
        continue

    if codigo == 0:
        break

    pedido.append(codigo)

total, vendidos = procesar_pedido(productos, pedido)

print("Monto total a pagar: $", round(total, 2))
print("Productos vendidos:", vendidos)
