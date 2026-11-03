""" Esta funcion recibe como parametro una lista.
    Evalua el contenido de la misma y retorna el valor minimo encontrado, o 
    retorna None si es una lista vacia."""
def minimo_elemento(lista):
  
    if (not lista):
        return None
    else :
        minimo=lista[0]
        for e in lista:
           if e < minimo :
               minimo=e
        return minimo
    
""" Funcion piedra_papel_tijera recibe como parametros dos strings, las cuales va a evaluar y teniendo 
    en cuentas las reglas del juego va a mostrar si hubo un ganador o hay empate """
    
def piedra_papel_tijera(jugador1,jugador2):
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
        
"""Funcion borrar_adyacentes recibe como parametro una lista de caracteres y retorna los mismos sin repeticiones"""

def borrar_adyacentes(lista) :
    nueva_lista=[]
    
    for caracter in lista :
        if caracter not in nueva_lista :
            nueva_lista.append(caracter)
    return nueva_lista

"""Funcion suma_digitos, recibe un numero como parametro, y recorre cada uno de sus digitos sumandolos"""
def suma_digitos(n):
    total = 0

    for digito in str(n):
        total = total + int(digito) 
    return total

"""Funcion sumatoria digitos, recibe una lista de numeros y llamando a la funcion suma_digitos, crea una nueva
    con los resultados de la sumatoria de cada numero"""
def sumatoria_digitos(lista):
    nueva_lista = []
    
    for e in lista:
        resultado_suma = suma_digitos(e)
        nueva_lista.append(resultado_suma)
            
    return nueva_lista 
""" Funcion dos_sumandos, recibe por parametros una lista de numeros enteros y un numero como valor de referencia
    Recorre cada indice de la lista y evalua las posibilidades de sumar 2 de ellos para encontrar el valor del numero de referencia ingresado"""

def dos_sumandos(lista,resultado):
    nueva_lista=[]
    
    for i in range(len(lista)):
        num1 = lista[i]
        for j in range(i + 1, len(lista)):
            num2 = lista[j]
            posible = num1 +num2 
            if (posible == resultado):
                nueva_lista=[i,j]    
    return nueva_lista

""" Funcion digitos_repetidos recibe como parametro un numero entero, lo pasa a string para poder recorrerlo digito por digito
    Luego ese digito lo pasa a entero nuevamente y lo agrega a una lista, antes de agregarlo evalua si esta repetido o no, y en caso 
    de ser un numero repetido, lo agrega a una nueva lista para retornar cuales son los numeros que se repiten"""
    
def digitos_repetidos(n):
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