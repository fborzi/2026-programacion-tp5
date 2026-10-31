"""Ejercicio 1512: sumatoria de dígitos de los elementos de una lista."""

from src.ejercicios.funciones import sumatoria_digitos


def main() -> None:
    """Muestra el resultado del ejemplo del enunciado."""
    numeros = [154, 27890, 111, 43]
    print(sumatoria_digitos(numeros))


if __name__ == "__main__":
    main()
