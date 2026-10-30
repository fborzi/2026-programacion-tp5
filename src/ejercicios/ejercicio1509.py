"""
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Separa los dígitos de un número entero y los devuelve en una lista, respetando el orden 
en que aparecen en el número. En esta implementación, el signo negativo no se incluye como dígito.
"""

from funciones import digitos
numero = int(input("Ingrese un número entero: "))
print(digitos(numero))
