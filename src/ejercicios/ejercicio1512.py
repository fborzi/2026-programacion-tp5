def suma_digitos(n):
    """
    Dado un número entero n, retorna la suma de sus dígitos.
    
    Args:
        n (int): Un número entero positivo.
        
    Returns:
        int: La suma de todos los dígitos de n.
    """
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma


def sumatoria_digitos(lista):
    """
    Dada una lista de números enteros positivos, retorna una lista con la 
    suma de los dígitos de cada uno de los números.
    
    Args:
        lista (list): Una lista de números enteros positivos.
        
    Returns:
        list: Una lista que contiene las sumas de los dígitos de cada elemento.
    """
    resultado = []
    for numero in lista:
        resultado.append(suma_digitos(numero))
        
    return resultado