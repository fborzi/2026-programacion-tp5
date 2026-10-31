"""Ejercicio 1504: carga interactiva de nombres en una lista."""

from src.ejercicios.funciones import cargar_nombres


def main() -> None:
    """Carga nombres hasta recibir uno en blanco y los muestra."""
    nombres = cargar_nombres()
    print("Nombres ingresados:")
    for nombre in nombres:
        print(nombre)


if __name__ == "__main__":
    main()
