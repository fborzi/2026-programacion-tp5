"""Resolución del ejercicio 1513.
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Se recibe una lista de numero y retorna el indice correspondiente al elemento
de mayor valor. Si existen varios elementos con el mismo valor maximo, debe definirse
si se devuelve la primera aparicion o la ultima.
"""
from funciones import indice_mayor

numeros = [6, 1, 7, 19, 21]
indice = indice_mayor(numeros)
print("Lista:", numeros)
print("Índice del elemento mayor:", indice)
