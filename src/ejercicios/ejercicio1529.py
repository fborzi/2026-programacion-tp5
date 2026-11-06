"""Ejercicio 1529: sucesión Mira y Decí."""


def siguiente_termino(numero: int) -> int:
    """Genera el término siguiente contando dígitos consecutivos.

    Args:
        numero: Número entero que se analizará.
    """
    cadena = str(numero)
    resultado = ""
    indice = 0

    while indice < len(cadena):
        digito = cadena[indice]
        cantidad = 0

        while indice < len(cadena) and cadena[indice] == digito:
            cantidad += 1
            indice += 1

        resultado += str(cantidad) + digito

    return int(resultado)


def sucesion_mira_y_deci(n: int) -> list[int]:
    """Devuelve los primeros n términos de la sucesión Mira y Decí.

    Args:
        n: Cantidad de términos que se generarán.
    """
    sucesion: list[int] = []

    if n <= 0:
        return sucesion

    actual = 1

    for _ in range(n):
        sucesion.append(actual)
        actual = siguiente_termino(actual)

    return sucesion


def main() -> None:
    """Ejecuta ejemplos de la sucesión."""
    print(sucesion_mira_y_deci(9))
    print(sucesion_mira_y_deci(1))
    print(sucesion_mira_y_deci(0))


if __name__ == "__main__":
    main()
