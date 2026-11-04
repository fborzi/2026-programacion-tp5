"""Ejercicio 1530 compresión y descompresión de texto con algoritmo RLE
Usa las funciones comprimir_rle, descomprimir_rle y tasa_compresion.
"""

from funciones import comprimir_rle, descomprimir_rle, tasa_compresion

texto: str = "aaabbbbaac"
comprimida: list = comprimir_rle(texto)

print(comprimida)
print(descomprimir_rle(comprimida))
print(tasa_compresion(texto, comprimida))
