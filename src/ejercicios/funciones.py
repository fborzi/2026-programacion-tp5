def minimo_elemento(lista):

    """Busca el elemento mínimo de una lista.
Args:
    lista: list - lista de elementos que se quieren comparar.
Returns:
    int - elemento mínimo de la lista, o None si está vacía."""
    
    if len(lista) == 0:
        return None

    minimo = lista[0]

    for elemento in lista:
        if elemento < minimo:
            minimo = elemento

    return minimo


def piedra_papel_tijera(uno, dos):

    """Determina el ganador de una partida de piedra, papel o tijera.
Args:
    jugador1: str - jugada del primer jugador.
    jugador2: str - jugada del segundo jugador.
Returns:
    int - 1 si gana el primero, 2 si gana el segundo o 0 si empatan."""

    uno = uno.lower()
    dos = dos.lower()

    if uno == dos:
        return 0
    elif uno == "piedra" and dos == "tijera":
        return 1
    elif uno == "tijera" and dos == "papel":
        return 1
    elif uno == "papel" and dos == "piedra":
        return 1
    else:
        return 2


def borrar_adyacentes(lista):

    """Elimina los elementos repetidos consecutivos de una lista.
Args:
    lista: list - lista de elementos que se quieren procesar.
Returns:
    list - lista sin repeticiones consecutivas."""

    resultado = []

    for caracter in lista:
        if len(resultado) == 0 or caracter != resultado[-1]:
            resultado.append(caracter)

    return resultado


def suma_digitos(n):

    """Calcula la suma de los dígitos de un número entero.
Args:
    n: int - número entero cuyos dígitos se van a sumar.
Returns:
    int - suma de los dígitos del número."""

    suma = 0

    while n > 0:
        digito = n % 10
        suma = suma + digito
        n = n // 10

    return suma


def sumatoria_digitos(lista):

    """Calcula la suma de los dígitos de cada número de una lista.
Args:
    lista: list - lista de números enteros positivos.
Returns:
    list - lista con la suma de los dígitos de cada número."""

    resultado = []

    for numero in lista:
        resultado.append(suma_digitos(numero))

    return resultado


def dos_sumandos(lista, resultado):

    """Busca dos elementos de una lista cuya suma sea igual a un objetivo.
Args:
    lista: list - lista de números que se van a evaluar.
    objetivo: int - valor que debe sumar la pareja de elementos.
Returns:
    list - índices de los dos elementos encontrados o una lista vacía."""

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]

    return []


def digitos_repetidos(n):

    """Busca los dígitos que se repiten en un número entero.
Args:
    numero: int - número que se quiere analizar.
Returns:
    list - lista de dígitos repetidos sin duplicarlos en el resultado."""

    repetidos = []
    vistos = []

    while n > 0:
        digito = n % 10

        if digito in vistos and digito not in repetidos:
            repetidos.append(digito)

        vistos.append(digito)
        n = n // 10

    return repetidos


def version_a():

    """Cuenta cuántas ciudades pertenecen a cada país durante la carga.
Args:
    - datos necesarios para ingresar ciudades y países.
Returns:
    None - muestra los resultados en pantalla."""

    print("VERSION A: SIN ALMACENAR CIUDADES")

    cantidad_ciudades = 0
    ciudades_por_pais = {}

    ciudad = input("Ingrese una ciudad (zz para terminar): ")

    while ciudad.lower() != "zz":
        pais = input("Ingrese el país: ")

        cantidad_ciudades = cantidad_ciudades + 1

        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] = ciudades_por_pais[pais] + 1
        else:
            ciudades_por_pais[pais] = 1

        ciudad = input("Ingrese una ciudad (zz para terminar): ")

    print("Cantidad total de ciudades:", cantidad_ciudades)

    for pais, cantidad in ciudades_por_pais.items():
        print(pais, ":", cantidad)


def version_b():

    """Registra ciudades y países en una lista y cuenta las ciudades
que pertenecen a cada país.
Args:
    - datos necesarios para ingresar ciudades y países.
Returns:
    None - muestra los resultados en pantalla."""

    print("VERSION B: ALMACENANDO CIUDADES EN UNA LISTA")

    ciudades = []

    ciudad = input("Ingrese una ciudad (zz para terminar): ")

    while ciudad.lower() != "zz":
        pais = input("Ingrese el país: ")
        ciudades.append([ciudad, pais])

        ciudad = input("Ingrese una ciudad (zz para terminar): ")

    cantidad_ciudades = len(ciudades)
    ciudades_por_pais = {}

    for ciudad in ciudades:
        pais = ciudad[1]

        if pais in ciudades_por_pais:
            ciudades_por_pais[pais] = ciudades_por_pais[pais] + 1
        else:
            ciudades_por_pais[pais] = 1

    print("Cantidad total de ciudades:", cantidad_ciudades)

    for pais, cantidad in ciudades_por_pais.items():
        print(pais, ":", cantidad)


def comprimir_rle(texto):

    """Comprime un texto mediante el método RLE.
Args:
    texto: str - texto que se quiere comprimir.
Returns:
    list - lista de tuplas con cada carácter y su cantidad consecutiva."""

    comprimido = []

    if len(texto) == 0:
        return comprimido

    caracter_actual = texto[0]
    cantidad = 1

    for i in range(1, len(texto)):
        if texto[i] == caracter_actual:
            cantidad = cantidad + 1
        else:
            comprimido.append((caracter_actual, cantidad))
            caracter_actual = texto[i]
            cantidad = 1

    comprimido.append((caracter_actual, cantidad))

    return comprimido


def descomprimir_rle(lista_comprimida):

    """Descomprime un texto codificado mediante RLE.
Args:
    lista_comprimida: list - lista de tuplas con caracteres y cantidades.
Returns:
    str - texto original reconstruido."""

    texto = ""

    for caracter, cantidad in lista_comprimida:
        texto = texto + caracter * cantidad

    return texto


def tasa_compresion(texto_original, lista_comprimida):

    """Calcula la tasa de compresión y determina si fue efectiva.
Args:
    texto_original: str - texto antes de comprimir.
    lista_comprimida: list - representación comprimida del texto.
Returns:
    tuple - porcentaje de compresión y un booleano que indica
    si la compresión fue efectiva."""
    
    if len(texto_original) == 0:
        return 0, False

    tasa = (1 - len(lista_comprimida) / len(texto_original)) * 100
    efectiva = len(lista_comprimida) < len(texto_original)

    return tasa, efectiva
