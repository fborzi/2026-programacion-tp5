"""Operaciones y mutilacion sobre listas"""

a = [ False, 1,'dos', 3.0, 'ix', (5,), [3, 3], True ]

"""Primer y ultimo elemento"""
print(a[0])
print(a[-1])

"""Eliminar primer elemento"""

del a[0]

"""Eliminar tres últimos elementos"""

del a[5:8]

"""Insertar un elemento en la primera posición"""

a.insert(0,9)

"""Reemplazar el elemento 'ix' por 4"""

a[a.index('ix')] = 4
print(a)

"""Agregar el elemento 5 al final de la lista"""

a.append(5)
print (a)

"""Mediante una rebanada los 3 primeros elementos"""

print(a[0:3])

"""Insertar al final de la lista la lista a en si misma"""

a.append(a)
print(a)

""" Intruccion para determinar si los siguientes elementos se encuentran en la lista"""

print('dos' in a)
print(3.0 in a)

"""Determina cuantas veces aparece el elemento 1 en la lista y el elemento 4"""
print(a.count(1))
print(a.count(4))

"""Imprimir cada elementos de la lista iterando"""

for i in a:
    print(i)

"""Imprimir cada elementos de la lista de forma inversa iterando"""

for i in (a[-1::-1]):
    print(i)