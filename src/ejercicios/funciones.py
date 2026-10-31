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

