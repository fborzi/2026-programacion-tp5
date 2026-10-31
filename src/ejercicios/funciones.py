#1502 ejercicio: conteo de elementos de una lista

def contar_elementos(lista: list, elemento: int) -> int:
    """cuenta cuantas veces aparece un elemento en una lista.
    args:
        lista: lista de elementos
        elemento: elemento a contar
    returns:
        int: cantidad de veces que aparece el elemento en la lista"""
    return lista.count(elemento)

#1504 carga interactiva de nombres en una lista carga 
"""este codigo de funciones sino recibimos una lista,
 creamos una vacia depues solcticamos un nombre por teclado , 
 si el nombre esta vacio devolvemos la lista."""


def cargar_nombres(nombres: list = None) -> list:


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
        la lista completa de nombres ingresados.
        La lista completa de nombres ingresados.
    """
    if nombres is None:
        nombres = []

    nombre = input("Ingrese un nombre (Enter para terminar): ")
    if nombre == "":
        return nombres
    nombres.append(nombre)
    return cargar_nombres(nombres)

#ejercicio 1506: busqueda de un elemento minimo  en una lista
"""en funciones py devuelve el menor elementos de la lista  comprueba si la
la lista tiene elementos,  cuando la lista esta vacia devuelve un none"""

def minimo_elemento(lista):
    """Busca el menor elemento de una lista.
    Args:
        lista (list): Elementos comparables entre sí.

    Returns:
        object | None: El menor elemento o None si la lista está vacia.
    """
    return min(lista) if lista else None

# Ejercicio 1508: juego de piedra, papel o tijera
"""
Este código determina el ganador de un juego de piedra, papel o tijera entre dos jugadores."""
def piedra_papel_tijera(uno, dos):
    """
    Determina el ganador de piedra, papel o tijera.

    Args:
        uno (str): Eleccion del primer jugador.
        dos (str): Eleccion del segundo jugador.

    Returns:
        int: 1 si gana el primero, 2 si gana el segundo
        o 0 si empatan.

    Raises:
        ValueError: Si alguna elección no es valida.
    """

    uno, dos = uno.lower().strip(), dos.lower().strip()

    opciones = {"piedra", "papel", "tijera"}

    if uno not in opciones or dos not in opciones:
        raise ValueError("las opciones deben ser piedra, papel o tijera.")

    
    if uno == dos:
        return 0

    if (uno, dos) in {
        ("piedra", "tijera"),
        ("tijera", "papel"),
        ("papel", "piedra")
    }:
        return 1

    return 2


# Ejercicio 1510: eliminacion de caracteres adyacentes repetidos.
"""Este codigo elimina caracteres repetidos consecutivamente de una lista."""

def borrar_adyacentes(lista):
    """
    Elimina caracteres repetidos consecutivamente.

    Args:
        lista (list): Lista de caracteres.

    Returns:
        list: Lista con una sola ocurrencia por grupo consecutivo.
    """
  
    return [
        elemento
        for i, elemento in enumerate(lista)
        if i == 0 or elemento != lista[i - 1]
    ]

# Ejercicio 1512: sumatoria de dígitos de elementos de una lista.
"""Este codigo calcula la suma de los digitos de cada numero en una lista."""

def digitos(numero):
    """
    Separa los dígitos de un número.

    Args:
        numero (int): Número que queremos separar.

    Returns:
        list: Lista de dígitos.
    """

    return [int(digito) for digito in str(abs(numero))]


def suma_digitos(numero):
    """
    Suma los digitos de un numero entero.

    Args:
        numero (int): Numero cuyos dígitos se suman.

    Returns:
        int: Suma de los digitos.
    """
    
    return sum(digitos(numero))


def sumatoria_digitos(lista):
    """
    Calcula la suma de digitos de cada numero.

    Args:
        lista (list[int]): Lista de numeros enteros.

    Returns:
        list[int]: Lista con la suma de los digitos.
    """

    return [suma_digitos(numero) for numero in lista]


# Ejercicio 1514: busqueda de dos sumandos en una lista.
"""Este codigo busca dos posiciones distintas cuya suma sea un resultado dado."""
def dos_sumandos(lista, resultado):
    """
    Busca dos posiciones distintas cuya suma sea un resultado dado.

    Args:
        lista (list[int | float]): Lista de numeros.
        resultado (int | float): Suma que se desea encontrar.

    Returns:
        list[int] | None: Dos indices o None si no existe una pareja.
    """
    
    for i, primero in enumerate(lista):

        
        for j in range(i + 1, len(lista)):

          
            if primero + lista[j] == resultado:
                
                return [i, j]

    
    return None


# Ejercicios 1518 identificacion de digitos repetidos en un numero
"""Este codigo identifica los digitos que se repiten en un numero entero ingresado por el usuario."""
def digitos_repetidos(numero):
    """
    Identifica los digitos que aparecen mas de una vez.

    Args:
        numero (int): Numero que se analiza.

    Returns:
        list[int]: Dígitos repetidos, sin duplicarlos en el resultado.
    """
   
    lista = digitos(numero)

    
    return list(dict.fromkeys(d for d in lista if lista.count(d) > 1))


# Ejercicio 1520: analisis de palabras y letras repetidas en un texto
"""Este codigo analiza un texto ingresado por el usuario, cuenta la cantidad de palabras y
muestra las letras que se repiten en cada palabra."""
def letras_repetidas(palabra):
    """
    Busca letras repetidas en una palabra.

    Args:
        palabra (str): Palabra que se analiza.

    Returns:
        list[str]: Letras repetidas en minúscula y sin repetirlas en la lista.
    """
   
    letras = [c.lower() for c in palabra if c.isalpha()]

  
    return list(dict.fromkeys(c for c in letras if letras.count(c) > 1))

# Ejercicio 1522 gestion de poblacion de ciudades con diccionarios
"""Este código carga socios de un club y permite realizar operaciones sobre ellos."""
def cargar_socios() -> dict:
    """
    Carga los socios de un club y los guarda en un diccionario.

    Returns:
        dict: Socios identificados por su DNI.
    """
    socios = {}

    cantidad = int(input("Ingrese la cantidad de socios: "))

    for i in range(cantidad):
     
        dni = input("Ingrese el DNI: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = int(input("Ingrese la edad: "))
        cuota = input("¿Tiene la cuota al dia? (s/n): ").lower()

        socios[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "cuota_al_dia": cuota == "s"
        }
    return socios

#ejercicio 1524 administracion de socios del Club CAVUL
"""Este codigo permite administrar socios de un club, incluyendo carga, 
búsqueda, actualización y eliminación de socios."""

def cargar_socios():
    """Carga socios del club hasta ingresar DNI 0.

    Args:
        Ninguno.

    Returns:
        dict: Socios indexados por DNI, con sus datos personales y cuota.
    """
    socios = {}

    def cargar_otro():
        dni = input("DNI (0 para terminar): ").strip()
        if dni == "0":
            return
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        edad = int(input("Edad: "))
        cuota = input("¿Cuota al día? (s/n): ").strip().lower() == "s"
        socios[dni] = {"nombre": nombre, "apellido": apellido,
                       "edad": edad, "cuota_al_dia": cuota}
        cargar_otro()

    cargar_otro()
    return socios

#ejercicio 1526 conteo y agrupacion de ciudades por pais 
"""Este codigo permite cargar ciudades y contar cuantas pertenecen a cada pais,
ademas de conservar la lista de ciudades si se desea."""

def cargar_ciudades_por_pais(guardar_lista=False):
    """Carga ciudades y cuenta cuantas pertenecen a cada pais.

    Args:
        guardar_lista (bool): Si es True, conserva cada ciudad junto a su país.

    Returns:
        tuple: Total de ciudades, conteo por pais y lista (si se solicita).
    """
    ciudades = []
    conteo = {}

    def cargar_otra():
        ciudad = input("Ciudad (zz para terminar): ").strip()
        if ciudad.lower() == "zz":
            return
        pais = input("País: ").strip()
        conteo[pais] = conteo.get(pais, 0) + 1
        if guardar_lista:
            ciudades.append([ciudad, pais])
        cargar_otra()

    cargar_otra()
    return len(ciudades) if guardar_lista else sum(conteo.values()), conteo, ciudades

def contar_vocales_distintas(palabra):
    """Cuenta las vocales distintas de una palabra, sin distinguir acentos.

    Args:
        palabra (str): Palabra que se analiza.

    Returns:
        int: Cantidad de vocales diferentes encontradas.
    """
    traduccion = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    texto = palabra.translate(traduccion).lower()
    return len({c for c in texto if c in "aeiou"})


    def leer_otra():
        linea = input("Ingrese una línea (termine con *): ")
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
        leer_otra()

    leer_otra()
    return "\n".join(lineas)

#ejercico 1530 Compreson  y descompresion de texto con algoritmo RLE
"""Este codigo permite comprimir y descomprimir 
texto usando el metodo RLE (Run-Length Encoding)."""

def comprimir_rle(texto):
    """Comprime caracteres consecutivos con el método RLE.

    Args:
        texto (str): Cadena original.

    Returns:
        list[tuple[str, int]]: Tuplas con cada carácter y su cantidad consecutiva.
    """
    if not texto:
        return []
    resultado = []
    actual, cantidad = texto[0], 1
    for caracter in texto[1:]:
        if caracter == actual:
            cantidad += 1
        else:
            resultado.append((actual, cantidad))
            actual, cantidad = caracter, 1
    resultado.append((actual, cantidad))
    return resultado

def descomprimir_rle(lista_comprimida):
    """Reconstruye un texto desde una lista comprimida con RLE.

    Args:
        lista_comprimida (list[tuple[str, int]]): Carácter y cantidad.

    Returns:
        str: Texto original reconstruido.
    """
    return "".join(caracter * cantidad for caracter, cantidad in lista_comprimida)

def tasa_compresion(texto_original, lista_comprimida):
    """Calcula la reducción de longitud obtenida mediante RLE.

    Args:
        texto_original (str): Texto antes de comprimir.
        lista_comprimida (list[tuple[str, int]]): Resultado de la compresión.

    Returns:
        tuple[float, bool]: Porcentaje de reducción y si fue efectiva.
    """
    if not texto_original:
        return 0.0, False
    tasa = (1 - len(lista_comprimida) / len(texto_original)) * 100
    return tasa, len(lista_comprimida) < len(texto_original)













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

def frecuencia_caracteres(cadena):
    """Cuenta la frecuencia de cada carácter de una cadena.
    Args:
        cadena (str): Texto que se analiza.
    Returns:
        dict[str, int]: Diccionario de carácter y cantidad de apariciones.
    """
    frecuencia = {}
    for caracter in cadena:
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
    return frecuencia

def sucesion_mira_y_deci(n):
    """Genera los primeros términos de la sucesión Mira y Decí.
    Args:
        n (int): Cantidad de términos solicitados.
    Returns:
        list[int]: Términos generados en orden.
    """
    if n <= 0:
        return []
    terminos = ["1"]
    for _ in range(1, n):
        anterior = terminos[-1]
        grupos = ocurrencias(list(anterior))
        terminos.append("".join(str(cantidad) + caracter for caracter, cantidad in grupos))
    return [int(termino) for termino in terminos]
