horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

if horm1 & horm2:
    print("horm1 y horm2 comparten:", horm1 & horm2)
else:
    print("horm1 y horm2 no comparten hormonas")

if horm1 & horm3:
    print("horm1 y horm3 comparten:", horm1 & horm3)
else:
    print("horm1 y horm3 no comparten hormonas")

if horm2.issubset(horm1):
    print("horm2 es subconjunto de horm1")
else:
    print("horm2 no es subconjunto de horm1")

todas = horm1 | horm2 | horm3
print("Todas las hormonas:")
for hormona in todas:
    print(hormona)
