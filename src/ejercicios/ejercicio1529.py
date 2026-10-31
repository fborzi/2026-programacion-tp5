"""Resolución del ejercicio 1529.

Este archivo importa las funciones necesarias desde funciones.py 
Este ejercicio permite practicar la generacion de sucesiones numericas
mediante algoritmos, el analisis de cadena de texto y el conteo de
caracteres consecutivos.
"""

from funciones import sucesion_mira_y_deci

n = int(input("Cantidad de términos a generar: "))
print(sucesion_mira_y_deci(n))