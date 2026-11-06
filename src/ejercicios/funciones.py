def dos_minimos(lista):
    """Determina los dos valores mínimos de una lista.
    Args:
      lista: list - lista de números.
    Returns:
        tuple - los dos valores mínimos de la lista."""

    if len(lista) == 0:
        return (None, None)

    if len(lista) == 1:
        return (lista[0], None)

    menor = lista[0]
    segundo_menor = lista[1]

    if segundo_menor < menor:
        menor, segundo_menor = segundo_menor, menor

    for elemento in lista[2:]:

        if elemento < menor:
            segundo_menor = menor
            menor = elemento

        elif elemento < segundo_menor:
            segundo_menor = elemento

    return (menor, segundo_menor)


def digitos(numero):
    """Separa los dígitos de un número y los guarda en una lista.
    Args:
       numero: int - número entero recibido por parámetro.
    Returns:
        list - lista con los dígitos del número."""
    lista = []
    numero = str(numero)

    for digito in numero:
        lista.append(int(digito))
    return lista



def ocurrencias(lista):
    """Cuenta las apariciones consecutivas de cada elemento de una lista.
    Args:
        lista: list - lista de elementos.
    Returns:
        list - lista con cada elemento y su cantidad de apariciones consecutivas."""
    
    resultado = []
    contador = 1

    for i in range(len(lista)):
        if i < len(lista) - 1 and lista[i] == lista[i + 1]:
            contador += 1
        else:
            resultado.append([lista[i], contador])
            contador = 1
    return resultado



def indice_mayor(lista):
    """Busca la posición del mayor elemento de una lista.
    Args:
        lista: list - lista de números.
    Returns:
        int - índice donde se encuentra el mayor elemento."""

    mayor = lista[0]
    indice = 0

    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i
    return indice





def obtenerCiudad(personas, DNI):
    """Obtiene la ciudad de una persona.
    Args:
        lista: list - lista con los datos de una persona.
    Returns:
        str - ciudad de la persona. """
    
    for persona in personas:

        if persona[1] == DNI:
            return persona[2]
        
    return None

def obtenerProvincia(personas, ciudades, DNI):
    """Obtiene la provincia de una persona.
    Args:
        lista: list - lista con los datos de una persona.
    Returns:
        str - provincia de la persona."""
    
    ciudad = obtenerCiudad(personas, DNI)
    for dato in ciudades:

        if dato[0] == ciudad:
            return dato[1]
        
    return None

def contarPoblacion(personas, ciudades, provincia):
    """Cuenta la población de una lista de personas.
    Args:
        lista: list - lista de personas.
    Returns:
        int - cantidad de personas."""

    contador = 0

    for persona in personas:
        dni = persona[1]
        provincia_persona = obtenerProvincia(personas, ciudades, dni)

        if provincia_persona == provincia:
            contador += 1
    return contador


def frecuencia_caracteres(cadena):
    """Cuenta cuántas veces aparece cada carácter de una cadena.
    Args:
        cadena: str - cadena de texto recibida por parámetro.
    Returns:
        dict - diccionario con cada carácter y su frecuencia. """
    
    frecuencias = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

def sucesion_mira_y_deci(n):
    """Calcula los primeros n números de la sucesión Mira y Decí.
    Args:
        n: int - cantidad de números que se desea obtener.
    Returns:
        list - lista con los primeros n números de la sucesión."""
    
    sucesion = [1]
    while len(sucesion) < n:
        numero = str(sucesion[-1])
        siguiente = ""
        contador = 1

        for i in range(len(numero)):
            if i < len(numero) - 1 and numero[i] == numero[i + 1]:
                contador += 1
            else:
                siguiente = siguiente + str(contador) + numero[i]
                contador = 1
        sucesion.append(int(siguiente))
    return sucesion
def minimo_elemento(lista):
    """busca y devuelve el minimo elemento mas pequeño de la lista, 
    recibe una lista, si la lista esta vacia devuelve none"""
    if not lista:
       return None
    minimo = lista[0]
    for elem in lista[1:]:
        if elem < minimo:
            minimo = elem
    return minimo

def piedra_papel_tijera(uno, dos):
    """ determina quien gana un piedra, papel o tijera"""
    uno = uno.lower()
    dos = dos.lower()
    
    if uno == dos:
        return 0
    
    if (uno == "piedra" and dos == "tijera") or \
       (uno == "papel" and dos == "piedra") or \
       (uno == "tijera" and dos == "papel"):
        return 1
    else:
        return 2

def borrar_adyacentes(lista):
    """borran elementos repetidos que estan uno al lado de otro"""
    if not lista:
        return []
    resultado = [lista[0]]
    for elem in lista[1:]:
        if elem != resultado[-1]:
            resultado.append(elem)
    return resultado

def suma_digitos(n):
    """ suma todos los digitos de una unidad"""

    return sum(int(d) for d in str(n))

def sumatoria_digitos(lista):
    """suma como la funcion de suma pero a todos los elementos de la lista"""
    return [suma_digitos(num) for num in lista]

def dos_sumandos(lista, resultado):
    """ busca dos numeros de la lista ingresada y que den el mismo resultado
    que ya ingresamos """
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == resultado:
                return [i, j]
    return None

def digitos_repetidos(n):
    """ que digitos se repiten dentro de un numero """
    texto = str(n)          # convertimos el número a cadena
    vistos = set()          # dígitos ya vistos
    repetidos = set()       # dígitos que se repiten
    
    for d in texto:
        if d in vistos:
            repetidos.add(d)
        else:
            vistos.add(d)
    
    return [int(d) for d in repetidos]

def analizar_texto(texto):
   """analiza el texto y ve si hay letras repetidas"""
   palabras = texto.split()
   print(f"Cantidad de palabras: {len(palabras)}")

   for palabra in palabras:
        palabra_limpia = "".join([c.lower() for c in palabra if c.isalpha()])
        repeticiones = set([c for c in palabra_limpia if palabra_limpia.count(c) > 1])
        
        if repeticiones:
            print(f"En '{palabra}' se repiten: {', '.join(sorted(repeticiones))}")
        else:
            print(f"En '{palabra}' no hay letras repetidas.")

def comprimir_rle(texto):
    """ recorremos el texto y vemos cuantas veces aparece, los guarda como duplas"""
    if not texto:
        return []

    resultado = []
    actual = texto[0]
    cantidad = 1

    for caracter in texto[1:]:
        if caracter == actual:
            cantidad += 1
        else:
            resultado.append((actual, cantidad))
            actual = caracter
            cantidad = 1

    resultado.append((actual, cantidad))
    return resultado


def descomprimir_rle(lista_comprimida):
    texto = ""

    for caracter, cantidad in lista_comprimida:
        texto += caracter * cantidad

    return texto


def tasa_compresion(texto_original, lista_comprimida):
    tasa = (1 - len(lista_comprimida) / len(texto_original)) * 100

    efectiva = len(lista_comprimida) < len(texto_original)

    return tasa, efectiva

