"""Programa que realiza operaciones y modificaciones sobre una lista.
Permite obtener el primero y el último elemento, eliminar e insertar
valores, reemplazar elementos, obtener rebanadas, comprobar pertenencia,
contar apariciones e imprimir los elementos en orden normal e inverso."""

lista = [False, 1, "dos", 3.0, "ix", (5,), [3, 3], True]


print(lista[0])
print(lista[-1])


del lista[0]
print(lista)


del lista[-3:]
print(lista)


lista.insert(0, "nuevo")
print(lista)


lista[1] = "reemplazo"
print(lista)


lista.append("final")
print(lista)


print(lista[:3])

lista.extend(lista)
print(lista)


print("dos" in lista)


print(lista.count("dos"))


for elemento in lista:
    print(elemento)


for elemento in reversed(lista):
    print(elemento)
