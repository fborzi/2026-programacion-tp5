#ejercicio 1506

def minimo_elemento(lista):
    """
    Busca el elemento de menor valor dentro de una lista.

    Args:
        lista (list): Lista de elementos comparables entre sí.

    Returns:
        object: Devuelve el elemento mínimo de la lista.
        Si la lista está vacía, devuelve None.
    """
    if len(lista) == 0:
        return None
    
    minimo = lista[0]
    
    for elem in lista:
        if elem < minimo:
            minimo = elem
            
    return minimo
            
            
#ejercicio 1508

def piedra_papel_tijera(uno, dos):
    """
    Compara las elecciones de dos jugadores para determinar
    el resultado de una partida de piedra, papel o tijera.

    Args:
        uno (str): Elección realizada por el primer jugador.
        dos (str): Elección realizada por el segundo jugador.

    Returns:
        str: Devuelve el resultado de la partida, indicando
        si gana el primer jugador, el segundo o si hay empate.
    """
    uno = uno.lower()
    dos = dos.lower()
    
    if uno == dos:
        return 0
    if uno == "piedra" and dos == "tijera":
        return 1
    if uno == "tijera" and dos == "papel":
        return 1
    if uno == "papel" and dos == "piedra":
        return 1
    return 2

#ejercicio 1510

def borrar_adyacentes(lista):
    """
    Elimina los elementos repetidos que aparecen
    consecutivamente en una lista.

    Args:
        lista (list): Lista de elementos en la que se buscan
        repeticiones consecutivas.

    Returns:
        list: Devuelve una lista sin las repeticiones
        consecutivas, conservando un solo elemento de cada grupo.
    """
    resultado = []

    for caracter in lista:
        if resultado == [] or caracter != resultado[-1]:
            resultado.append(caracter)

    return resultado

#ejercicio 1512

def suma_digitos(n):
    """
    Calcula la suma de todos los dígitos de un número entero.

    Args:
        n (int): Número entero cuyos dígitos se quieren sumar.

    Returns:
        int: Devuelve el resultado de sumar todos los dígitos.
    """
    suma = 0
    n = str(n)

    for digito in n:
        suma = suma + int(digito)

    return suma

def sumatoria_digitos(lista):
    """
    Calcula la suma de los dígitos de cada número
    que contiene una lista.

    Args:
        lista (list): Lista de números enteros.

    Returns:
        list: Devuelve una lista con la suma de los dígitos
        de cada número, utilizando la función suma_digitos().
    """
    resultado = []

    for numero in lista:
        resultado.append(suma_digitos(numero))

    return resultado

#ejercicio 1514

def dos_sumandos(lista, resultado):
    """
    Busca dos elementos de una lista cuya suma sea igual
    al resultado indicado.

    Args:
        lista (list): Lista de números donde se buscan
        los dos elementos.
        resultado (int): Valor que se quiere obtener
        mediante la suma de dos elementos.

    Returns:
        list: Devuelve los índices de los dos elementos
        que cumplen con la suma solicitada.
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
            

#ejercicio 1518

def titulo(s):
    """
    Transforma una cadena de texto al formato de título.

    Args:
        s (str): Cadena de texto que se quiere formatear.

    Returns:
        str: Devuelve una cadena con la primera letra
        de cada palabra en mayúscula y las demás en minúscula.
    """
    digitos = str(n)
    repetidos = []

    for digito in digitos:
        if digitos.count(digito) > 1 and digito not in repetidos:
            repetidos.append(digito)

    return repetidos


#ejercicio 1520

def analizar_texto(texto):
    """
    Analiza un texto y cuenta las palabras que contiene.
    También identifica las letras repetidas en cada palabra,
    sin distinguir entre mayúsculas y minúsculas.

    Args:
        texto (str): Cadena de texto ingresada por el usuario
        que se quiere analizar.

    Returns:
        tuple: Devuelve la cantidad total de palabras
        y un diccionario con las letras repetidas
        de cada palabra.
    """
    texto = input("Ingrese un texto: ")

    palabras = texto.split()

    print("Cantidad de palabras:", len(palabras))

    for palabra in palabras:
        palabra = palabra.lower()
        repetidas = ""

        for letra in palabra:
            if letra.isalpha() and palabra.count(letra) > 1:
                if letra not in repetidas:
                    repetidas = repetidas + letra

        if repetidas != "":
            print(palabra, ":", repetidas)
            

#ejercicio 1530

def comprimir_rle(texto):
    """
    Comprime un texto agrupando los caracteres iguales
    que aparecen consecutivamente.

    Args:
        texto (str): Cadena de texto original que se quiere
        comprimir.

    Returns:
        list: Devuelve una lista de tuplas. Cada tupla contiene
        un carácter y la cantidad de veces que aparece
        consecutivamente.
    """

    lista = []

    if texto == "":
        return lista

    contador = 1

    for i in range(len(texto)):
        if i + 1 < len(texto) and texto[i] == texto[i + 1]:
            contador += 1
        else:
            lista.append((texto[i], contador))
            contador = 1

    return lista

def descomprimir_rle(lista_comprimida):
    """
    Reconstruye el texto original a partir de una lista
    comprimida utilizando el algoritmo RLE.

    Args:
        lista_comprimida (list): Lista de tuplas que contiene
        cada carácter y su cantidad de repeticiones.

    Returns:
        str: Devuelve la cadena de texto original reconstruida.
    """

    texto = ""

    for caracter, cantidad in lista_comprimida:
        texto += caracter * cantidad

    return texto

def tasa_compresion(texto_original, lista_comprimida):
    """
    Calcula el porcentaje de reducción del tamaño del texto
    y determina si la compresión fue efectiva.

    Args:
        texto_original (str): Cadena de texto original
        sin comprimir.
        lista_comprimida (list): Lista de tuplas obtenida
        mediante la función comprimir_rle.

    Returns:
        tuple: Devuelve el porcentaje de reducción
        y un valor booleano que indica si la compresión
        fue efectiva (True) o no (False).
    """

    if len(texto_original) == 0:
        return 0, False

    tasa = (1 - len(lista_comprimida) / len(texto_original)) * 100

    efectiva = len(lista_comprimida) < len(texto_original)

    return tasa, efectiva
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
