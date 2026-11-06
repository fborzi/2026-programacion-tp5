
""" Ejercicio 1509: descomposición de un número en dígitos.
    Devuelve una lista con los dígitos de un número entero.
    Prueba la descomposición de diferentes números."""


def digitos(numero: int) -> list[int]:
    """Devuelve una lista con los dígitos de un número entero."""
    numero_texto: str = str(abs(numero))
    lista_digitos: list[int] = []
    for caracter in numero_texto:
        digito: int = int(caracter)
        lista_digitos.append(digito)
    return lista_digitos


def main() -> None:
    """Ejecuta ejemplos de separación de dígitos."""
    print(digitos(18413))
    print(digitos(12345))
    print(digitos(7))
    print(digitos(0))
    print(digitos(-456))


if __name__ == "__main__":
    main()
