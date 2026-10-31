"""Ejercicio 1530: compresión y descompresión de texto con RLE."""

from src.ejercicios.funciones import (
    comprimir_rle,
    descomprimir_rle,
    tasa_compresion,
)


def main() -> None:
    """Comprime, descomprime y calcula la tasa de un texto ingresado."""
    texto = input("Ingrese un texto: ")
    comprimido = comprimir_rle(texto)
    tasa, efectiva = tasa_compresion(texto, comprimido)
    print(f"a. Comprimido: {comprimido}")
    print(f"b. Descomprimido: {descomprimir_rle(comprimido)}")
    print(f"c. Reducción: {tasa:.2f}% - ¿Fue efectiva? "
          f"{'Sí' if efectiva else 'No'}")


if __name__ == "__main__":
    main()
