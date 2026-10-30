"""Resolución del ejercicio 1521.
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Analiza las palabras para identificar aquellas que contienen al menos tres vocales diferentes,
cuenta las oraciones y calcula el porcentaje.
"""
from funciones import contar_vocales_distintas, cargar_lineas_hasta_asterisco

texto = cargar_lineas_hasta_asterisco()
palabras = texto.split()

cantidad_palabras = 0
for palabra in palabras:
    palabra_limpia = palabra.strip(".,;:!?¡¿()[]{}\"'")
    if contar_vocales_distintas(palabra_limpia) >= 3:
        cantidad_palabras +=1

oraciones = [parte.strip() for parte in texto.split(".") if parte.strip()]
oraciones_largas = sum(1 for oracion in oraciones if len(oracion.split()) > 5)

if oraciones:
    porcentaje = oraciones_largas / len(oraciones) * 100
else:
    porcentaje = 0

print("Palabras con al menos 3 vocales diferentes:", cantidad_palabras)
print("Cantidad de oraciones:", len(oraciones))
print("Porcentaje de oraciones con más de 5 palabras:", round(porcentaje, 2), "%")