"""Ejercicio 1516: operaciones básicas con conjuntos numéricos, crea
el conjunto numeros con los números del 1 al 10, agrega el 11 y
el 12, incorpora del 30 al 35 de una sola vez con update y range, y
agrega el 232 y el -264. Luego informa si el 7 y el 20 pertenecen al
conjunto y cuántos elementos tiene.

No es posible informar el primer y el último número almacenado,
porque los conjuntos no tienen orden ni índices: numeros[0] produce
un error.
"""

numeros: set = set(range(1, 11))

numeros.add(11)
numeros.add(12)
numeros.update(range(30, 36))
numeros.add(232)
numeros.add(-264)

print(7 in numeros, 20 in numeros)
print(len(numeros))
