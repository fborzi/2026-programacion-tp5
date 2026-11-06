"""Ejercicio 1527: inventario y ventas de supermercado."""

Producto = dict[str, str | int | float]
Inventario = dict[int, Producto]


def cargar_productos() -> Inventario:
    """Carga productos hasta ingresar el código -1."""
    inventario: Inventario = {}
    continuar = True

    while continuar:
        codigo = int(input("Código del producto (-1 para finalizar): "))

        if codigo == -1:
            continuar = False
        else:
            tipo = input("Tipo de producto: ").lower()
            descripcion = input("Descripción: ")
            stock = int(input("Stock actual: "))
            minimo = int(input("Stock mínimo: "))
            precio = float(input("Precio unitario: "))

            inventario[codigo] = {
                "tipo": tipo,
                "descripcion": descripcion,
                "stock": stock,
                "minimo": minimo,
                "precio": precio
            }

    return inventario


def puede_vender(inventario: Inventario, codigo: int) -> bool:
    """Determina si hay al menos una unidad disponible.

    Args:
        inventario: Diccionario con los productos registrados.
        codigo: Código identificador del producto.
    """
    return (
        codigo in inventario
        and int(inventario[codigo]["stock"]) > 0
    )


def bajo_minimo(inventario: Inventario) -> list[tuple[int, str]]:
    """Obtiene productos con stock inferior al mínimo.

    Args:
        inventario: Diccionario con los productos registrados.
    """
    resultado: list[tuple[int, str]] = []

    for codigo, producto in inventario.items():
        if int(producto["stock"]) < int(producto["minimo"]):
            resultado.append((codigo, str(producto["descripcion"])))

    return resultado


def contar_lacteos(inventario: Inventario) -> int:
    """Cuenta los productos clasificados como lácteos.

    Args:
        inventario: Diccionario con los productos registrados.
    """
    return sum(
        1 for producto in inventario.values()
        if producto["tipo"] in ("lácteo", "lacteo")
    )


def almacen_menor_stock(inventario: Inventario) -> int | None:
    """Devuelve el código del producto de almacén con menor stock.

    Args:
        inventario: Diccionario con los productos registrados.
    """
    codigos = [
        codigo for codigo, producto in inventario.items()
        if str(producto["tipo"]) in ("almacen", "almacén")
    ]

    if not codigos:
        return None

    return min(
        codigos,
        key=lambda codigo: int(inventario[codigo]["stock"])
    )


def descripcion_producto(inventario: Inventario, codigo: int) -> str | None:
    """Busca la descripción de un producto por código.

    Args:
        inventario: Diccionario con los productos registrados.
        codigo: Código identificador del producto.
    """
    if codigo in inventario:
        return str(inventario[codigo]["descripcion"])
    return None


def tipo_menor_stock(inventario: Inventario) -> str | None:
    """Obtiene el tipo con menor cantidad total de unidades.

    Args:
        inventario: Diccionario con los productos registrados.
    """
    totales: dict[str, int] = {}

    for producto in inventario.values():
        tipo = str(producto["tipo"])
        totales[tipo] = totales.get(tipo, 0) + int(producto["stock"])

    if not totales:
        return None

    return min(totales, key=totales.__getitem__)


def procesar_pedido(
    inventario: Inventario, pedido: list[int]
) -> tuple[float, list[int]]:
    """Procesa las ventas disponibles y actualiza el stock.

    Args:
        inventario: Diccionario con los productos registrados.
        pedido: Lista de códigos de productos solicitados.
    """
    monto = 0.0
    vendidos: list[int] = []

    for codigo in pedido:
        if puede_vender(inventario, codigo):
            producto = inventario[codigo]
            monto += float(producto["precio"])
            producto["stock"] = int(producto["stock"]) - 1
            vendidos.append(codigo)

    return monto, vendidos


def main() -> None:
    """Carga el inventario y ejecuta las consultas solicitadas."""
    inventario = cargar_productos()

    print("Se puede vender el producto 124:", puede_vender(inventario, 124))
    print("Productos bajo mínimo:", bajo_minimo(inventario))
    print("Cantidad de productos lácteos:", contar_lacteos(inventario))
    print("Código de almacén con menor stock:",
          almacen_menor_stock(inventario))
    print(
        "Descripción del producto 3148:",
        descripcion_producto(
            inventario,
            3148))
    print("Tipo con menor stock:", tipo_menor_stock(inventario))

    pedido: list[int] = []
    continuar = True

    while continuar:
        codigo = int(input("Código para el pedido (-1 para terminar): "))

        if codigo == -1:
            continuar = False
        else:
            pedido.append(codigo)

    monto, vendidos = procesar_pedido(inventario, pedido)

    print("Monto total:", monto)
    print("Productos vendidos:", vendidos)
    print("Inventario actualizado:", inventario)


if __name__ == "__main__":
    main()
