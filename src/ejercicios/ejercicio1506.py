"""Ejercicio 1506: búsqueda del elemento mínimo en una lista."""

from src.ejercicios.funciones import minimo_elemento


def main() -> None:
    """Muestra el mínimo de los ejemplos del enunciado."""
    ejemplos = [[4, 8, 15, 16, 23, 42], "PYTHON", []]
    for ejemplo in ejemplos:
        print(f"minimo_elemento({ejemplo!r}) = {minimo_elemento(ejemplo)!r}")


if __name__ == "__main__":
    main()
