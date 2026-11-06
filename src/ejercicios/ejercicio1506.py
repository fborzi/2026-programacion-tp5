def minimo_elemento(lista: list) ->list: 
    """
    Recibe como parámetro una lista de elementos comparables entre sí 
    y devuelve el mínimo valor encontrado, o none si la lista estuviera vacía.

     Args:
        lista (list): Una secuencia de elementos comparables entre sí.
        
    Returns:
        any: El valor mínimo encontrado en la lista, o none si la lista está vacía.
    """
    if not lista:
        return None
    
    minimo = lista[0]
    
    for elemento in lista[1:]:
        if elemento < minimo:
            minimo = elemento
            
    return minimo                   