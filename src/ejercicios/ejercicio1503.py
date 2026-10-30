"""
Importamos las funciones creadas en el ejercicio 1501.
Creamos la lista indicada en la consigna.
"""
from funciones import pertenece, buscar_indice

a = [False, 1, "dos", 3.0, "ix", (5,), [3, 3], True]

print("a. Primer elemento:", a[0])
print("   Último elemento:", a[-1])
print("b. Sin el primer elemento:", a[1:])
print("c. Sin los tres últimos elementos:", a[:-3])

lista_d = a.copy()
lista_d.insert(0, 9)
print("d. Insertar 9 al principio:", lista_d)

indice = buscar_indice(a, "ix")

lista_e = a.copy()
if indice != -1:
    lista_e[indice] = 4
print("e. Reemplazar 'ix' por 4:", lista_e)

lista_f = a.copy()
lista_f.append(5)
print("f. Agregar 5 al final:", lista_f)
print("g. Primeros tres elementos:", a[:3])

lista_h = a.copy()
lista_h.append(lista_h)
print("h. La lista se contiene a sí misma:", lista_h[-1] is lista_h)
print("i. ¿'dos' pertenece?:", pertenece(a, "dos"))
print("   ¿3.0 pertenece?:", pertenece(a, 3.0))
print("j. Cantidad de veces que aparece 1:", a.count(1))
print("   Cantidad de veces que aparece 4:", a.count(4))
print("k. Elementos de la lista:")

for elemento in a:
    print(elemento)
print("l. Elementos en orden inverso:")

for elemento in reversed(a):
    print(elemento)