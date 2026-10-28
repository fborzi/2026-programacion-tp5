"""Pertenencia y busqueda de indices en listas"""

b = [4,"palabra",[0,1],9.6,False]
"""Intruccion para determinar si los siguientes elementos se encuentran en la lista"""

print(9.6 in b)
print(0 in b)
print(False in b)
print([0,1] in b)
print(4.0 in b)
print("p" in b)


""" Intruccion para determinar en que poscioin se encu
entra el elemento en la lista"""

print(b.index([0,1]))