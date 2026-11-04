"""Cuenta con el método count cuántas veces aparece el elemento 5 en la
lista L. Solo se cuentan los elementos de la lista, no los que están
dentro de una sublista, por lo que el 5 de [9, 5] no se cuenta.
"""

L: list = [5, 6, [9, 5], 2, 5]

print(L.count(5))
