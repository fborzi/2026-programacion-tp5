"""Ejercicio 1502: conteo de elementos en una lista."""


def main() -> None:
    """Cuenta cuántas veces aparece el elemento 5 en la lista."""
    lista = [5, 6, [9, 5], 2, 5]
    cantidad = lista.count(5)
    print(f"El elemento 5 aparece {cantidad} veces en la lista.")


if __name__ == "__main__":
    main()
