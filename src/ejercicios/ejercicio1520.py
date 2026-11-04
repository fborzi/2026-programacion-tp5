"""Ejercicio 1520. análisis de palabras y letras repetidas en un texto.
Lee un texto e informa la cantidad de palabras y, para cada palabra
que tenga letras repetidas, cuales son.
"""

from funciones import letras_repetidas

texto: str = input("Ingrese un texto: ")
palabras: list = texto.split()

print(f"Cantidad de palabras: {len(palabras)}")

for palabra in palabras:
    repetidas: list = letras_repetidas(palabra)
    if repetidas != []:
        print(f"Letras repetidas en {palabra.strip('.,;:')}: {repetidas}")
