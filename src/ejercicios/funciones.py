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

