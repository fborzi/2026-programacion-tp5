def comparar_elementos_en_lista(b: list, elementos: list) -> bool:
    """
    Verifica si todos los elementos de una lista pertenecen a otra.

    Args:
        b (list): lista donde se busca.
        elementos (list): elementos a buscar en b.

    Returns:
        bool: True si todos los elementos están en b, False si falta alguno.
    """
    return (all(e in b for e in elementos))


def dos_minimos(lista: list) -> int:
    """
    pide ingresar una lista con elementos enteros, los compara
    y devuelve los dos valores menores de la lista ingresada.
    si falta un valor minimo guarda none.

    args:
        lista (list): lista que se ingresa y compara

    return:
        int: guarda los valores minimos o none
    """
    menor = None
    segundo = None
    for x in lista:
        if menor is None or x < menor:
            segundo = menor
            menor = x
        elif segundo is None or x < segundo:
            segundo = x
    return (menor, segundo)


def digitos(numero: int) -> list:
    """
    pide ingresar digitos, y se retorna como lista
    los numeros que se ingresen

    args:
        numero(int): el numero que se ingresa para convertir en lista

    return: 
        guarda la lista que se creo con el ingreso de digitos
    """
    lista = []
    for d in str(numero):
        lista.append(int(d))
    return lista


def ocurrencias(lista: list) -> list:
    """
    recorre una lista y cuenta cuantas veces aparece cada elemento
    de forma contigua (seguido), respetando el orden en que aparecen

    args:
        lista(list): la lista de elementos a analizar

    return:
        una lista de listas, donde cada una tiene el elemento
        y la cantidad de veces que aparece seguido.
    """
    resultado = []
    for i in range(len(lista)):
        if i > 0 and lista[i] == lista[i - 1]:
            resultado[-1][1] += 1
        else:
            resultado.append([lista[i], 1])
    return resultado


def indice_mayor(lista: list) -> int:
    """
    busca el mayor numero de la lista y devuelve
    la posicion (indice) en la que se encuentra

    args:
        lista(list): la lista de numeros a analizar

    return:
        el indice (int) donde esta el numero mas grande.
    """
    pos_mayor = 0
    for i in range(len(lista)):
        if lista[i] > lista[pos_mayor]:
            pos_mayor = i
    return pos_mayor


def obtenerCiudad(personas: list, DNI: int) -> str or None:
    """
    busca a una persona por su DNI y devuelve la ciudad donde vive

    args:
        personas(list): lista de personas, cada una [nombre, dni, ciudad]
        DNI(int): el DNI de la persona a buscar

    return:
        la ciudad (str) donde vive la persona,
        o None si no se encuentra el DNI
    """
    for persona in personas:
        if persona[1] == DNI:
            return persona[2]
    return None


def obtenerProvincia(personas: list, ciudades: list, DNI: int) -> str or None:
    """
    busca la provincia donde vive una persona a partir de su DNI,
    usando obtenerCiudad para saber primero su ciudad

    args:
        personas(list): lista de personas, cada una [nombre, dni, ciudad]
        ciudades(list): lista de ciudades, cada una [ciudad, provincia]
        DNI(int): el DNI de la persona a buscar

    return:
        la provincia (str) donde vive la persona,
        o None si no se encuentra
    """
    ciudad_persona = obtenerCiudad(personas, DNI)
    for ciudad in ciudades:
        if ciudad[0] == ciudad_persona:
            return ciudad[1]
    return None


def contarPoblacion(personas: list, ciudades: list, provincia: str) -> int:
    """
    cuenta cuantas personas viven en una provincia,
    usando obtenerProvincia para cada persona

    args:
        personas(list): lista de personas, cada una [nombre, dni, ciudad]
        ciudades(list): lista de ciudades, cada una [ciudad, provincia]
        provincia(str): la provincia a contar

    return:
        la cantidad (int) de personas que viven en esa provincia
    """
    contador = 0
    for persona in personas:
        dni = persona[1]
        if obtenerProvincia(personas, ciudades, dni) == provincia:
            contador += 1
    return contador


def digitos_repetidos(numero: int) -> list:
    """
    busca los digitos que aparecen mas de una vez en un numero

    args:
        numero(int): el numero a analizar

    return:
        una lista (list) con los digitos repetidos, sin repetirlos.
        ej: 11223 -> [1, 2]
    """
    texto = str(abs(numero))
    repetidos = []
    for d in texto:
        if texto.count(d) > 1 and int(d) not in repetidos:
            repetidos.append(int(d))
    return repetidos


def procesar_numeros() -> None:
    """
    pide numeros enteros hasta que se ingrese uno sin digitos repetidos.
    para cada numero informa la suma y la cantidad de digitos repetidos,
    y al finalizar informa el porcentaje de mayores a 478 y el promedio

    args:
        no recibe argumentos

    return:
        no retorna nada (None), solo muestra los resultados por pantalla
    """
    cantidad_numeros = 0
    suma_numeros = 0
    mayores_478 = 0

    numero = int(input("Ingresá un número entero: "))
    repetidos = digitos_repetidos(numero)

    while len(repetidos) > 0:
        print("Suma de dígitos repetidos:", sum(repetidos))
        print("Cantidad de dígitos repetidos:", len(repetidos))

        cantidad_numeros += 1
        suma_numeros += numero
        if numero > 478:
            mayores_478 += 1

        numero = int(input("Ingresá un número entero: "))
        repetidos = digitos_repetidos(numero)

    if cantidad_numeros > 0:
        porcentaje = mayores_478 / cantidad_numeros * 100
        promedio = suma_numeros / cantidad_numeros
        print("Porcentaje de números mayores a 478:", porcentaje, "%")
        print("Promedio de los números procesados:", promedio)
    else:
        print("No se procesó ningún número.")


def leer_texto() -> str:
    """
    pide lineas de texto hasta que se ingrese una que termine con '*'
    y las junta todas en un solo texto

    args:
        no recibe argumentos

    return:
        el texto completo (str), sin el '*' final
    """
    texto = ""
    linea = input("Ingresá una línea (terminá con *): ")
    while not linea.endswith("*"):
        texto += linea + " "
        linea = input("Ingresá una línea (terminá con *): ")
    texto += linea[:-1]
    return texto


def normalizar(palabra: str) -> str:
    """
    pasa una palabra a minusculas y le saca los acentos

    args:
        palabra(str): la palabra a normalizar

    return:
        la palabra (str) en minusculas y sin acentos.
    """
    palabra = palabra.lower()
    acentos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}
    resultado = ""
    for letra in palabra:
        if letra in acentos:
            resultado += acentos[letra]
        else:
            resultado += letra
    return resultado


def limpiar_palabra(palabra: str) -> str:
    """
    le saca los signos de puntuacion del principio y del final a una palabra

    args:
        palabra(str): la palabra a limpiar

    return:
        la palabra (str) sin signos de puntuacion.
    """
    return palabra.strip(".,;:!?¡¿\"'()*")


def vocales_diferentes(palabra: str) -> int:
    """
    cuenta cuantas vocales distintas tiene una palabra,
    ignorando acentos y mayusculas

    args:
        palabra(str): la palabra a analizar

    return:
        la cantidad (int) de vocales diferentes.
    """
    encontradas = set()
    for letra in normalizar(palabra):
        if letra in "aeiou":
            encontradas.add(letra)
    return len(encontradas)


def palabras_con_3_vocales(texto: str) -> list:
    """
    busca las palabras del texto que tienen al menos 3 vocales diferentes

    args:
        texto(str): el texto a analizar

    return:
        una lista (list) con esas palabras, sin repetirlas
    """
    resultado = []
    for palabra in texto.split():
        palabra = limpiar_palabra(palabra)
        if vocales_diferentes(palabra) >= 3 and palabra not in resultado:
            resultado.append(palabra)
    return resultado


def separar_oraciones(texto: str) -> list:
    """
    separa el texto en oraciones. una oracion termina siempre con '.'

    args:
        texto(str): el texto a analizar

    return:
        una lista (list) con las oraciones encontradas
    """
    partes = texto.split(".")
    oraciones = []
    for parte in partes[:-1]:
        if parte.strip() != "":
            oraciones.append(parte.strip())
    return oraciones


def porcentaje_oraciones_largas(oraciones: list) -> float:
    """
    calcula el porcentaje de oraciones que tienen mas de cinco palabras

    args:
        oraciones(list): la lista de oraciones

    return:
        el porcentaje (float). si no hay oraciones, devuelve 0
    """
    if len(oraciones) == 0:
        return 0
    largas = 0
    for oracion in oraciones:
        if len(oracion.split()) > 5:
            largas += 1
    return largas / len(oraciones) * 100


def procesar_texto() -> None:
    """
    pide un texto, y informa las palabras con al menos 3 vocales
    diferentes, la cantidad de oraciones y el porcentaje de
    oraciones con mas de cinco palabras

    args:
        no recibe argumentos

    return:
        no retorna nada (None), solo muestra los resultados por pantalla
    """
    texto = leer_texto()
    oraciones = separar_oraciones(texto)

    print("a. Palabras con al menos 3 vocales diferentes:",
          palabras_con_3_vocales(texto))
    print("b. Cantidad de oraciones:", len(oraciones))
    print("c. Porcentaje de oraciones con más de 5 palabras:",
          porcentaje_oraciones_largas(oraciones), "%")
