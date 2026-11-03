
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

"""Agregamos 11 y 12 al conjunto"""

numeros.add(11)
numeros.add(12)

"""Con update agregamos varios numeros a la vez, con range le damos el rango de numeros"""

numeros.update(range(30, 36))

""" Agregamos los ultimos dos numeros, con update """
numeros.update([232, -264])

print("a. No es posible obtener el primer y último elemento por posición porque los conjuntos no tienen orden.")

print(7 in numeros)
print(20 in numeros)
print(len(numeros))

