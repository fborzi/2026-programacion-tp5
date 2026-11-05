
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