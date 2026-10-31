"""Resolución del ejercicio 1525.

Este archivo importa las funciones necesarias desde funciones.py.
El programa recibe una cadena de texto mediante la funcion, luego
recorre cada caracter y contabiliza sus apariciones utilizando
un diccionario.
"""

from funciones import frecuencia_caracteres

cadena = input("Ingrese una cadena de texto: ")
print(frecuencia_caracteres(cadena))
