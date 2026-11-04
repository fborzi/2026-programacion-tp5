""" Funciones del TP5 """


# 1504 Usada también en el ejercicio 1505 y 1528
def cargar_nombres() -> list:
    """Carga nombres por teclado hasta que se ingresa uno en blanco.

    Args:
        No recibe argumentos.

    Returns:
        Una lista con los nombres ingresados, en el orden de ingreso.
    """
    nombres: list = []
    nombre: str = input("Ingrese un nombre: ")
    while nombre != "":
        nombres.append(nombre)
        nombre = input("Ingrese un nombre: ")
    return nombres


# 1505
def convertir_a_mayusculas(nombres: list) -> list:
    """Produce una nueva lista con los nombres en mayúsculas.

    Args:
        nombres: es una lista de cadenas.

    Returns:
        Una nueva lista con cada nombre convertido a mayúsculas.
    """
    nombres_mayusculas: list = []
    for nombre in nombres:
        nombres_mayusculas.append(nombre.upper())
    return nombres_mayusculas


# 1506
def minimo_elemento(lista: list | str) -> object:
    """Busca el mínimo valor de una lista de elementos comparables.

    Args:
        lista: es una lista o cadena de elementos comparables entre sí.

    Returns:
        El mínimo valor encontrado, o None si la lista está vacía.
    """
    minimo: object = None
    for elemento in lista:
        if minimo is None or elemento < minimo:
            minimo = elemento
    return minimo


# 1507
def dos_minimos(lista: list) -> tuple:
    """Busca los dos valores menores de una lista de elementos comparables.

    Args:
        lista: es una lista de elementos comparables entre sí.

    Returns:
        Una tupla con el menor y el segundo menor valor. Si la lista
        tiene menos de dos elementos, None por cada elemento faltante.
    """
    primero: object = None
    segundo: object = None
    for elemento in lista:
        if primero is None or elemento < primero:
            segundo = primero
            primero = elemento
        elif segundo is None or elemento < segundo:
            segundo = elemento
    return (primero, segundo)


# 1508
def piedra_papel_tijera(uno: str, dos: str) -> int:
    """Determina el ganador de una jugada de piedra, papel o tijera.

    Args:
        uno: es la elección del primer jugador: 'piedra', 'papel' o
            'tijera', sin distinguir mayúsculas de minúsculas.
        dos: es la elección del segundo jugador, con el mismo formato.

    Returns:
        1 si ganó el primer jugador, 2 si ganó el segundo jugador
        o 0 si hubo empate.
    """
    eleccion_uno: str = uno.lower()
    eleccion_dos: str = dos.lower()
    resultado: int = 2
    if eleccion_uno == eleccion_dos:
        resultado = 0
    elif ((eleccion_uno == "piedra" and eleccion_dos == "tijera")
          or (eleccion_uno == "tijera" and eleccion_dos == "papel")
          or (eleccion_uno == "papel" and eleccion_dos == "piedra")):
        resultado = 1
    return resultado


# 1509 Usada también en el ejercicio 1518 y 1529
def digitos(numero: int) -> list:
    """Descompone un número entero en la lista de sus dígitos.

    Args:
        numero: es un entero.

    Returns:
        Una lista con los dígitos del número, en el mismo orden en que
        aparecen.
    """
    lista_digitos: list = []
    for caracter in str(abs(numero)):
        lista_digitos.append(int(caracter))
    return lista_digitos


# 1510
def borrar_adyacentes(lista: list) -> list:
    """Elimina los caracteres repetidos que están uno al lado del otro.

    Args:
        lista: es una lista de caracteres (cadenas de longitud 1).

    Returns:
        Una nueva lista con una única ocurrencia de cada grupo de
        caracteres adyacentes repetidos.
    """
    resultado: list = []
    for caracter in lista:
        if resultado == [] or caracter != resultado[-1]:
            resultado.append(caracter)
    return resultado


# 1511 Usada también en el ejercicio 1529 y 1530
def ocurrencias(lista: list) -> list:
    """Cuenta las ocurrencias contiguas de cada elemento de una lista.

    Args:
        lista: es una lista de elementos de cualquier tipo.

    Returns:
        Una lista de listas, cada una formada por un elemento y la
        cantidad de veces seguidas que aparece, en el orden original.
    """
    resultado: list = []
    for elemento in lista:
        if resultado != [] and resultado[-1][0] == elemento:
            resultado[-1][1] += 1
        else:
            resultado.append([elemento, 1])
    return resultado


# 1512 - Usada por sumatoria_digitos, corresponde a este mismo ejercicio
def suma_digitos(n: int) -> int:
    """Calcula la suma de los dígitos de un número entero.

    Args:
        n: es un entero.

    Returns:
        La suma de los dígitos del número como entero.
    """
    numero: int = abs(n)
    suma: int = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma


# 1512
def sumatoria_digitos(lista: list) -> list:
    """Calcula la suma de los dígitos de cada número de una lista.

    Args:
        lista: es una lista de números enteros positivos.

    Returns:
        Una lista con la suma de los dígitos de cada número, en el
        mismo orden.
    """
    sumas: list = []
    for numero in lista:
        sumas.append(suma_digitos(numero))
    return sumas


# 1513
def indice_mayor(lista: list) -> int | None:
    """Busca el índice en el que se encuentra el mayor número de una lista.

    Args:
        lista: es una lista de números.

    Returns:
        El índice del mayor número como entero, o None si la lista está
        vacía.
    """
    indice: int | None = None
    for posicion in range(len(lista)):
        if indice is None or lista[posicion] > lista[indice]:
            indice = posicion
    return indice


# 1514
def dos_sumandos(lista: list, resultado: int) -> list:
    """Busca dos elementos de una lista cuya suma da un resultado dado.

    Args:
        lista: es una lista de números.
        resultado: es el número que debe dar la suma.

    Returns:
        Una lista con los índices de los dos elementos cuya suma da el
        resultado, sin usar el mismo elemento dos veces, o una lista
        vacía si no existen.
    """
    indices: list = []
    for primero in range(len(lista)):
        for segundo in range(primero + 1, len(lista)):
            if indices == [] and lista[primero] + lista[segundo] == resultado:
                indices = [primero, segundo]
    return indices


# 1515 - Usada por obtenerProvincia
def obtenerCiudad(personas: list, DNI: int) -> str | None:
    """Obtiene la ciudad donde vive una persona a partir de su DNI.

    Args:
        personas: es una lista de listas con nombre, DNI y ciudad.
        DNI: es el DNI de la persona buscada.

    Returns:
        El nombre de la ciudad donde vive la persona, o None si no se
        encuentra ninguna persona con ese DNI.
    """
    ciudad: str | None = None
    for persona in personas:
        if persona[1] == DNI:
            ciudad = persona[2]
    return ciudad


# 1515  Usa obtenerCiudad y la usa contarPoblacion
def obtenerProvincia(personas: list, ciudades: list, DNI: int) -> str | None:
    """Obtiene la provincia donde vive una persona a partir de su DNI.

    Args:
        personas: es una lista de listas con nombre, DNI y ciudad.
        ciudades: es una lista de listas con ciudad y provincia.
        DNI: es el DNI de la persona buscada.

    Returns:
        El nombre de la provincia donde vive la persona, o None si no se
        encuentra la persona o su ciudad.
    """
    ciudad: str | None = obtenerCiudad(personas, DNI)
    provincia: str | None = None
    for datos_ciudad in ciudades:
        if datos_ciudad[0] == ciudad:
            provincia = datos_ciudad[1]
    return provincia


# 1515 Usa obtenerProvincia
def contarPoblacion(personas: list, ciudades: list, provincia: str) -> int:
    """Cuenta cuántas personas viven en una provincia.

    Args:
        personas: es una lista de listas con nombre, DNI y ciudad.
        ciudades: es una lista de listas con ciudad y provincia.
        provincia: es el nombre de la provincia.

    Returns:
        La cantidad de personas que viven en la provincia como entero.
    """
    cantidad: int = 0
    for persona in personas:
        if obtenerProvincia(personas, ciudades, persona[1]) == provincia:
            cantidad += 1
    return cantidad


# 1518, Usa digitos y la usa el ejercicio 1519
def digitos_repetidos(n: int) -> list:
    """Obtiene los dígitos que se repiten en un número entero.

    Args:
        n: es un entero.

    Returns:
        Una lista con los dígitos que aparecen más de una vez en el
        número, cada uno una única vez.
    """
    lista_digitos: list = digitos(n)
    repetidos: list = []
    for digito in lista_digitos:
        if lista_digitos.count(digito) > 1 and digito not in repetidos:
            repetidos.append(digito)
    return repetidos


# 1520
def letras_repetidas(palabra: str) -> list:
    """Obtiene las letras que se repiten en una palabra.

    Args:
        palabra: es una cadena de caracteres.

    Returns:
        Una lista con las letras que aparecen más de una vez, sin
        distinguir mayúsculas de minúsculas y excluyendo dígitos y
        símbolos, cada una una única vez.
    """
    minusculas: str = palabra.lower()
    repetidas: list = []
    for caracter in minusculas:
        if (caracter.isalpha() and minusculas.count(caracter) > 1
                and caracter not in repetidas):
            repetidas.append(caracter)
    return repetidas


# 1521
def cantidad_vocales_diferentes(palabra: str) -> int:
    """Cuenta cuántas vocales diferentes tiene una palabra.

    Args:
        palabra: es una cadena de caracteres.

    Returns:
        La cantidad de vocales distintas de la palabra como entero, sin
        distinguir acentos ni mayúsculas de minúsculas.
    """
    sin_tildes = str.maketrans("áéíóúü", "aeiouu")
    letras: set = set(palabra.lower().translate(sin_tildes))
    return len(letras & set("aeiou"))


# 1521
def leer_texto() -> str:
    """Lee líneas de texto hasta recibir una terminada en '*'.

    Args:
        No recibe argumentos.

    Returns:
        El texto completo con las líneas unidas por un espacio y sin el
        '*' final.
    """
    texto: str = ""
    linea: str = input("Ingrese una linea: ")
    while not linea.endswith("*"):
        texto += linea + " "
        linea = input("Ingrese una linea: ")
    texto += linea[:-1]
    return texto


# 1521
def contar_oraciones_largas(oraciones: list) -> int:
    """Cuenta las oraciones que tienen más de cinco palabras.

    Args:
        oraciones: es una lista de oraciones.

    Returns:
        La cantidad de oraciones con más de cinco palabras como entero.
    """
    cantidad: int = 0
    for oracion in oraciones:
        if len(oracion.split()) > 5:
            cantidad += 1
    return cantidad


# 1523
def edad_promedio_diabeticos(pacientes: dict) -> float | None:
    """Calcula la edad promedio de los pacientes con diabetes.

    Args:
        pacientes: es un diccionario con el DNI como clave y una lista
            con edad, sexo y si es diabético como valor.

    Returns:
        La edad promedio de los pacientes diabéticos, o None si no hay
        ninguno.
    """
    suma_edades: int = 0
    cantidad: int = 0
    promedio: float | None = None
    for dni in pacientes:
        if pacientes[dni][2]:
            suma_edades += pacientes[dni][0]
            cantidad += 1
    if cantidad > 0:
        promedio = suma_edades / cantidad
    return promedio


# 1523
def hay_mayor_sin_diabetes(pacientes: dict) -> bool:
    """Indica si hay algún paciente mayor de 80 años sin diabetes.

    Args:
        pacientes: es un diccionario con el DNI como clave y una lista
            con edad, sexo y si es diabético como valor.

    Returns:
        True si existe al menos un paciente mayor de 80 años sin
        diabetes, False en caso contrario.
    """
    existe: bool = False
    for dni in pacientes:
        if pacientes[dni][0] > 80 and not pacientes[dni][2]:
            existe = True
    return existe


# 1524
def cargar_socios() -> dict:
    """Carga los datos de los socios por teclado hasta que se ingresa el DNI 0.

    Args:
        No recibe argumentos.

    Returns:
        Un diccionario con el DNI como clave y una lista con nombre,
        apellido, edad y si tiene la cuota al día como valor.
    """
    socios: dict = {}
    dni: int = int(input("Ingrese el DNI (0 para terminar): "))
    while dni != 0:
        nombre: str = input("Ingrese el nombre: ")
        apellido: str = input("Ingrese el apellido: ")
        edad: int = int(input("Ingrese la edad: "))
        cuota_al_dia: bool = input("¿Tiene la cuota al dia? (s/n): ") == "s"
        socios[dni] = [nombre, apellido, edad, cuota_al_dia]
        dni = int(input("Ingrese el DNI (0 para terminar): "))
    return socios


# 1524
def contar_morosos(socios: dict) -> int:
    """Cuenta los socios que no tienen la cuota al día.

    Args:
        socios: es un diccionario con el DNI como clave y una lista con
            nombre, apellido, edad y si tiene la cuota al día como valor.

    Returns:
        La cantidad de socios morosos como entero.
    """
    cantidad: int = 0
    for dni in socios:
        if not socios[dni][3]:
            cantidad += 1
    return cantidad


# 1524
def dni_mayor_edad(socios: dict) -> int | None:
    """Busca el DNI del socio de mayor edad.

    Args:
        socios: es un diccionario con el DNI como clave y una lista con
            nombre, apellido, edad y si tiene la cuota al día como valor.

    Returns:
        El DNI del socio de mayor edad como entero, o None si no hay
        socios.
    """
    dni_mayor: int | None = None
    for dni in socios:
        if dni_mayor is None or socios[dni][2] > socios[dni_mayor][2]:
            dni_mayor = dni
    return dni_mayor


# 1525
def frecuencia_caracteres(cadena: str) -> dict:
    """Calcula cuántas veces aparece cada carácter de una cadena.

    Args:
        cadena: es una cadena de caracteres.

    Returns:
        Un diccionario con cada carácter como clave y la cantidad de
        veces que aparece como valor.
    """
    frecuencias: dict = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias


# 1526 - Versión a
def contar_ciudades_sin_almacenar() -> tuple:
    """Lee ciudades y países hasta la ciudad 'zz' sin almacenar ciudades.

    Args:
        No recibe argumentos.

    Returns:
        Una tupla con la cantidad total de ciudades ingresadas y un
        diccionario con cada país como clave y su cantidad de ciudades
        como valor.
    """
    total: int = 0
    por_pais: dict = {}
    ciudad: str = input("Ingrese una ciudad (zz para terminar): ")
    while ciudad != "zz":
        pais: str = input("Ingrese el pais: ")
        total += 1
        if pais in por_pais:
            por_pais[pais] += 1
        else:
            por_pais[pais] = 1
        ciudad = input("Ingrese una ciudad (zz para terminar): ")
    return (total, por_pais)


# 1526 - Versión b
def cargar_ciudades() -> list:
    """Lee ciudades y países hasta la ciudad 'zz' y los almacena.

    Args:
        No recibe argumentos.

    Returns:
        Una lista en la que cada elemento es una lista con la ciudad y
        su país.
    """
    ciudades: list = []
    ciudad: str = input("Ingrese una ciudad (zz para terminar): ")
    while ciudad != "zz":
        pais: str = input("Ingrese el pais: ")
        ciudades.append([ciudad, pais])
        ciudad = input("Ingrese una ciudad (zz para terminar): ")
    return ciudades


# 1526 - Versión b
def contar_por_pais(ciudades: list) -> dict:
    """Cuenta cuántas ciudades hay de cada país en una lista.

    Args:
        ciudades: es una lista en la que cada elemento es una lista con
            la ciudad y su país.

    Returns:
        Un diccionario con cada país como clave y su cantidad de
        ciudades como valor.
    """
    por_pais: dict = {}
    for ciudad in ciudades:
        if ciudad[1] in por_pais:
            por_pais[ciudad[1]] += 1
        else:
            por_pais[ciudad[1]] = 1
    return por_pais


# 1527
def cargar_productos() -> dict:
    """Carga los datos de los productos por teclado hasta el código -1.

    Args:
        No recibe argumentos.

    Returns:
        Un diccionario con el código como clave y una lista con tipo,
        descripción, stock actual, stock mínimo y precio unitario como
        valor.
    """
    productos: dict = {}
    codigo: int = int(input("Ingrese el codigo (-1 para terminar): "))
    while codigo != -1:
        tipo: str = input("Ingrese el tipo: ")
        descripcion: str = input("Ingrese la descripcion: ")
        stock: int = int(input("Ingrese el stock actual: "))
        stock_minimo: int = int(input("Ingrese el stock minimo: "))
        precio: float = float(input("Ingrese el precio unitario: "))
        productos[codigo] = [tipo, descripcion, stock, stock_minimo, precio]
        codigo = int(input("Ingrese el codigo (-1 para terminar): "))
    return productos


# 1527 - Usada también en procesar_pedido
def se_puede_vender(productos: dict, codigo: int) -> bool:
    """Indica si es posible vender una unidad de un producto.

    Args:
        productos: es un diccionario con el código como clave y una
            lista con tipo, descripción, stock actual, stock mínimo y
            precio unitario como valor.
        codigo: es el código del producto.

    Returns:
        True si el producto existe y tiene stock, False en caso
        contrario.
    """
    return codigo in productos and productos[codigo][2] > 0


# 1527
def productos_bajo_minimo(productos: dict) -> list:
    """Obtiene los productos que están por debajo del stock mínimo.

    Args:
        productos: es un diccionario con el código como clave y una
            lista con tipo, descripción, stock actual, stock mínimo y
            precio unitario como valor.

    Returns:
        Una lista en la que cada elemento es una lista con el código y
        la descripción de un producto por debajo del stock mínimo.
    """
    bajo_minimo: list = []
    for codigo in productos:
        if productos[codigo][2] < productos[codigo][3]:
            bajo_minimo.append([codigo, productos[codigo][1]])
    return bajo_minimo


# 1527
def contar_tipo(productos: dict, tipo: str) -> int:
    """Cuenta cuántos productos hay de un tipo.

    Args:
        productos: es un diccionario con el código como clave y una
            lista con tipo, descripción, stock actual, stock mínimo y
            precio unitario como valor.
        tipo: es el tipo de producto.

    Returns:
        La cantidad de productos de ese tipo como entero.
    """
    cantidad: int = 0
    for codigo in productos:
        if productos[codigo][0] == tipo:
            cantidad += 1
    return cantidad


# 1527
def codigo_menor_stock(productos: dict, tipo: str) -> int | None:
    """Busca el código del producto de un tipo con menor stock actual.

    Args:
        productos: es un diccionario con el código como clave y una
            lista con tipo, descripción, stock actual, stock mínimo y
            precio unitario como valor.
        tipo: es el tipo de producto.

    Returns:
        El código del producto de ese tipo con menor stock, o None si
        no hay productos de ese tipo.
    """
    codigo_menor: int | None = None
    for codigo in productos:
        if productos[codigo][0] == tipo and (
                codigo_menor is None
                or productos[codigo][2] < productos[codigo_menor][2]):
            codigo_menor = codigo
    return codigo_menor


# 1527
def tipo_menor_stock(productos: dict) -> str | None:
    """Busca el tipo de producto con menos unidades disponibles.

    Args:
        productos: es un diccionario con el código como clave y una
            lista con tipo, descripción, stock actual, stock mínimo y
            precio unitario como valor.

    Returns:
        El tipo con menor suma de stock entre sus productos, o None si
        no hay productos.
    """
    stock_por_tipo: dict = {}
    tipo_menor: str | None = None
    for codigo in productos:
        tipo: str = productos[codigo][0]
        if tipo in stock_por_tipo:
            stock_por_tipo[tipo] += productos[codigo][2]
        else:
            stock_por_tipo[tipo] = productos[codigo][2]
    for tipo in stock_por_tipo:
        if (tipo_menor is None
                or stock_por_tipo[tipo] < stock_por_tipo[tipo_menor]):
            tipo_menor = tipo
    return tipo_menor


# 1527 Usa se_puede_vender
def procesar_pedido(productos: dict, pedido: list) -> tuple:
    """Procesa un pedido, reduciendo el stock de lo vendido.

    Args:
        productos: es un diccionario con el código como clave y una
            lista con tipo, descripción, stock actual, stock mínimo y
            precio unitario como valor.
        pedido: es una lista con los códigos de los productos a comprar.

    Returns:
        Una tupla con el monto total a pagar y una lista con los
        códigos de los productos que pudieron venderse.
    """
    monto: float = 0.0
    vendidos: list = []
    for codigo in pedido:
        if se_puede_vender(productos, codigo):
            monto += productos[codigo][4]
            vendidos.append(codigo)
            productos[codigo][2] -= 1
    return (monto, vendidos)


# 1528  Utilisa cargar_nombres
def cargar_peliculas() -> dict:
    """Carga los datos de las películas hasta que se ingresa un título vacío.

    Args:
        No recibe argumentos.

    Returns:
        Un diccionario con el título como clave y una lista con
        director, año de estreno y lista de actores principales como
        valor.
    """
    peliculas: dict = {}
    titulo: str = input("Ingrese el titulo (vacio para terminar): ")
    while titulo != "":
        director: str = input("Ingrese el director: ")
        anio: int = int(input("Ingrese el anio de estreno: "))
        print("Ingrese los actores principales (vacio para terminar)")
        actores: list = cargar_nombres()
        peliculas[titulo] = [director, anio, actores]
        titulo = input("Ingrese el titulo (vacio para terminar): ")
    return peliculas


# 1528 Usada también en director_con_mas_peliculas
def peliculas_por_director(peliculas: dict) -> dict:
    """Cuenta cuántas películas dirigió cada director.

    Args:
        peliculas: es un diccionario con el título como clave y una
            lista con director, año de estreno y lista de actores como
            valor.

    Returns:
        Un diccionario con cada director como clave y su cantidad de
        películas como valor.
    """
    por_director: dict = {}
    for titulo in peliculas:
        director: str = peliculas[titulo][0]
        if director in por_director:
            por_director[director] += 1
        else:
            por_director[director] = 1
    return por_director


# 1528 utiliza peliculas_por_director
def director_con_mas_peliculas(peliculas: dict) -> str | None:
    """Busca el director que dirigió más películas.

    Args:
        peliculas: es un diccionario con el título como clave y una
            lista con director, año de estreno y lista de actores como
            valor.

    Returns:
        El nombre del director con más películas, o None si no hay
        películas.
    """
    por_director: dict = peliculas_por_director(peliculas)
    director_mayor: str | None = None
    for director in por_director:
        if (director_mayor is None
                or por_director[director] > por_director[director_mayor]):
            director_mayor = director
    return director_mayor


# 1528
def peliculas_de_actor(peliculas: dict, actor: str) -> list:
    """Obtiene los títulos de las películas en las que participó un actor.

    Args:
        peliculas: es un diccionario con el título como clave y una
            lista con director, año de estreno y lista de actores como
            valor.
        actor: es el nombre del actor.

    Returns:
        Una lista con los títulos de las películas donde participó.
    """
    titulos: list = []
    for titulo in peliculas:
        if actor in peliculas[titulo][2]:
            titulos.append(titulo)
    return titulos


# 1529 - Usa digitos 1509 y ocurrencias 1511
def sucesion_mira_y_deci(n: int) -> list:
    """Calcula los primeros n números de la sucesión Mira y Decí.

    Args:
        n: es la cantidad de números a calcular.

    Returns:
        Una lista con los primeros n números de la sucesión, que
        comienza en 1 y donde cada número describe los dígitos
        consecutivos del anterior.
    """
    sucesion: list = []
    actual: int = 1
    for _ in range(n):
        sucesion.append(actual)
        siguiente: str = ""
        for par in ocurrencias(digitos(actual)):
            siguiente += str(par[1]) + str(par[0])
        actual = int(siguiente)
    return sucesion


# 1530 - Usa ocurrencias 1511
def comprimir_rle(texto: str) -> list:
    """Comprime un texto agrupando los caracteres consecutivos idénticos.

    Args:
        texto: es una cadena de caracteres.

    Returns:
        Una lista de tuplas con el formato (carácter, cantidad), una por
        cada grupo de caracteres consecutivos idénticos.
    """
    comprimida: list = []
    for par in ocurrencias(list(texto)):
        comprimida.append((par[0], par[1]))
    return comprimida


# 1530
def descomprimir_rle(lista_comprimida: list) -> str:
    """Reconstruye un texto a partir de su compresión RLE.

    Args:
        lista_comprimida: es una lista de tuplas con el formato
            (carácter, cantidad).

    Returns:
        La cadena de texto original.
    """
    texto: str = ""
    for tupla in lista_comprimida:
        texto += tupla[0] * tupla[1]
    return texto


# 1530
def tasa_compresion(texto_original: str, lista_comprimida: list) -> tuple:
    """Calcula el porcentaje de reducción de una compresión RLE.

    Args:
        texto_original: es la cadena de texto sin comprimir.
        lista_comprimida: es la lista de tuplas generada al comprimir.

    Returns:
        Una tupla con el porcentaje de reducción y un booleano que
        indica si la compresión fue efectiva.
    """
    tasa: float = 0.0
    efectiva: bool = len(lista_comprimida) < len(texto_original)
    if len(texto_original) > 0:
        tasa = (1 - len(lista_comprimida) / len(texto_original)) * 100
    return (tasa, efectiva)
