def digitos_repetidos(n):
    """
    Dado un número n, retorna una lista conteniendo los dígitos que se repiten en n. 
    Cada dígito aparece una única vez en la lista, aunque se repita varias veces.
    
    Args:
        n (int): Un número entero a evaluar.
        
    Returns:
        list: Una lista con los dígitos enteros que se encuentran repetidos.
    """
    s = str(abs(n))
    
    vistos = set()
    repetidos = set()
    
    for digito in s:
        if digito in vistos:
            repetidos.add(int(digito))
        else:
            vistos.add(digito)
            
    return list(repetidos)