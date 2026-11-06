"""Ejercicio 1518: identificación de dígitos repetidos en un número."""

from src.ejercicios.funciones import digitos_repetidos


def main() -> None:
    """Pide un número y muestra sus dígitos repetidos."""
    numero = int(input("Ingrese un número entero: "))
    print(f"Dígitos repetidos: {digitos_repetidos(numero)}")


if __name__ == "__main__":
    main()
