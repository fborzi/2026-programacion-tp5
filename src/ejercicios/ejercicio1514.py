
# Ejercicio 1514: busqueda de dos sumandos en una lista.
""" creamos una lista de numero y indico el resultado que
 quiero encontrar y llamo a la funcion para buscar dos sumandos y lo imprimimos    """

from funciones import dos_sumandos

numeros = [2, 7, 11, 15]
objetivo = 9
posiciones = dos_sumandos(numeros, objetivo)
print(posiciones)
