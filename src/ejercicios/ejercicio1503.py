""" Sobre la lista a se obtienen elementos por índice y por rebanada, se
eliminan, insertan, reemplazan y agregan elementos, se verifica la
pertenencia y la cantidad de apariciones, y se recorre la lista en
orden y en forma inversa.
"""

a: list = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

print(a[0], a[-1])

del a[0]

del a[-3:]

a.insert(0, 9)

a[a.index('ix')] = 4

a.append(5)

print(a[:3])

a.append(a)

print('dos' in a, 3.0 in a)

print(a.count(1), a.count(4))

for elemento in a:
    print(elemento)

for elemento in a[::-1]:
    print(elemento)
