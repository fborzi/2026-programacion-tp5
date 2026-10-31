import unicodedata
import re

def dos_minimos(lista):
    """Devuelve los dos valores menores de una lista.

    Args:
        lista: list - lista de elementos comparables entre sí.

    Returns:
        tuple - una tupla con los dos valores menores.
        Si faltan elementos, retorna None en su lugar.
    """
    lista_ordenada = sorted(lista)

    minimo1 = None
    minimo2 = None

    if len(lista_ordenada) >= 1:
        minimo1 = lista_ordenada[0]

    if len(lista_ordenada) >= 2:
        minimo2 = lista_ordenada[1]

    return (minimo1, minimo2)



def digitos(numero):
    
    """Retorna una lista con los dígitos de un número entero.

    Args:
        numero: int - número entero que se desea separar en dígitos.

    Returns:
        list - lista con los dígitos que componen al número.
    """
    lista = []

    for digito in str(numero):
        lista.append(int(digito))

    return lista



def ocurrencias(lista):
    """Cuenta las ocurrencias contiguas de cada elemento.

    Args:
        lista: list - lista de elementos que se quieren analizar.

    Returns:
        list - lista de listas con cada elemento y su cantidad
        de apariciones consecutivas.
    """

    resultado = []

    if len(lista) == 0:
        return resultado

    elemento_actual = lista[0]
    contador = 1

    for elemento in lista[1:]:
        if elemento == elemento_actual:
            contador += 1
        else:
            resultado.append([elemento_actual, contador])
            elemento_actual = elemento
            contador = 1

    resultado.append([elemento_actual, contador])

    return resultado




def indice_mayor(lista):
    """Retorna el índice donde se encuentra el mayor número.

    Args:
        lista: list - lista de números.

    Returns:
        int - índice del mayor número de la lista.
    """

    indice = 0

    for i in range(len(lista)):
        if lista[i] > lista[indice]:
            indice = i

    return indice





def obtenerCiudad(personas, DNI):
    """Obtiene la ciudad donde vive una persona según su DNI.

    Args:
        personas: lista con nombre, DNI y ciudad.
        DNI: documento de la persona que se busca.

    Returns:
        La ciudad donde vive la persona, o None si no existe.
    """

    for persona in personas:
        if persona[1] == DNI:
            return persona[2]

    return None


def obtenerProvincia(personas, ciudades, DNI):
    """Obtiene la provincia donde vive una persona según su DNI.

    Args:
        personas: lista con nombre, DNI y ciudad.
        ciudades: lista con ciudad y provincia.
        DNI: documento de la persona que se busca.

    Returns:
        La provincia donde vive la persona, o None si no existe.
    """

    ciudad = obtenerCiudad(personas, DNI)

    for dato in ciudades:
        if dato[0] == ciudad:
            return dato[1]

    return None


def contarPoblacion(personas, ciudades, provincia):
    """Cuenta las personas que viven en una provincia.

    Args:
        personas: lista con nombre, DNI y ciudad.
        ciudades: lista con ciudad y provincia.
        provincia: provincia que se desea contar.

    Returns:
        Cantidad de personas que viven en esa provincia.
    """

    contador = 0

    for persona in personas:
        DNI = persona[1]

        if obtenerProvincia(personas, ciudades, DNI) == provincia:
            contador += 1

    return contador




def analizar_digitos(numero):
    """Analiza los dígitos repetidos de un número.

    Args:
        numero: número entero que se desea analizar.

    Returns:
        Una tupla con la suma de los dígitos repetidos,
        la cantidad de apariciones repetidas y un booleano
        que indica si existen dígitos repetidos.
    """

    digitos = str(abs(numero))
    suma = 0
    cantidad = 0

    for digito in digitos:
        if digitos.count(digito) > 1:
            suma += int(digito)
            cantidad += 1

    tiene_repetidos = cantidad > 0

    return suma, cantidad, tiene_repetidos



def analizar_texto(texto):
    """Analiza las palabras y las oraciones de un texto.

    Args:
        texto: str - texto que se desea analizar.

    Returns:
        Una tupla con las palabras que tienen al menos
        tres vocales diferentes, la cantidad de oraciones
        y el porcentaje de oraciones con más de cinco palabras.
    """

    palabras = re.findall(r"[^\W\d_]+", texto)

    palabras_vocales = []

    for palabra in palabras:
        palabra_normalizada = unicodedata.normalize("NFD", palabra.lower())
        palabra_normalizada = "".join(
            caracter for caracter in palabra_normalizada
            if unicodedata.category(caracter) != "Mn"
        )

        vocales = set(palabra_normalizada) & set("aeiou")

        if len(vocales) >= 3:
            palabras_vocales.append(palabra)

    oraciones = texto.split(".")
    cantidad_oraciones = 0
    oraciones_largas = 0

    for oracion in oraciones:
        if oracion.strip() != "":
            cantidad_oraciones += 1

            palabras_oracion = re.findall(r"[^\W\d_]+", oracion)

            if len(palabras_oracion) > 5:
                oraciones_largas += 1

    if cantidad_oraciones > 0:
        porcentaje = oraciones_largas * 100 / cantidad_oraciones
    else:
        porcentaje = 0

    return palabras_vocales, cantidad_oraciones, porcentaje




def contar_pacientes(pacientes):
    """Cuenta la cantidad de pacientes registrados.

    Args:
        pacientes: diccionario con los datos de los pacientes.

    Returns:
        int: cantidad de pacientes registrados.
    """
    return len(pacientes)


def listar_pacientes(pacientes):
    """Muestra el DNI y los datos de cada paciente.

    Args:
        pacientes: diccionario con los datos de los pacientes.

    Returns:
        None
    """
    for dni, datos in pacientes.items():
        print("DNI:", dni)
        print("Edad:", datos["edad"])
        print("Sexo:", datos["sexo"])
        print("Diabético:", datos["diabetico"])
        print("--------------------")


def incrementar_edad(pacientes, dni):
    """Incrementa en uno la edad de un paciente.

    Args:
        pacientes: diccionario con los datos de los pacientes.
        dni: DNI del paciente que se desea modificar.

    Returns:
        bool: True si se encontró al paciente, False si no.
    """
    if dni in pacientes:
        pacientes[dni]["edad"] += 1
        return True

    return False


def tiene_diabetes(pacientes, dni):
    """Indica si un paciente tiene diabetes.

    Args:
        pacientes: diccionario con los datos de los pacientes.
        dni: DNI del paciente que se desea consultar.

    Returns:
        bool o None: True si tiene diabetes, False si no,
        None si el DNI no está registrado.
    """
    if dni in pacientes:
        return pacientes[dni]["diabetico"]

    return None


def promedio_edad_diabeticos(pacientes):
    """Calcula la edad promedio de pacientes con diabetes.

    Args:
        pacientes: diccionario con los datos de los pacientes.

    Returns:
        float o None: promedio de edad o None si no hay
        pacientes con diabetes.
    """
    suma_edades = 0
    cantidad = 0

    for datos in pacientes.values():
        if datos["diabetico"]:
            suma_edades += datos["edad"]
            cantidad += 1

    if cantidad > 0:
        return suma_edades / cantidad

    return None


def existe_mayor_80_sin_diabetes(pacientes):
    """Comprueba si hay pacientes mayores de 80 sin diabetes.

    Args:
        pacientes: diccionario con los datos de los pacientes.

    Returns:
        bool: True si existe al menos uno, False si no.
    """
    for datos in pacientes.values():
        if datos["edad"] > 80 and not datos["diabetico"]:
            return True

    return False



def frecuencia_caracteres(cadena):
    """
    Explicación:
    Cuenta cuántas veces aparece cada carácter
    dentro de una cadena de texto.

    Arg:
    cadena: texto que se desea analizar.

    Return:
    Un diccionario con cada carácter como clave
    y su cantidad de apariciones como valor.
    """
    frecuencias = {}

    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1

    return frecuencias




def puede_vender(productos, codigo):
    """
    Explicación:
    Determina si se puede vender una unidad del producto.

    Arg:
    productos: diccionario con los productos del supermercado.
    codigo: código del producto que se desea vender.

    Return:
    True si el producto existe y tiene stock disponible.
    False si no existe o no tiene stock.
    """
    if codigo in productos and productos[codigo]["stock"] > 0:
        return True
    return False


def productos_bajo_stock(productos):
    """
    Explicación:
    Busca los productos cuyo stock actual es menor
    que su stock mínimo.

    Arg:
    productos: diccionario con los productos.

    Return:
    Una lista con el código y la descripción de cada producto.
    """
    lista = []

    for codigo, datos in productos.items():
        if datos["stock"] < datos["stock_minimo"]:
            lista.append((codigo, datos["descripcion"]))

    return lista


def contar_lacteos(productos):
    """
    Explicación:
    Cuenta cuántos productos de tipo lácteo hay registrados.

    Arg:
    productos: diccionario con los productos.

    Return:
    La cantidad de productos lácteos.
    """
    cantidad = 0

    for datos in productos.values():
        if datos["tipo"] == "lácteo":
            cantidad += 1

    return cantidad


def almacen_menor_stock(productos):
    """
    Explicación:
    Busca el producto de almacén con menor stock actual.

    Arg:
    productos: diccionario con los productos.

    Return:
    Una tupla con el código y la descripción del producto,
    o None si no hay productos de almacén.
    """
    menor = None

    for codigo, datos in productos.items():
        if datos["tipo"] == "almacén":
            if menor is None or datos["stock"] < productos[menor]["stock"]:
                menor = codigo

    if menor is not None:
        return (menor, productos[menor]["descripcion"])

    return None


def buscar_descripcion(productos, codigo):
    """
    Explicación:
    Busca la descripción de un producto por su código.

    Arg:
    productos: diccionario con los productos.
    codigo: código del producto que se busca.

    Return:
    La descripción si existe; None si no se encuentra.
    """
    if codigo in productos:
        return productos[codigo]["descripcion"]

    return None


def tipo_menor_stock(productos):
    """
    Explicación:
    Suma el stock actual de cada tipo de producto y determina
    qué tipo tiene menos unidades disponibles para la venta.

    Arg:
    productos: diccionario con los productos.

    Return:
    El tipo de producto con menor stock total, o None
    si no hay productos registrados.
    """
    stock_por_tipo = {}

    for datos in productos.values():
        tipo = datos["tipo"]

        if tipo not in stock_por_tipo:
            stock_por_tipo[tipo] = 0

        stock_por_tipo[tipo] += datos["stock"]

    if len(stock_por_tipo) == 0:
        return None

    menor_tipo = min(stock_por_tipo, key=stock_por_tipo.get)

    return menor_tipo


def procesar_pedido(productos, pedido):
    """
    Explicación:
    Procesa una lista de códigos de productos que un cliente
    desea comprar. Vende solamente los productos con stock,
    actualiza el inventario y calcula el total.

    Arg:
    productos: diccionario con los productos.
    pedido: lista de códigos de productos solicitados.

    Return:
    Una tupla con el monto total y la lista de códigos
    que pudieron venderse.
    """
    total = 0
    vendidos = []

    for codigo in pedido:
        if puede_vender(productos, codigo):
            total += productos[codigo]["precio"]
            productos[codigo]["stock"] -= 1
            vendidos.append(codigo)

    return (total, vendidos)




def sucesion_mira_y_deci(n):
    """
    Explicación:
    Genera los primeros n números de la sucesión Mira y Decí.
    Cada número se obtiene contando las repeticiones consecutivas
    de los dígitos del número anterior.

    Arg:
    n: cantidad de números que tendrá la sucesión.

    Return:
    Una lista con los primeros n números de la sucesión.
    """
    sucesion = []

    if n <= 0:
        return sucesion

    numero = "1"
    sucesion.append(int(numero))

    for i in range(n - 1):
        nuevo_numero = ""
        contador = 1

        for j in range(1, len(numero)):
            if numero[j] == numero[j - 1]:
                contador += 1
            else:
                nuevo_numero += str(contador) + numero[j - 1]
                contador = 1

        nuevo_numero += str(contador) + numero[-1]
        numero = nuevo_numero

        sucesion.append(int(numero))

    return sucesion
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
