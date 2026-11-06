a = [False, 1, 'dos', 3.0, 'ix', (5), [3, 3], True]

b = []

for x in a:
    if isinstance(x, str):
        b.append(x.upper())
    else:
        b.append(x)
