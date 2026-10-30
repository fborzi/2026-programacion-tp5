def minimo_elemento(lista):
  
    if (not lista):
        return None
    else :
        minimo=lista[0]
        for e in lista:
           if e < minimo :
               minimo=e
        return minimo
      

def pertenece(lista: list, elemento):
    """
    Comprueba si un elemento se encuentra en una lista.
    Args:
        lista: lista que queremos consultar.
        elemento: elemento que queremos buscar.
    Returns: 
        True si pertenece a la lista y False si no pertenece.
    """
    
    return elemento in lista

def buscar_indice(lista: list, elemento):
    """
    Devuelve la posicion de un elemento dentro de una lista.
    Args: 
        lista: lista donde buscamos.
        elemento: elemento que queremos encontrar.
    Returns:
        el indice de la primera aparicion del elemento.
    """
    if elemento in lista:
        return lista.index(elemento)
    return -1

def cargar_nombres(nombres: list = None) -> list:
    """
    Solicita nombres y los guarda hasta recibir una entrada en blanco.
    Args:
        nombres: lista donde se guardan los nombres.
    Returns:
        La lista completa de nombres ingresados.
    """
    if nombres is None:
        nombres = []

    nombre = input("Ingrese un nombre (Enter para terminar): ")
    if nombre == "":
        return nombres
    nombres.append(nombre)
    return cargar_nombres(nombres)

def convertir_mayusculas(nombres: list) -> list:
    """
    Crea una nueva lista con los nombres en mayúsculas.
    Args:
        nombres: lista de nombres recibida.
    Returns:
        Una nueva lista con los nombres en mayúsculas.
    """
    nombres_mayusculas = []
    
    for nombre in nombres:
        nombre_mayuscula = nombre.upper()
        nombres_mayusculas.append(nombre_mayuscula)
    return nombres_mayusculas

def dos_minimos(lista):
    """Busca los dos valores menores de una lista.
    Args:
        lista (list): Elementos comparables entre sí.
    Returns:
        Los dos menores valores; usa None si faltan elementos.
    """
    ordenados = sorted(lista)
    primero = ordenados[0] if len(ordenados) >= 1 else None
    segundo = ordenados[1] if len(ordenados) >= 2 else None
    return primero, segundo

def digitos(numero):
    """Separa un número entero en sus dígitos.
    Args:
        numero (int): Número que se desea separar.
    Returns:
        list[int]: Dígitos en el orden en que aparecen.
    """
    return [int(c) for c in str(abs(numero))]

def ocurrencias(lista):
    """Cuenta grupos consecutivos de elementos iguales.
    Args:
        lista (list): Elementos que se desean agrupar.
    Returns:
        list[list]: Pares [elemento, cantidad] en orden de aparición.
    """
    resultado = []
    for elemento in lista:
        if resultado and resultado[-1][0] == elemento:
            resultado[-1][1] += 1
        else:
            resultado.append([elemento, 1])
    return resultado

def indice_mayor(lista):
    """Devuelve el índice de la primera aparición del mayor elemento.
    Args:
        lista (list): Lista de números comparables.
    Returns:
        int | None: Índice del máximo, o None si la lista está vacía.
    """
    if not lista:
        return None
    mayor = max(lista)
    return lista.index(mayor)
import unicodedata


def normalizar(texto):
    """Normaliza texto para comparar sin distinguir mayúsculas ni tildes."""
    texto = str(texto).strip().casefold()
    return "".join(
        caracter for caracter in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caracter) != "Mn"
    )


def obtenerCiudad(personas, DNI):
    """Busca y devuelve la ciudad de una persona por su DNI."""
    for persona in personas:
        if str(persona[1]).strip() == str(DNI).strip():
            return persona[2]
    return None


def obtenerProvincia(personas, ciudades, DNI):
    """Busca y devuelve la provincia donde vive una persona."""
    ciudad_persona = obtenerCiudad(personas, DNI)

    if ciudad_persona is None:
        return None

    for ciudad, provincia in ciudades:
        if normalizar(ciudad) == normalizar(ciudad_persona):
            return provincia
    return None


def contarPoblacion(personas, ciudades, provincia):
    """Cuenta cuántas personas viven en una provincia."""
    cantidad = 0

    for persona in personas:
        provincia_persona = obtenerProvincia(personas, ciudades, persona[1])
        if provincia_persona is not None and normalizar(provincia_persona) == normalizar(provincia):
            cantidad += 1

    return cantidad

def digitos_repetidos(numero):
    """Devuelve una lista de dígitos distintos que aparecen más de una vez.
    Args:
        numero (int): Número entero que se analiza.
    Returns:
        list[int]: Dígitos repetidos, sin duplicarlos en la lista resultado.
    """
    digitos_numero = digitos(numero)
    return list(dict.fromkeys(
        digito for digito in digitos_numero
        if digitos_numero.count(digito) > 1
    ))

def cargar_lineas_hasta_asterisco():
    """Lee líneas de texto hasta que una termine con *.
    Returns:
        str: Texto completo ingresado, sin el asterisco final.
    """
    lineas = []

    def leer_otra_linea():
        linea = input("Ingrese una línea (termine la última con *): ")
        if linea.rstrip().endswith("*"):
            lineas.append(linea.rstrip()[:-1])
            return
        lineas.append(linea)
        leer_otra_linea()

    leer_otra_linea()
    return "\\n".join(lineas)

def contar_vocales_distintas(palabra):
    """Cuenta las vocales diferentes de una palabra, ignorando mayúsculas y acentos.
    Args:
        palabra (str): Palabra que se desea analizar.
    Returns:
        int: Cantidad de vocales distintas encontradas.
    """
    traduccion = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    texto = palabra.translate(traduccion).lower()
    return len({caracter for caracter in texto if caracter in "aeiou"})

