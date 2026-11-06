"""Ejercicio 1510: eliminación de caracteres adyacentes repetidos."""

from src.ejercicios.funciones import borrar_adyacentes


def main() -> None:
    """Muestra el resultado del ejemplo del enunciado."""
    lista = ["a", "a", "*", "b", "-", "=", "c", "a"]
    print(borrar_adyacentes(lista))


if __name__ == "__main__":
    main()
