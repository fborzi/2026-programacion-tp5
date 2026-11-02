"""Comparacion y subconjuntos con conjuntos de hormonas"""


horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcinotna', 'estradiol'])

"""Informar si horm1 comparte alguna hormona con horm2"""
print(horm1 & horm2)
"""Y con horm3?"""
print(horm1 & horm3)


"""Es un subconjunto horm2 de horm1?"""
print( horm2 in horm1 )


"""Informe de todas las hormonas iterando por conjuntos"""
for hormona in horm1:
    print(hormona)

for hormona in horm2:
    print(hormona)

for hormona in horm3:
    print(hormona)