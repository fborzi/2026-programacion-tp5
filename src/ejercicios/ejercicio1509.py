"""Este programa descompone un número entero en una lista de dígitos.
"""

from funciones import digitos

numero = str(input("Ingrese un numero: "))
resultado = digitos(numero)
print(resultado)