
"""Solicita al usuario una cadena de texto y utiliza la función
frecuencia_caracteres() para contar cuántas veces aparece
cada carácter. Finalmente, muestra las frecuencias obtenidas.
"""

from funciones import frecuencia_caracteres

cadena = input("Ingresá una cadena de texto: ")

resultado = frecuencia_caracteres(cadena)

print("Frecuencia de caracteres:", resultado)
