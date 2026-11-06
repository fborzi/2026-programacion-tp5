"""Ejercicio 1517: comparación de conjuntos de hormonas."""


def main() -> None:
    """Compara conjuntos y muestra sus elementos."""
    horm1: set[str] = {"melanina", "oxitocina", "dopamina"}
    horm2: set[str] = {"testosterona", "melanina"}
    horm3: set[str] = {"calcitonina", "estradiol"}

    print("a. Horm1 y horm2 comparten:", bool(horm1 & horm2))
    print("a. Horm1 y horm3 comparten:", bool(horm1 & horm3))
    print("b. Horm2 es subconjunto de horm1:", horm2 <= horm1)

    print("c. Todas las hormonas:")
    for hormona in sorted(horm1 | horm2 | horm3):
        print(hormona)


if __name__ == "__main__":
    main()
