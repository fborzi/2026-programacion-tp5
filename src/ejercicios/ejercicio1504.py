"""Ejercicio 1504: carga interactiva de nombres en una lista."""

from src.ejercicios.funciones import imprimir_nombres, ingresar_nombres


def main() -> None:
    """Carga nombres hasta recibir uno en blanco y los muestra."""
    nombres = ingresar_nombres()
    print("Nombres ingresados:")
    imprimir_nombres(nombres)


if __name__ == "__main__":
    main()
