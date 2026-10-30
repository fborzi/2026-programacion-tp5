"""Programa que compara conjuntos de hormonas para determinar si
comparten elementos, comprobar si un conjunto es subconjunto de otro
y mostrar todas las hormonas mediante una iteracion."""
horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

print("horm1 y horm2 comparten alguna hormona?",
      not horm1.isdisjoint(horm2))

print("horm1 y horm3 comparten alguna hormona?",
      not horm1.isdisjoint(horm3))



print("horm2 es un subconjunto de horm1?",
      horm2.issubset(horm1))



todas_hormonas = horm1 | horm2 | horm3

print("Todas las hormonas:")

for hormona in todas_hormonas:
    print(hormona)
