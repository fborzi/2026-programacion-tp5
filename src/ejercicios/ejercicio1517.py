horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

# a) Verificar si comparten alguna hormona
print(horm1.isdisjoint(horm2))
print(horm1.isdisjoint(horm3))

# b) Verificar si horm2 es subconjunto de horm1
print(horm2.issubset(horm1))

# c) Informar todas las hormonas
for hormona in horm1 | horm2 | horm3:
    print(hormona)