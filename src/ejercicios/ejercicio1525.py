"""Ejercicio 1525: frecuencia de caracteres."""


def frecuencia_caracteres(cadena: str) -> dict[str, int]:
    """Cuenta cuántas veces aparece cada carácter de una cadena.

    Args:
        cadena: Cadena de caracteres que se analizará.
    """
    frecuencias: dict[str, int] = {}

    for caracter in cadena:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1

    return frecuencias


def main() -> None:
    """Ejecuta ejemplos de frecuencia de caracteres."""
    print(frecuencia_caracteres("banana"))
    print(frecuencia_caracteres("Hola mundo"))
    print(frecuencia_caracteres(""))
    print(frecuencia_caracteres("aaaBBB"))


if __name__ == "__main__":
    main()
