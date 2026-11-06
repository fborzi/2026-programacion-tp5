"""Ejercicio 1505: conversión de nombres a mayúsculas."""


def convertir_a_mayusculas(nombres: list[str]) -> list[str]:
    """Devuelve una nueva lista con todos los nombres en mayúsculas.

    Args:
        nombres: Lista de nombres que se convertirán a mayúsculas.
    """
    nombres_mayusculas: list[str] = []

    for nombre in nombres:
        nombres_mayusculas.append(nombre.upper())

    return nombres_mayusculas


def main() -> None:
    """Carga nombres y muestra una nueva lista en mayúsculas."""
    nombres: list[str] = []
    nombre = input("Ingrese un nombre (Enter para terminar): ")

    while nombre != "":
        nombres.append(nombre)
        nombre = input("Ingrese un nombre (Enter para terminar): ")

    nombres_mayusculas = convertir_a_mayusculas(nombres)

    print("Lista original:", nombres)
    print("Lista en mayúsculas:", nombres_mayusculas)


if __name__ == "__main__":
    main()
