"""Carga nombres por teclado con la función cargar_nombres y luego
imprime los elementos de la lista iterando por ella.
"""

from funciones import cargar_nombres

nombres: list = cargar_nombres()

for elemento in nombres:
    print(elemento)
    