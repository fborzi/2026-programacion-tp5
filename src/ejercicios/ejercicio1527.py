productos = {}

codigo = int(input("Ingrese el código del producto (-1 para terminar): "))

while codigo != -1:

    tipo = input("Ingrese el tipo de producto: ")
    descripcion = input("Ingrese la descripción: ")
    stock = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock mínimo: "))
    precio = float(input("Ingrese el precio unitario: "))

    productos[codigo] = [tipo, descripcion, stock, stock_minimo, precio]

    codigo = int(input("Ingrese el código del producto (-1 para terminar): "))


if 124 in productos:

    if productos[124][2] > 0:
        print("Se puede vender una unidad del producto 124.")
    else:
        print("No hay stock del producto 124.")

else:
    print("No existe el producto 124.")


print("Productos por debajo del stock mínimo:")

for codigo in productos:

    if productos[codigo][2] < productos[codigo][3]:
        print(codigo, productos[codigo][1])


cantidad_lacteos = 0

for codigo in productos:

    if productos[codigo][0] == "lácteo":
        cantidad_lacteos = cantidad_lacteos + 1

print("Cantidad de productos lácteos:", cantidad_lacteos)


menor_stock = None
codigo_menor = None

for codigo in productos:

    if productos[codigo][0] == "almacén":

        if menor_stock == None or productos[codigo][2] < menor_stock:
            menor_stock = productos[codigo][2]
            codigo_menor = codigo

if codigo_menor != None:
    print("Producto de almacén con menor stock:")
    print(codigo_menor, productos[codigo_menor][1], menor_stock)
else:
    print("No hay productos de almacén.")


if 3148 in productos:
    print("Descripción del producto 3148:", productos[3148][1])
else:
    print("No existe el producto 3148.")


tipos = ["lácteo", "almacén", "verdulería", "limpieza", "carnicería", "otros"]

unidades = {}

for tipo in tipos:
    unidades[tipo] = 0

for codigo in productos:

    tipo = productos[codigo][0]
    stock = productos[codigo][2]

    unidades[tipo] = unidades[tipo] + stock

menor_cantidad = None
tipo_menor = None

for tipo in unidades:

    if menor_cantidad == None or unidades[tipo] < menor_cantidad:
        menor_cantidad = unidades[tipo]
        tipo_menor = tipo

print("Tipo con menor cantidad de unidades disponibles:", tipo_menor)
print("Cantidad de unidades:", menor_cantidad)


pedido = []

codigo = int(input("Ingrese el código del producto del pedido (-1 para terminar): "))

while codigo != -1:

    pedido.append(codigo)

    codigo = int(input("Ingrese otro código (-1 para terminar): "))


total = 0
vendidos = []

for codigo in pedido:

    if codigo in productos:

        if productos[codigo][2] > 0:

            total = total + productos[codigo][4]
            productos[codigo][2] = productos[codigo][2] - 1
            vendidos.append(codigo)

print("Monto total a pagar:", total)
print("Productos que pudieron venderse:", vendidos)