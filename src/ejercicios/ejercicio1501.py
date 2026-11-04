"""Determina con el operador in si los elementos 9.6, 0, False, [0, 1],
4.0 y "p" pertenecen a la lista b, y con el método index en qué
posición se encuentra el elemento [0, 1].
"""

b: list = [4, "palabra", [0, 1], 9.6, False]

print(9.6 in b)
print(0 in b)
print(False in b)
print([0, 1] in b)
print(4.0 in b)
print("p" in b)


print(b.index([0, 1]))
