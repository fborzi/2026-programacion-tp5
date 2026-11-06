productos = {}

while True:
    codigo = input("Código de producto (-1 para terminar): ").strip()
    if codigo == "-1":
        break
    tipo = input("Tipo ('lácteo', 'almacén', 'verdulería', 'limpieza', 'carnicería', 'otros'): ").strip().lower()
    descripcion = input("Descripción: ").strip()
    stock_act = int(input("Stock actual: "))
    stock_min = int(input("Stock mínimo: "))
    precio = float(input("Precio unitario: "))

    productos[codigo] = {
        "tipo": tipo,
        "descripcion": descripcion,
        "stock_actual": stock_act,
        "stock_minimo": stock_min,
        "precio": precio
    }

p_124_vender = "124" in productos and productos["124"]["stock_actual"] >= 1
print("a. ¿Es posible vender una unidad de 124?:", p_124_vender)

print("b. Productos por debajo del stock mínimo:")
for cod, info in productos.items():
    if info["stock_actual"] < info["stock_minimo"]:
        print(f"  Código: {cod}, Descripción: {info['descripcion']}")

lacteos = sum(1 for info in productos.values() if info["tipo"] == "lácteo")
print("c. Cantidad de productos lácteos:", lacteos)

almacen = [info for info in productos.values() if info["tipo"] == "almacén"]
if almacen:
    menor_almacen = min(almacen, key=lambda x: x["stock_actual"])
    print("d. Producto de almacén con menor stock:", menor_almacen["descripcion"])

if "3148" in productos:
    print("e. Descripción del producto 3148:", productos["3148"]["descripcion"])
else:
    print("e. El producto 3148 no existe.")
unidades_por_tipo = {}
for info in productos.values():
    unidades_por_tipo[info["tipo"]] = unidades_por_tipo.get(info["tipo"], 0) + info["stock_actual"]

if unidades_por_tipo:
    tipo_menor = min(unidades_por_tipo, key=unidades_por_tipo.get)
    print("f. Tipo con menor cantidad de unidades disponibles:", tipo_menor)

def procesar_pedido(pedido, productos_dict):
    monto_total = 0.0
    vendidos = []
    for cod in pedido:
        if cod in productos_dict and productos_dict[cod]["stock_actual"] >= 1:
            monto_total += productos_dict[cod]["precio"]
            productos_dict[cod]["stock_actual"] -= 1
            vendidos.append(cod)
    return monto_total, vendidos

pedido_ejemplo = ["124", "3148", "124"]
monto, vendidos = procesar_pedido(pedido_ejemplo, productos)
print("g. Monto total a pagar:", monto)
print("   Productos vendidos:", vendidos)