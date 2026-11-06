
""" Ejercicio 1511: conteo de ocurrencias contiguas.
    Agrupa elementos consecutivos iguales y cuenta sus apariciones.
    Prueba el conteo de ocurrencias contiguas."""


def ocurrencias(lista: list[object]) -> list[list[object]]:
    """Agrupa elementos consecutivos iguales y cuenta sus apariciones."""
    resultado: list[list[object]] = []
    for elemento in lista:
        if resultado and resultado[-1][0] == elemento:
            resultado[-1][1] += 1
        else:
            resultado.append([elemento, 1])
    return resultado


def main() -> None:
    """Ejecuta ejemplos de agrupación de ocurrencias."""
    lista: list[object] = [
        "z", 7, True, True, 34, "z", "z", "z", 3.14
    ]
    print(ocurrencias(lista))
    print(ocurrencias([1, 1, 2, 2, 2, 3]))
    print(ocurrencias([]))
    print(ocurrencias(["a"]))
    print(ocurrencias([5, 5, 5, 5]))


if __name__ == "__main__":
    main()
