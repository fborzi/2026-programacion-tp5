
# Ejercicio 1510: eliminacion de caracteres adyacentes repetidos.
"""Este codigo elimina caracteres repetidos consecutivamente de una lista.
se solicita al usuario que ingrese una cadena de caracteres y 
se imprime la cadena resultante sin caracteres adyacentes repetidos."""

from funciones import borrar_adyacentes

texto = input("Ingrese una cadena de caracteres: ")

caracteres = list(texto)

resultado = borrar_adyacentes(caracteres)

texto_final = "".join(resultado)

print(texto_final)
