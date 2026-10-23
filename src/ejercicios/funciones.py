#1502 ejercicio: conteo de elementos de una lista

def contar_elementos(lista: list, elemento: int) -> int:
    """cuenta cuantas veces aparece un elemento en una lista.
    args:
        lista: lista de elementos
        elemento: elemento a contar
    returns:
        int: cantidad de veces que aparece el elemento en la lista"""
    return lista.count(elemento)