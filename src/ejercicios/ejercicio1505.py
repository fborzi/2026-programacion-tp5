"""Ejercicio 1505: conversión de elementos de una lista a mayúsculas.

Reutiliza la carga del ejercicio 1504 y produce una nueva lista con
los nombres convertidos completamente a mayúsculas.
"""

from funciones import cargar_nombres, convertir_a_mayusculas

nombres: list = cargar_nombres()
nombres_mayusculas: list = convertir_a_mayusculas(nombres)

print(nombres_mayusculas)