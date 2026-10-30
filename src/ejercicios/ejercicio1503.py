
# EJERCICIO 1503 - OPERACIONES Y MUTACION SOBRE LISTAS

# Lista original
a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]


# A) Obtener el primero y el ultimo elemento
print("\nA) PRIMER Y ULTIMO ELEMENTO")

print("Primer elemento:", a[0])
print("Ultimo elemento:", a[-1])


# B) Eliminar el primer elemento
print("\nB) ELIMINAR EL PRIMER ELEMENTO")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

del a[0]

print("Lista resultante:", a)


# C) Eliminar los tres ultimos elementos
print("\nC) ELIMINAR LOS TRES ULTIMOS ELEMENTOS")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

del a[-3:]

print("Lista resultante:", a)


# D) Insertar el valor 9 en el primer lugar
print("\nD) INSERTAR EL VALOR 9 EN EL PRIMER LUGAR")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

a.insert(0, 9)

print("Lista resultante:", a)


# E) Reemplazar el valor 'ix' por el valor 4
print("\nE) REEMPLAZAR 'ix' POR 4")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

a[a.index('ix')] = 4

print("Lista resultante:", a)


# F) Agregar el valor 5 al final de la lista
print("\nF) AGREGAR EL VALOR 5 AL FINAL")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

a.append(5)

print("Lista resultante:", a)


# G) Obtener mediante una rebanada los primeros 3 elementos
print("\nG) OBTENER LOS PRIMEROS 3 ELEMENTOS")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

print("Primeros 3 elementos:", a[:3])


# H) Insertar la lista al final de la misma lista
print("\nH) INSERTAR LA LISTA DENTRO DE SI MISMA")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

a.append(a)

print("La lista contiene una referencia a si misma:", a[-1] is a)
print("Lista resultante:", a)


# I) Determinar si 'dos' y 3.0 pertenecen a la lista
print("\nI) COMPROBAR PERTENENCIA A LA LISTA")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

if 'dos' in a:
    print("'dos' pertenece a la lista")
else:
    print("'dos' no pertenece a la lista")

if 3.0 in a:
    print("3.0 pertenece a la lista")
else:
    print("3.0 no pertenece a la lista")


# J) Determinar cuantas veces aparecen 1 y 4
print("\nJ) CONTAR LAS APARICIONES DE 1 Y 4")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

print("Cantidad de veces que aparece el 1:", a.count(1))
print("Cantidad de veces que aparece el 4:", a.count(4))


# K) Imprimir cada elemento de la lista (iterando)
print("\nK) RECORRER LA LISTA EN ORDEN NORMAL")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

for elemento in a:
    print(elemento)


# L) Imprimir cada elemento de la lista en forma inversa
print("\nL) RECORRER LA LISTA EN ORDEN INVERSO")

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

for elemento in reversed(a):
    print(elemento)
