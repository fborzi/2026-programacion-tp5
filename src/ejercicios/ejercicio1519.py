"""Ejercicio 1519: secuencia interactiva de números y análisis de dígitos.

Lee números enteros hasta recibir uno sin dígitos repetidos. Para cada
número procesado informa la suma y la cantidad de sus dígitos
repetidos, y al finalizar informa el porcentaje de números mayores
que 478 y el promedio de los números procesados. El número sin
dígitos repetidos que corta la lectura no se procesa.
"""

from funciones import digitos_repetidos

cantidad: int = 0
mayores: int = 0
suma_numeros: int = 0
numero: int = int(input("Ingrese un numero: "))
repetidos: list = digitos_repetidos(numero)

while repetidos != []:
    print(f"Suma de los digitos repetidos: {sum(repetidos)}")
    print(f"Cantidad de digitos repetidos: {len(repetidos)}")
    cantidad += 1
    suma_numeros += numero
    if numero > 478:
        mayores += 1
    numero = int(input("Ingrese un numero: "))
    repetidos = digitos_repetidos(numero)

if cantidad > 0:
    print(f"Porcentaje de numeros mayores que 478: {mayores * 100 / cantidad}")
    print(f"Promedio de los numeros procesados: {suma_numeros / cantidad}")
else:
    print("No se procesaron numeros")
