def borrar_adyacentes(lista):
    """
    Recibe una lista de caracteres (strings de longitud 1) y retorna una lista 
    en la que queda una única ocurrencia de todos los caracteres adyacentes repetidos.
    
    Args:
        lista (list): Una lista de strings de longitud 1.
        
    Returns:
        list: Una nueva lista con los caracteres adyacentes repetidos eliminados.
    """
    if not lista:
        return []
    
    resultado = [lista[0]]
    
    for elemento in lista[1:]:
        if elemento != resultado[-1]:
            resultado.append(elemento)
            
    return resultado