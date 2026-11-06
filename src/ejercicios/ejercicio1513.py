
"""Ejercicio 1513: búsqueda del índice del elemento mayor.
Devuelve el índice del mayor número o None si la lista está vacía.
Prueba la función con diferentes listas numéricas."""


def indice_mayor(lista: list[int | float]) -> int | None:
    """Devuelve el índice de la primera aparición del valor máximo.

    Args:
        lista: Lista de elementos que se procesarán.
    """
    if not lista:
        return None
    mayor: int | float = max(lista)
    indice: int = lista.index(mayor)
    return indice


def main() -> None:
    """Ejecuta ejemplos de búsqueda del índice mayor."""
    print(indice_mayor([6, 1, 7, 19, 2]))
    print(indice_mayor([10, 20, 30, 40]))
    print(indice_mayor([50, 20, 10]))
    print(indice_mayor([5]))
    print(indice_mayor([-8, -3, -15, -1]))
    print(indice_mayor([]))


if __name__ == "__main__":
    main()
