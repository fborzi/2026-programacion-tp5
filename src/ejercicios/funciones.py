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



def ocurrencias(lista):
    """Conteo de ocurrencias contiguas
    args:Recibe una lista
    return:lista formada por cada elemento de la lista
    junto con el numero de ocurrencias contiguas"""

    if lista == []:
        return []

    en_seguimiento  = lista[0]
    contador = 1
    resultado = []

    for i in lista[1:]:
        if i == en_seguimiento:
            contador=contador + 1
        else:
            resultado.append([en_seguimiento,contador])
            en_seguimiento=i
            contador=1
    resultado.append([en_seguimiento,contador])
    return resultado
