#ejercicio 1501: comprobar si un elemento pertenece a una lista.
def pertenece(lista: list, elemento) -> bool:
    """
    Comprueba si un elemento se encuentra en una lista.
    Args:
        lista: lista que queremos consultar.
        elemento: elemento que queremos buscar.
    Returns: 
        True si pertenece a la lista y False si no pertenece.
    """
    
    return elemento in lista

def buscar_indice(lista: list, elemento) -> int:
    """
    Devuelve la posicion de un elemento dentro de una lista.
    Args: 
        lista: lista donde buscamos.
        elemento: elemento que queremos encontrar.
    Returns:
        el indice de la primera aparicion del elemento.
    """
    if elemento in lista:
        return lista.index(elemento)
    return -1
