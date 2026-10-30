"""Resolución del ejercicio 1519.
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Para cada numero calcula la suma y la cantidad de digitos repetidos. Determina el
porcentaje y al finalizar el ingreso calcula el promedio de los numeros procesados.
"""
from funciones import digitos_repetidos

def procesar_numeros(cantidad=0, mayores=0, suma_total=0):
    """Solicita y procesa números de manera recursiva.
    Returns:
        tuple: Cantidad procesada, cantidad mayor que 478 y suma total.
    """
    numero = int(input("Ingrese un entero (sin dígitos repetidos para terminar): "))
    repetidos = digitos_repetidos(numero)

    if not repetidos:
        return cantidad, mayores, suma_total
    print("Suma de los dígitos repetidos:", sum(repetidos))
    print("Cantidad de dígitos distintos que se repiten:", len(repetidos))

    return procesar_numeros(
        cantidad + 1,
        mayores + (1 if numero > 478 else 0),
        suma_total + numero
    )

cantidad, mayores, suma_total = procesar_numeros()
porcentaje = mayores / cantidad * 100 if cantidad else 0
promedio = suma_total / cantidad if cantidad else 0

print("Porcentaje de números procesados mayores que 478:", round(porcentaje, 2), "%")
print("Promedio de los números procesados:", round(promedio, 2))
