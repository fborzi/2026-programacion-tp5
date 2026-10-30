""" ejercicio 1530.
Este archivo importa las funciones necesarias desde funciones py cuando corresponde,
utiliza los datos de la consigna y muestra los resultados solicitados.
No se redefinen aqui las funciones compartidas.
"""

from funciones import comprimir_rle, descomprimir_rle, tasa_compresion

texto = input("Ingrese el texto a comprimir: ")

comprimido = comprimir_rle(texto)
descomprimido = descomprimir_rle(comprimido)
tasa, efectiva = tasa_compresion(texto, comprimido)

print("Texto original:", texto)
print("Texto comprimido:", comprimido)
print("Texto descomprimido:", descomprimido)
print("Tasa de compresión:", tasa, "%")
print("¿La compresión fue efectiva?:", efectiva)