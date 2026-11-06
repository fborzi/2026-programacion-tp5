
a = [False, 1, 'dos', 3.0, 'ix', (5), [3, 3], True]


print(a[0])
print(a[-1])
del a[0]
del a[-3:]
a.insert(0, 9)
a[a.index('ix')] = 4
a.append(5)
a[0:4:1]
a.append(a[:])
'dos' in a
3.0 in a
a.count(1)
a.count(4)
for i in a:
    print(a)

for i in reversed(a):
    print(i)
