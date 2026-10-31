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