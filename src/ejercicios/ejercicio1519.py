"""Ejercicio 1519: análisis de dígitos repetidos."""


def analizar_digitos(numero: int) -> tuple[int, int]:
    """Calcula suma y cantidad de apariciones de dígitos repetidos.

    Args:
        numero: Número entero que se analizará.
    """
    digitos = str(abs(numero))
    suma = 0
    cantidad = 0

    for digito in digitos:
        if digitos.count(digito) > 1:
            suma += int(digito)
            cantidad += 1

    return suma, cantidad


def main() -> None:
    """Procesa números hasta encontrar uno sin dígitos repetidos."""
    numeros: list[int] = []
    continuar = True

    while continuar:
        numero = int(input("Ingrese un número entero: "))
        suma, cantidad = analizar_digitos(numero)

        numeros.append(numero)

        print("Suma de dígitos repetidos:", suma)
        print("Cantidad de dígitos repetidos:", cantidad)

        if cantidad == 0:
            continuar = False

    mayores = sum(numero > 478 for numero in numeros)
    porcentaje = mayores * 100 / len(numeros)
    promedio = sum(numeros) / len(numeros)

    print("Porcentaje de números mayores a 478:", porcentaje)
    print("Promedio de números procesados:", promedio)


if __name__ == "__main__":
    main()
