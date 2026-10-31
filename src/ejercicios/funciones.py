"""Funciones reutilizables para los ejercicios del Trabajo Práctico 5."""

from typing import Any


def ingresar_nombres() -> list[str]:
    """Pide nombres por teclado hasta que se ingrese uno en blanco.

    Returns:
        list[str]: Nombres ingresados, en el orden de carga.
    """
    nombres: list[str] = []
    nombre = input("Ingrese un nombre (Enter para terminar): ")
    while nombre != "":
        nombres.append(nombre)
        nombre = input("Ingrese un nombre (Enter para terminar): ")
    return nombres


def imprimir_nombres(nombres: list[str]) -> None:
    """Muestra cada nombre de la lista en una línea, iterando sobre ella.

    Args:
        nombres (list[str]): Nombres a mostrar.
    """
    for nombre in nombres:
        print(nombre)


def minimo_elemento(lista: list[Any] | str) -> object:
    """Busca el menor elemento de una secuencia de valores comparables.

    Args:
        lista (list | str): Elementos comparables entre sí.

    Returns:
        object: El menor valor encontrado, o None si la secuencia está vacía.
    """
    if len(lista) == 0:
        return None
    return min(lista)


def piedra_papel_tijera(uno: str, dos: str) -> int:
    """Determina el ganador de una mano de piedra, papel o tijera.

    Args:
        uno (str): Elección del primer jugador.
        dos (str): Elección del segundo jugador.

    Returns:
        int: 1 si gana el primero, 2 si gana el segundo y 0 si empatan.
    """
    le_gana_a = {"piedra": "tijera", "tijera": "papel", "papel": "piedra"}
    eleccion_uno = uno.strip().lower()
    eleccion_dos = dos.strip().lower()
    resultado = 2
    if eleccion_uno == eleccion_dos:
        resultado = 0
    elif le_gana_a[eleccion_uno] == eleccion_dos:
        resultado = 1
    return resultado


def borrar_adyacentes(lista: list[str]) -> list[str]:
    """Elimina los caracteres repetidos que están uno al lado del otro.

    Args:
        lista (list[str]): Caracteres (strings de longitud 1).

    Returns:
        list[str]: Nueva lista con una sola ocurrencia por grupo adyacente.
    """
    resultado: list[str] = []
    for caracter in lista:
        if len(resultado) == 0 or resultado[-1] != caracter:
            resultado.append(caracter)
    return resultado


def suma_digitos(n: int) -> int:
    """Suma los dígitos de un número entero.

    Args:
        n (int): Número entero.

    Returns:
        int: Suma de sus dígitos.
    """
    numero = abs(n)
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma


def sumatoria_digitos(lista: list[int]) -> list[int]:
    """Calcula la suma de dígitos de cada número de una lista.

    Args:
        lista (list[int]): Números enteros positivos.

    Returns:
        list[int]: Suma de dígitos de cada número, en el mismo orden.
    """
    return [suma_digitos(numero) for numero in lista]


def dos_sumandos(lista: list[int], resultado: int) -> list[int]:
    """Busca dos posiciones distintas cuyos valores sumen el resultado.

    Args:
        lista (list[int]): Números donde buscar.
        resultado (int): Valor que deben sumar los dos elementos.

    Returns:
        list[int]: Los dos índices encontrados, o lista vacía si no existen.
    """
    indices: list[int] = []
    i = 0
    while i < len(lista) and len(indices) == 0:
        j = i + 1
        while j < len(lista) and len(indices) == 0:
            if lista[i] + lista[j] == resultado:
                indices = [i, j]
            j += 1
        i += 1
    return indices


def digitos_repetidos(n: int) -> list[int]:
    """Obtiene los dígitos que aparecen más de una vez en un número.

    Args:
        n (int): Número entero a analizar.

    Returns:
        list[int]: Dígitos repetidos, cada uno una sola vez.
    """
    texto = str(abs(n))
    repetidos: list[int] = []
    for caracter in texto:
        digito = int(caracter)
        if texto.count(caracter) > 1 and digito not in repetidos:
            repetidos.append(digito)
    return repetidos


def contar_palabras(texto: str) -> int:
    """Cuenta las palabras de un texto separadas por espacios.

    Args:
        texto (str): Texto a analizar.

    Returns:
        int: Cantidad de palabras.
    """
    return len(texto.split())


def letras_repetidas(palabra: str) -> list[str]:
    """Obtiene las letras que se repiten en una palabra.

    Ignora mayúsculas, dígitos y símbolos.

    Args:
        palabra (str): Palabra a analizar.

    Returns:
        list[str]: Letras repetidas en minúscula, cada una una sola vez.
    """
    letras = [caracter for caracter in palabra.lower() if caracter.isalpha()]
    repetidas: list[str] = []
    for letra in letras:
        if letras.count(letra) > 1 and letra not in repetidas:
            repetidas.append(letra)
    return repetidas


def contar_por_pais(ciudades: list[list[str]]) -> dict[str, int]:
    """Cuenta cuántas ciudades hay por país.

    Args:
        ciudades (list[list[str]]): Pares [ciudad, país].

    Returns:
        dict[str, int]: Cantidad de ciudades por cada país.
    """
    por_pais: dict[str, int] = {}
    for _, pais in ciudades:
        por_pais[pais] = por_pais.get(pais, 0) + 1
    return por_pais


def peliculas_por_director(
    peliculas: dict[str, dict[str, Any]],
) -> dict[str, int]:
    """Cuenta cuántas películas dirigió cada director.

    Args:
        peliculas (dict): Películas indexadas por título.

    Returns:
        dict[str, int]: Cantidad de películas por director.
    """
    conteo: dict[str, int] = {}
    for datos in peliculas.values():
        director = datos["director"]
        conteo[director] = conteo.get(director, 0) + 1
    return conteo


def director_con_mas_peliculas(
    peliculas: dict[str, dict[str, Any]],
) -> str | None:
    """Obtiene el director con más películas dirigidas.

    Args:
        peliculas (dict): Películas indexadas por título.

    Returns:
        str | None: Nombre del director, o None si no hay películas.
    """
    conteo = peliculas_por_director(peliculas)
    if len(conteo) == 0:
        return None
    return max(conteo, key=lambda director: conteo[director])


def actores_de_pelicula(
    peliculas: dict[str, dict[str, Any]], titulo: str,
) -> list[str]:
    """Devuelve los actores principales de una película.

    Args:
        peliculas (dict): Películas indexadas por título.
        titulo (str): Título de la película buscada.

    Returns:
        list[str]: Actores, o lista vacía si la película no existe.
    """
    if titulo not in peliculas:
        return []
    return peliculas[titulo]["actores"]


def peliculas_de_actor(
    peliculas: dict[str, dict[str, Any]], actor: str,
) -> list[str]:
    """Busca los títulos de las películas donde participó un actor.

    Args:
        peliculas (dict): Películas indexadas por título.
        actor (str): Nombre del actor.

    Returns:
        list[str]: Títulos donde participó el actor.
    """
    return [
        titulo for titulo, datos in peliculas.items()
        if actor in datos["actores"]
    ]


def comprimir_rle(texto: str) -> list[tuple[str, int]]:
    """Comprime un texto agrupando caracteres consecutivos idénticos.

    Args:
        texto (str): Texto a comprimir.

    Returns:
        list[tuple[str, int]]: Tuplas (carácter, cantidad).
    """
    comprimido: list[tuple[str, int]] = []
    for caracter in texto:
        if len(comprimido) > 0 and comprimido[-1][0] == caracter:
            comprimido[-1] = (caracter, comprimido[-1][1] + 1)
        else:
            comprimido.append((caracter, 1))
    return comprimido


def descomprimir_rle(lista_comprimida: list[tuple[str, int]]) -> str:
    """Reconstruye el texto original a partir de su compresión RLE.

    Args:
        lista_comprimida (list[tuple[str, int]]): Tuplas (carácter, cantidad).

    Returns:
        str: Texto descomprimido.
    """
    return "".join(
        caracter * cantidad for caracter, cantidad in lista_comprimida
    )


def tasa_compresion(
    texto_original: str, lista_comprimida: list[tuple[str, int]],
) -> tuple[float, bool]:
    """Calcula el porcentaje de reducción logrado por la compresión.

    Args:
        texto_original (str): Texto sin comprimir.
        lista_comprimida (list[tuple[str, int]]): Resultado de comprimir_rle.

    Returns:
        tuple[float, bool]: Porcentaje de reducción y si fue efectiva.
    """
    if len(texto_original) == 0:
        return 0.0, False
    tasa = (1 - len(lista_comprimida) / len(texto_original)) * 100
    return tasa, len(lista_comprimida) < len(texto_original)
