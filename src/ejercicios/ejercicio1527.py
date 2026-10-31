productos = {}

codigo = int(input("Ingrese el código del producto (-1 para finalizar): "))

while codigo != -1:
    tipo = input("Ingrese el tipo de producto: ")
    descripcion = input("Ingrese la descripcion: ")
    stock = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock minimo: "))
    precio = float(input("Ingrese el precio unitario: "))

    productos[codigo] = [tipo, descripcion, stock, stock_minimo, precio]

    codigo = int(input("Ingrese el código del producto (-1 para finalizar): "))


if 124 in productos and productos[124][2] > 0:
    print("Se puede vender una unidad del producto 124")
else:
    print("No se puede vender una unidad del producto 124")



for codigo, datos in productos.items():
    if datos[2] < datos[3]:
        print("codigo:", codigo, "- Descripcion:", datos[1])



cantidad_lacteos = 0

for datos in productos.values():
    if datos[0] == "lácteo":
        cantidad_lacteos += 1

print("Cantidad de productos lácteos:", cantidad_lacteos)



menor_stock = None
codigo_menor = None

for codigo, datos in productos.items():
    if datos[0] == "almacen":
        if menor_stock is None or datos[2] < menor_stock:
            menor_stock = datos[2]
            codigo_menor = codigo

if codigo_menor is not None:
    print("Producto de almacén con menor stock:")
    print("Codigo:", codigo_menor)
    print("Descripcion:", productos[codigo_menor][1])
    print("Stock:", menor_stock)
else:
    print("No hay productos de almacen")



if 3148 in productos:
    print("Descripcion del producto 3148:", productos[3148][1])
else:
    print("No existe el producto 3148")


unidades_por_tipo = {}

for datos in productos.values():
    tipo = datos[0]
    stock = datos[2]

    if tipo in unidades_por_tipo:
        unidades_por_tipo[tipo] += stock
    else:
        unidades_por_tipo[tipo] = stock

if len(unidades_por_tipo) > 0:
    tipo_menor = min(unidades_por_tipo, key=unidades_por_tipo.get)
    print("Tipo con menor cantidad de unidades disponibles:", tipo_menor)
    print("Unidades disponibles:", unidades_por_tipo[tipo_menor])


pedido = [124, 3148, 500, 124]

codigos_vendidos = []
total = 0

for codigo in pedido:
    if codigo in productos and productos[codigo][2] > 0:
        total += productos[codigo][4]
        productos[codigo][2] -= 1
        codigos_vendidos.append(codigo)

print("monto total a pagar:", total)
print("codigos de productos vendidos:", codigos_vendidos)
