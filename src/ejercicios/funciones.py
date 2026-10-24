#1502 ejercicio: conteo de elementos de una lista

def contar_elementos(lista: list, elemento: int) -> int:
    """cuenta cuantas veces aparece un elemento en una lista.
    args:
        lista: lista de elementos
        elemento: elemento a contar
    returns:
        int: cantidad de veces que aparece el elemento en la lista"""
    return lista.count(elemento)

#1504 carga interactiva de nombres en una lista carga 
"""este codigo de funciones sino recibimos una lista,
 creamos una vacia depues solcticamos un nombre por teclado , 
 si el nombre esta vacio devolvemos la lista."""


def cargar_nombres(nombres: list = None) -> list:


    """
    Solicita nombres y los guarda hasta recibir una entrada en blanco.
    Args:
        nombres: lista donde se guardan los nombres.
    Returns:
        la lista completa de nombres ingresados.
    """
    if nombres is None:
        nombres = []

    nombre = input("ingrese un nombre (Enter para terminar): ")
    if nombre == "":
        return nombres
    nombres.append(nombre)
    return cargar_nombres(nombres)

#ejercicio 1506: busqueda de un elemento minimo  en una lista
"""en funciones py devuelve el menor elementos de la lista  comprueba si la
la lista tiene elementos,  cuando la lista esta vacia devuelve un none"""

def minimo_elemento(lista):
    """Busca el menor elemento de una lista.
    Args:
        lista (list): Elementos comparables entre sí.

    Returns:
        object | None: El menor elemento o None si la lista está vacia.
    """
    return min(lista) if lista else None

# Ejercicio 1508: juego de piedra, papel o tijera
"""
Este código determina el ganador de un juego de piedra, papel o tijera entre dos jugadores."""
def piedra_papel_tijera(uno, dos):
    """
    Determina el ganador de piedra, papel o tijera.

    Args:
        uno (str): Eleccion del primer jugador.
        dos (str): Eleccion del segundo jugador.

    Returns:
        int: 1 si gana el primero, 2 si gana el segundo
        o 0 si empatan.

    Raises:
        ValueError: Si alguna elección no es valida.
    """

    uno, dos = uno.lower().strip(), dos.lower().strip()

    opciones = {"piedra", "papel", "tijera"}

    if uno not in opciones or dos not in opciones:
        raise ValueError("las opciones deben ser piedra, papel o tijera.")

    
    if uno == dos:
        return 0

    if (uno, dos) in {
        ("piedra", "tijera"),
        ("tijera", "papel"),
        ("papel", "piedra")
    }:
        return 1

    return 2


# Ejercicio 1510: eliminacion de caracteres adyacentes repetidos.
"""Este codigo elimina caracteres repetidos consecutivamente de una lista."""

def borrar_adyacentes(lista):
    """
    Elimina caracteres repetidos consecutivamente.

    Args:
        lista (list): Lista de caracteres.

    Returns:
        list: Lista con una sola ocurrencia por grupo consecutivo.
    """
  
    return [
        elemento
        for i, elemento in enumerate(lista)
        if i == 0 or elemento != lista[i - 1]
    ]

# Ejercicio 1512: sumatoria de dígitos de elementos de una lista.
"""Este codigo calcula la suma de los digitos de cada numero en una lista."""

def digitos(numero):
    """
    Separa los dígitos de un número.

    Args:
        numero (int): Número que queremos separar.

    Returns:
        list: Lista de dígitos.
    """

    return [int(digito) for digito in str(abs(numero))]


def suma_digitos(numero):
    """
    Suma los digitos de un numero entero.

    Args:
        numero (int): Numero cuyos dígitos se suman.

    Returns:
        int: Suma de los digitos.
    """
    
    return sum(digitos(numero))


def sumatoria_digitos(lista):
    """
    Calcula la suma de digitos de cada numero.

    Args:
        lista (list[int]): Lista de numeros enteros.

    Returns:
        list[int]: Lista con la suma de los digitos.
    """

    return [suma_digitos(numero) for numero in lista]



