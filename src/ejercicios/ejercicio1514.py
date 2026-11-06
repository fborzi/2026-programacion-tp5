"""Ejercicio 1514: búsqueda de dos sumandos en una lista."""

from src.ejercicios.funciones import dos_sumandos


def main() -> None:
    """Muestra el resultado del ejemplo del enunciado."""
    lista = [2, 7, 11, 15]
    resultado = 17
    indices = dos_sumandos(lista, resultado)
    print(f"Índices que suman {resultado}: {indices}")


if __name__ == "__main__":
    main()
