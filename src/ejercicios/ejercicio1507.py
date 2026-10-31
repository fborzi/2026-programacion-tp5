"""
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Busca los dos valores más pequeños de una lista y los devuelve en una tupla, ordenados de menor a mayor. 
Si la lista tiene menos de dos elementos, completa los valores faltantes con None.
"""

from funciones import dos_minimos

print(dos_minimos([23, 456, 12, 16, -4, 56]))
print(dos_minimos([4]))
print(dos_minimos([]))
