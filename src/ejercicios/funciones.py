
def minimo_elemento(lista):
    #Esta funcion recibe como parametro una lista.
    #Evalua el contenido de la misma y retorna el valor minimo encontrado, o 
    #retorna None si es una lista vacia.
    
    if (not lista):
        return None
    else :
        minimo=lista[0]
        for e in lista:
           if e < minimo :
               minimo=e
        return minimo
    
def piedra_papel_tijera(jugador1,jugador2):
    # Funcion piedra_papel_tijera recibe como parametros dos strings, las cuales va a evaluar y teniendo 
    # en cuentas las reglas del juego va a mostrar si hubo un ganador o hay empate 
    valor1=jugador1.lower()
    valor2=jugador2.lower()
    if valor1=="piedra" :
        if valor2 == "piedra" :
            return 0
        elif valor2 == "papel" :
            return 2
        else :
            return 1
    elif valor1 == "papel" :
        if valor2 == "papel" :
            return 0
        elif valor2 == "tijera" :
            return 2
        else :
            return 1
    else :
        if valor2 == "tijera" :
            return 0
        elif valor2 == "piedra" :
            return 2
        else :
            return 1
        

def borrar_adyacentes(lista) :
    #Funcion borrar_adyacentes recibe como parametro una lista de caracteres y retorna los mismos 
    # sin repeticiones

    nueva_lista=[]
    
    for caracter in lista :
        if caracter not in nueva_lista :
            nueva_lista.append(caracter)
    return nueva_lista


def suma_digitos(n):
   #Funcion suma_digitos, recibe un numero como parametro, y recorre cada uno de sus digitos sumandolos
    total = 0

    for digito in str(n):
        total = total + int(digito) 
    return total


def sumatoria_digitos(lista):
    #Funcion sumatoria digitos, recibe una lista de numeros y llamando a la funcion suma_digitos, crea una nueva
    #con los resultados de la sumatoria de cada numero
    nueva_lista = []
    
    for e in lista:
        resultado_suma = suma_digitos(e)
        nueva_lista.append(resultado_suma)
            
    return nueva_lista 


def dos_sumandos(lista,resultado):
    #Funcion dos_sumandos, recibe por parametros una lista de numeros enteros y un numero como valor de referencia
    #Recorre cada indice de la lista y evalua las posibilidades de sumar 2 de ellos para encontrar el valor del numero de referencia ingresado"""
    nueva_lista=[]
    
    for i in range(len(lista)):
        num1 = lista[i]
        for j in range(i + 1, len(lista)):
            num2 = lista[j]
            posible = num1 +num2 
            if (posible == resultado):
                nueva_lista=[i,j]    
    return nueva_lista


def digitos_repetidos(n):
    #Funcion digitos_repetidos recibe como parametro un numero entero, lo pasa a string para poder recorrerlo digito por digito
    #Luego ese digito lo pasa a entero nuevamente y lo agrega a una lista, antes de agregarlo evalua si esta repetido o no, y en caso 
    #de ser un numero repetido, lo agrega a una nueva lista para retornar cuales son los numeros que se repiten"""
    
    texto_numero = str(n)
    
    vistos = []   
    repetidos = [] 
    
    for digito in texto_numero:
        digito_int = int(digito)
        
        if digito_int in vistos:
            if digito_int not in repetidos:
                repetidos.append(digito_int)
        else:
            vistos.append(digito_int)
    return repetidos

def comprimir_rle(texto):
    # 
    if not texto:
        return []
    
    lista_comprimida = []
    caracter_actual = texto[0]
    contador = 1
    
    for i in range(1, len(texto)):
        if texto[i] == caracter_actual:
            contador += 1
        else:
            lista_comprimida.append((caracter_actual, contador))
            caracter_actual = texto[i]
            contador = 1
    lista_comprimida.append((caracter_actual, contador))
    
    return lista_comprimida


def descomprimir_rle(lista_comprimida):
    texto_original = ""

    for caracter, cantidad in lista_comprimida:
        texto_original += caracter * cantidad
        
    return texto_original

def tasa_compresion(texto_original, lista_comprimida):
    longitud_original = len(texto_original)
    longitud_comprimida = len(lista_comprimida)
    
    if longitud_original == 0:
        return 0.0, False
    
    tasa = (1 - longitud_comprimida / longitud_original) * 100
    
    efectiva = longitud_comprimida < longitud_original
    
    return tasa, efectiva
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

def contarPacientes(pacientes):
    """Cuenta la cantidad de pacientes en la lista
    args:Recibe una lista de pacientes
    return:retorna la cantidad de pacientes"""
    return len(pacientes)


def frecuencia_caracteres(cadena):
    """Retorna  la frecuencia de cada caracter en la cadena
    args:Recibe una cadena de texto
    return:retorna cantidad de veces que aparece cada caracter en la cadena"""
    
    frecuencias = {}
    for caracter in cadena:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias



def leer_productos():
    """Lee los productos hasta que se ingresa el código -1.
    args:No recibe parametros
    return:retorna un diccionario con los productos ingresados"""
    productos = {}
    codigo = int(input("Código de producto (-1 para terminar): "))
    while codigo != -1:
        tipo = input("Tipo (lácteo, almacén, verdulería, limpieza, carnicería, otros): ")
        descripcion = input("Descripción: ")
        stock = int(input("Stock actual: "))
        stock_minimo = int(input("Stock mínimo: "))
        precio = float(input("Precio unitario: "))
        productos[codigo] = {
            "tipo": tipo,
            "descripcion": descripcion,
            "stock": stock,
            "stock_minimo": stock_minimo,
            "precio": precio,
        }
        codigo = int(input("Código de producto (-1 para terminar): "))
    return productos



def se_puede_vender(productos, codigo):
    """Verifica si se puede vender un producto.
    args:Recibe un diccionario de productos y un código de producto
    return:retorna True si se puede vender, False en caso contrario"""
    return codigo in productos and productos[codigo]["stock"] > 0


def productos_bajo_minimo(productos):
    """Devuelve una lista de productos cuyo stock es menor al stock mínimo.
    args:Recibe un diccionario de productos
    return:retorna una lista de tuplas con el código y la descripción de los productos"""
    resultado = []
    for codigo, datos in productos.items():
        if datos["stock"] < datos["stock_minimo"]:
            resultado.append((codigo, datos["descripcion"]))
    return resultado


def cantidad_lacteos(productos):
    """Cuenta la cantidad de productos de tipo lácteo.
    args:Recibe un diccionario de productos
    return:retorna la cantidad de productos de tipo lácteo"""
    cantidad = 0
    for datos in productos.values():
        if datos["tipo"] == "lácteo":
            cantidad += 1
    return cantidad


def almacen_menor_stock(productos):
    """Encuentra el producto de tipo almacén con menor stock.
    args:Recibe un diccionario de productos
    return:retorna una tupla con el código y la descripción del producto"""
    menor_codigo = None
    for codigo, datos in productos.items():
        if datos["tipo"] == "almacén":
            if menor_codigo is None or datos["stock"] < productos[menor_codigo]["stock"]:
                menor_codigo = codigo
    if menor_codigo is None:
        return None
    return menor_codigo, productos[menor_codigo]["descripcion"]


def descripcion_producto(productos, codigo):
    """Obtiene la descripción de un producto dado su código.
    args:Recibe un diccionario de productos y un código de producto
    return:retorna la descripción del producto o None si no se encuentra"""
    if codigo in productos:
        return productos[codigo]["descripcion"]
    return None


def tipo_menor_stock(productos):
    """Encuentra el tipo de producto con menor stock total.
    args:Recibe un diccionario de productos
    return:retorna el tipo de producto con menor stock total"""
    stock_por_tipo = {}
    for datos in productos.values():
        tipo = datos["tipo"]
        stock_por_tipo[tipo] = stock_por_tipo.get(tipo, 0) + datos["stock"]
    if not stock_por_tipo:
        return None
    menor_tipo = None
    for tipo, total in stock_por_tipo.items():
        if menor_tipo is None or total < stock_por_tipo[menor_tipo]:
            menor_tipo = tipo
    return menor_tipo


def procesar_pedido(productos, pedido):
    """Retorna (monto_total, lista_de_codigos_vendidos)
    args:Recibe un diccionario de productos y una lista de códigos de productos
    return:retorna el monto total del pedido y la lista de códigos vendidos"""
    total = 0
    vendidos = []
    for codigo in pedido:
        if se_puede_vender(productos, codigo):
            productos[codigo]["stock"] -= 1
            total += productos[codigo]["precio"]
            vendidos.append(codigo)
    return total, vendidos



def siguiente_mira_y_deci(numero):
    """Retorna el siguiente número en la secuencia "mira y deci"
    args:Recibe un número entero
    return:retorna el siguiente número en la secuencia"""
    texto = str(numero)
    resultado = ""
    contador = 1
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            resultado += str(contador) + texto[i - 1]
            contador = 1
    resultado += str(contador) + texto[-1]
    return int(resultado)


def sucesion_mira_y_deci(n):
    """Genera la sucesión "mira y deci" hasta el n-ésimo término
    args:Recibe un número entero n
    return:retorna una lista con los primeros n términos de la sucesión"""
    sucesion = []
    actual = 1
    for _ in range(n):
        sucesion.append(actual)
        actual = siguiente_mira_y_deci(actual)
    return sucesion
 
