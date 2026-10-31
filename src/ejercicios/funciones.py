def dos_minimos(lista):
    """
    1507
    esta funcion se llama dos minimos ya que pide que reciba una lista de elementos
    que se comparen entre si y devuelva los dos valores menores encontrados,si tiene menos de dos
    elementos que devuelva none por cada elemento faltante 
    args:
    dos_minimos : integer
    returns: Integer 
    """

    if len(lista) == 0:
        return (None, None)

    if len(lista) == 1:
        return (lista[0], None)

    minimo1 = min(lista)
    lista.remove(minimo1)
    minimo2 = min(lista)

    return (minimo1, minimo2)

def digitos(numero):
    """
    1509
    esta funcion pide que retorne una lista una lista con los numeros ingresados 
    args: 
    digitos: Integer 
    returns: lista
    """
    lista = []

    for digito in str(numero):
        lista.append(int(digito))

    return lista

def ocurrencias(lista):
    """
    1511
    esta funcion pide recibir una lista y retornar una lista que contiene listas formadas por cada elemento
    de la lista junto con el numero de ocurrencias contiguas de ese elemento de la lista con el orden q aparecieron
    args:
    ocurrencias : integer 
    returns: resultado
    """
    resultado = []

    for elemento in lista:
        if len(resultado) > 0 and resultado[-1][0] == elemento:
            resultado[-1][1] += 1
        else:
            resultado.append([elemento, 1])

    return resultado

def indice_mayor(lista):
    """
    1513
    esta funcion pide retornar el indice en el cual se encuentre el numero mayor de la lista 
    args:
    indice_mayor: lista - integer
    returns: indice - Integer
    """
    mayor = lista[0]
    indice = 0

    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i

    return indice

def obtenerCiudad(personas, DNI):
    """1515 3 funciones 
    esta funcion pide que con el dni y la lista de personas retorne donde vive
    args:
    obtenerCiudad: String
    returns: String
    """
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]


def obtenerProvincia(personas, ciudades, DNI):
    """esta funcion pide que dadas las dos listas y el dni de una persona retorne la provincia donde vive
    se debe utilizar la funcion anterior osea obtenerCiudad
    args:
    obtenerProvincia: String - Integer
    returns: String
    """
    ciudad = obtenerCiudad(personas, DNI)

    for dato in ciudades:
        if dato[0] == ciudad:
            return dato[1]


def contarPoblacion(personas, ciudades, provincia):
    """ esta funcion pide que dadas las listas y una provincia informe cuantas personas viven en esa 
    provincia, se debe utilizar la funcion anterior osea obtenerProvincia
    args: 
    obtenerPoblacion: String
    returns: Integer

    """
    contador = 0

    for persona in personas:
        DNI = persona[1]

        if obtenerProvincia(personas, ciudades, DNI) == provincia:
            contador += 1

    return contador

def frecuencia_caracteres(cadena):
    """ejercicio 1525
    esta funcion pide una cadena de texto y retorna la cantidad de veces que aparecen cada uno de los
    caracteres de la cadena, la frecuencia. 
    args:
    frecuencia_caracteres: String
    returns: Integer
    """
    frecuencias = {}

    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1

    return frecuencias


def sucesion_mira_y_deci(n):
    """ejercicio 1529 
    esta funcion pide los primeros n numeros de la sucesion Mira y Deci donde cada numero se obtiene
    contando las repeticiones consecutivas de los digitos del numero anterior 
    args: 
    sucesion_mira_y_deci: Integer 
    returns: Integer 
    """
    sucesion = [1]

    for i in range(n - 1):
        anterior = str(sucesion[-1])
        nuevo = ""
        contador = 1

        for j in range(1, len(anterior)):
            if anterior[j] == anterior[j - 1]:
                contador += 1
            else:
                nuevo += str(contador) + anterior[j - 1]
                contador = 1

        nuevo += str(contador) + anterior[-1]
        sucesion.append(int(nuevo))

    return sucesion
