# Ejercicio 1518 identificacion de dígitos repetidos en un numero
"""Este código identifica los dígitos que se repiten en un 
numero entero ingresado por el usuario."""
from funciones import digitos_repetidos

numero = int(input("Ingrese un número entero: "))
print("Dígitos repetidos:", digitos_repetidos(numero))
