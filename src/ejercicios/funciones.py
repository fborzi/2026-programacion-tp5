def dos_minimos(lista):
    """Devuelve los dos elementos más pequeños de una lista
    args: recibe numeros en la lista
    return: retorna none por cada elemento faltante"""
    if len(lista) < 2:
        return [None, None]
    else:
        min1 = min(lista)
        lista.remove(min1)
        min2 = min(lista)
        return [min1, min2]


"""Digitos
args:Recibe numeros por parametros
return:retorna la lista pasada por parametro"""

def digitos(numero):
    resultado=[]
    for caracter in str(numero):
        resultado.append(int(caracter))
    return resultado