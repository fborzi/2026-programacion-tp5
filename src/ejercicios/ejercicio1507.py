"""Ejercicio 1507: búsqueda de los dos elementos menores."""


def dos_minimos(
    lista: list[int | float]
) -> tuple[int | float | None, int | float | None]:
    """Devuelve los dos elementos menores de una lista numérica."""
    if not lista:
        return None, None

    ordenada = sorted(lista)

    if len(ordenada) == 1:
        return ordenada[0], None

    return ordenada[0], ordenada[1]


def main() -> None:
    """Ejecuta ejemplos de búsqueda de mínimos."""
    print(dos_minimos([23, 456, 12, 16, -4, 56]))
    print(dos_minimos([4]))
    print(dos_minimos([]))
    print(dos_minimos([2, 2, 5]))


if __name__ == "__main__":
    main()
