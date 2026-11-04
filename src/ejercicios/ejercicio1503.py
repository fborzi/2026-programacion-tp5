a = [ False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True ]

#Obtener el primero y el ultimo elemento
print(a[0])
print(a[-1])

#Eliminar el primer elemento
del a[0]

#Eliminar los tres ultimos elementos
del a[-3:]

#Insertar el valor 9 al principio de la lista
a.insert(0, 9)

#Reemplazar 'ix' por 4
a[a.index('ix')] = 4

#Agregar el valor de 5 al final
a.append(5)

#Obtener los primeros tres elementos mediante una rebanada
print(a[:3])

#Insertar la lista al final de si misma
a.append(a)

#Determinar si 'dos' y 3.0 pertenecen a la lista
print('dos' in a)
print(3.0 in a)

#Contar cuantas veces aparecen 1 y 4
print(a.count(1))
print(a.count(4))

#Imprimir cada elemento de la lista iterando
for elemento in a:
    print(elemento)

#Imprimir cada elemento en orden inverso
for elemento in a[::-1]:
    print(elemento)