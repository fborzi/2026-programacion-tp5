"""Programa que calcula la suma de los dígitos de cada número
entero positivo de una lista y devuelve una lista con los resultados."""

from funciones import sumatoria_digitos

numeros = [154, 27890, 111, 43]

resultado = sumatoria_digitos(numeros)

print("Lista original:", numeros)
print("Sumatoria de dígitos:", resultado)
