"""Ejercicio 1517: comparación y subconjuntos con conjuntos de hormonas.

Informa si horm1 comparte alguna hormona con horm2 y con horm3, si
horm2 es subconjunto de horm1, y muestra el conjunto de todas las
hormonas iterando por él.
"""

horm1: set = set(['melanina', 'oxitocina', 'dopamina'])
horm2: set = set(['testosterona', 'melanina'])
horm3: set = set(['calcinotna', 'estradiol'])

todas: set = horm1 | horm2 | horm3

print(not horm1.isdisjoint(horm2))
print(not horm1.isdisjoint(horm3))
print(horm2.issubset(horm1))

for hormona in todas:
    print(hormona)
    