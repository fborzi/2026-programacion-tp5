def pertenece(lista: list, elemento) -> bool:
    """
    Comprueba si un elemento se encuentra en una lista.
    Args:
        lista: lista que queremos consultar.
        elemento: elemento que queremos buscar.
    Returns: 
        True si pertenece a la lista y False si no pertenece.
    """
    
    return elemento in lista

def buscar_indice(lista: list, elemento) -> int:
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