def dos_minimos(lista):
    """Devuelve los dos elementos más pequeños de una lista
    args: recibe numeros en la lista
    return: retorna none por cada elemento faltante"""
    if len(lista) == 0:
        return [None, None]
    if len(lista) == 1:
        return (lista[0], None)
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


def indice_mayor(lista):
    """Indice del mayor elemento
    args:Recibe una lista
    return:retorna el indice del mayor elemento de la lista"""
    if len(lista) == 0:
        return None
    else:
        mayor = max(lista)
        return lista.index(mayor)



def obtenerCiudad(personas,DNI):
    """Obtiene la ciudad de una persona a partir de su DNI
    args:Recibe una lista de personas y un DNI
    return:retorna la ciudad de la persona con el DNI """
    for persona in personas:
        if persona['DNI'] == DNI:
            return persona['ciudad']
    return None

def obtenerProvincia(personas,ciudades,DNI):
    """Obtiene la provincia de una persona a partir de su DNI
    args:Recibe una lista de personas, una lista de ciudades y un DNI
    return:retorna la provincia de la persona con el DNI dado"""
    ciudad = obtenerCiudad(personas,DNI)
    if ciudad is not None:
        for ciudad_info in ciudades:
            if ciudad_info['nombre'] == ciudad:
                return ciudad_info['provincia']
    return None

def contarPoblacion(personas,ciudades,provincia):
    """Cuenta la población de una provincia
    args:Recibe una lista de personas, una lista de ciudades y una provincia
    return:retorna la cantidad de personas que viven en la provincia dada"""
    contador = 0
    for persona in personas:
        ciudad = persona['ciudad']
        for ciudad_info in ciudades:
            if ciudad_info['nombre'] == ciudad and ciudad_info['provincia'] == provincia:
                contador += 1
                break
    return contador