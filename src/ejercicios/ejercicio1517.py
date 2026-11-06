horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

comparten_1_2 = not horm1.isdisjoint(horm2)
comparten_1_3 = not horm1.isdisjoint(horm3)
print(f"a. horm1 y horm2 comparten hormonas: {comparten_1_2}")
print(f"   horm1 y horm3 comparten hormonas: {comparten_1_3}")

es_subconjunto = horm2.issubset(horm1)
print(f"b. horm2 es subconjunto de horm1: {es_subconjunto}")

todas_hormonas = horm1 | horm2 | horm3
print("c. Conjunto de todas las hormonas (iterando):")
for h in todas_hormonas:
    print("-", h)