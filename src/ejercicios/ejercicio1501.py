
"""Ejercicio 1501: pertenencia y búsqueda de índices en listas."""


def main() -> None:
    """Comprueba la pertenencia de elementos y busca un índice."""
    elementos: list[object] = [4, "palabra", [0, 1], 9.6, False]
    valores: list[object] = [9.6, 0, False, [0, 1], 4.0, "p"]

    print("Apartado A: Pertenencia a la lista")

    for valor in valores:
        pertenece: bool = valor in elementos
        print(f"{valor}: {pertenece}")

    print("Apartado B: Búsqueda de índice")

    indice: int = elementos.index([0, 1])
    print(f"El elemento [0, 1] está en el índice {indice}")


if __name__ == "__main__":
    main()
