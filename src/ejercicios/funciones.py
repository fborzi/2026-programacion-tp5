#ejercicio 1501: comprobar si un elemento pertenece a una lista.
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

# Ejercicio 1504: carga interactiva de nombres.
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


# Ejercicio 1505: convertir los nombres de una lista a mayúsculas.
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