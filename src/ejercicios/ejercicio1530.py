"""Programa que comprime un texto utilizando el método RLE,
descomprime el texto para recuperar el original y calcula la tasa
de compresión para determinar si la compresión fue efectiva."""

from funciones import comprimir_rle, descomprimir_rle, tasa_compresion

texto = input("Ingrese un texto: ")

comprimido = comprimir_rle(texto)
print("Texto comprimido:", comprimido)

descomprimido = descomprimir_rle(comprimido)
print("Texto descomprimido:", descomprimido)

tasa, efectiva = tasa_compresion(texto, comprimido)
print("Tasa de compresión:", tasa, "%")
print("¿La compresión fue efectiva?:", efectiva)
