def dos_sumandos(lista, resultado):
    """
    Dada una lista de números y un número objetivo (resultado), retorna una nueva 
    lista con dos índices de elementos cuya suma da como resultado dicho número. 
    No se puede utilizar el mismo elemento dos veces.
    
    Args:
        lista (list): Una lista de números.
        resultado (int o float): El valor numérico objetivo que debe sumar la pareja.
        
    Returns:
        list: Una lista con los dos índices de los elementos que suman el resultado.
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
                
    return []  