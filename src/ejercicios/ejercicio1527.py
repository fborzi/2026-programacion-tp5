"""Resolución del ejercicio 1527.
El programa recibe informacion de cada producto: codigo, tipo, descripcion,
stock actual, stock minimo y precio unitario. Los datos se almacenan en una
estructura para facilitar su busqueda y administracion.
"""

def cargar_productos(productos):
    codigo = int(input("Código del producto (-1 para terminar): "))
    if codigo == -1:
        return
    tipo = input("Tipo (lácteo/almacén/verdulería/limpieza/carnicería/otros): ").strip().lower()
    descripcion = input("Descripción: ").strip()
    stock = int(input("Stock actual: "))
    minimo = int(input("Stock mínimo: "))
    precio = float(input("Precio unitario: "))
    productos[codigo] = {"tipo": tipo, "descripcion": descripcion,
                         "stock": stock, "minimo": minimo, "precio": precio}
    cargar_productos(productos)

productos = {}
cargar_productos(productos)

producto124 = productos.get(124)
print("¿Se puede vender una unidad del producto 124?:",
      bool(producto124 and producto124["stock"] >= 1))
print("Productos por debajo del stock mínimo:",
      [(c, p["descripcion"]) for c, p in productos.items() if p["stock"] < p["minimo"]])
print("Cantidad de productos lácteos:", sum(1 for p in productos.values() if p["tipo"] == "lácteo"))

almacen = [(c, p) for c, p in productos.items() if p["tipo"] == "almacén"]
menor = min(almacen, key=lambda item: item[1]["stock"], default=None)
print("Producto de almacén con menor stock:", menor)

print("Descripción del producto 3148:",
      productos[3148]["descripcion"] if 3148 in productos else "No existe")

disponibles = [(c, p) for c, p in productos.items() if p["stock"] > 0]
mas_stock = max(disponibles, key=lambda item: item[1]["stock"], default=None)
print("Producto con mayor cantidad disponible:", mas_stock)

pedido = [int(codigo.strip()) for codigo in input("Ingrese códigos del pedido separados por coma: ").split(",") if codigo.strip()]
monto_total = 0
vendidos = []
for codigo in pedido:
    producto = productos.get(codigo)
    if producto and producto["stock"] > 0:
        monto_total += producto["precio"]
        producto["stock"] -= 1
        vendidos.append(codigo)
print("Monto total a pagar:", monto_total)
print("Códigos efectivamente vendidos:", vendidos)