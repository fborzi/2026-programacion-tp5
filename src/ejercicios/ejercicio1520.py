"""Ejercicio 1520: análisis de palabras y letras repetidas en un texto."""

from src.ejercicios.funciones import contar_palabras, letras_repetidas


def main() -> None:
    """Pide un texto e informa palabras y letras repetidas."""
    texto = input("Ingrese un texto: ")
    print(f"a. Cantidad de palabras: {contar_palabras(texto)}")
    print("b. Letras repetidas por palabra:")
    for palabra in texto.split():
        repetidas = letras_repetidas(palabra)
        if len(repetidas) > 0:
            print(f"   {palabra}: {', '.join(repetidas)}")


if __name__ == "__main__":
    main()
