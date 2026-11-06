horm1 = set(['melanina', 'oxitocina', 'dopamina'])
horm2 = set(['testosterona', 'melanina'])
horm3 = set(['calcitonina', 'estradiol'])

print(horm1 & horm2)
print(horm1 & horm3)

print(horm2.issubset(horm1))

for hormona in horm1:
    print(hormona)