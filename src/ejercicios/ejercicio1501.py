"""Programa que determina si ciertos elementos pertenecen a una lista,
utilizando el operador in para comprobar la presencia de cada elemento."""

b = [4, "palabra", [0, 1], 9.6, False]

print(9.6 in b)
print(0 in b)
print(False in b)
print([0, 1] in b)
print(4.0 in b)
print("p" in b)


print(b.index([0, 1]))