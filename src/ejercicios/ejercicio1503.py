
"""Ejercicio 1503: operaciones y mutación sobre listas.
     a. Obtener el primero y el último elemento
     b. Eliminar el primer elemento
     c. Eliminar los tres últimos elementos
     d. Insertar el valor 9 al principio
     e. Reemplazar 'ix' por 4
     f. Agregar el valor 5 al final
     g. Obtener los primeros tres elementos
     h. Insertar la lista al final de sí misma
     i. Comprobar pertenencia de 'dos' y 3.0
     j. Contar las apariciones de 1 y 4
     k. Imprimir cada elemento
     l. Imprimir los elementos en orden inverso

"""


def main() -> None:
    """Realiza operaciones de consulta y modificación sobre una lista."""
    a: list[object] = [
        False, 1, "dos", 3.0, "ix", (5,), [3, 3], True
    ]
    print("Lista original:", a)
    print("a. Primer elemento:", a[0])
    print("a. Último elemento:", a[-1])
    a.pop(0)
    print("b. Lista:", a)
    del a[-3:]
    print("c. Lista:", a)
    a.insert(0, 9)
    print("d. Lista:", a)
    indice: int = a.index("ix")
    a[indice] = 4
    print("e. Lista:", a)
    a.append(5)
    print("f. Lista:", a)
    primeros_tres: list[object] = a[:3]
    print("g. Primeros tres elementos:", primeros_tres)
    a.append(a.copy())
    print("h. Lista:", a)
    print("i. 'dos' pertenece:", "dos" in a)
    print("i. 3.0 pertenece:", 3.0 in a)
    print("j. Cantidad de 1:", a.count(1))
    print("j. Cantidad de 4:", a.count(4))
    print("k. Elementos:")
    for elemento in a:
        print(elemento)
    print("l. Elementos en orden inverso:")
    for elemento in reversed(a):
        print(elemento)


if __name__ == "__main__":
    main()
