"""Programa que solicita números enteros hasta ingresar uno cuyos
dígitos no se repitan. Para cada número informa la suma y la cantidad
de dígitos repetidos. Al finalizar, calcula el porcentaje de números
mayores que 478 y el promedio de los números procesados."""


from funciones import analizar_digitos

cantidad_numeros = 0
cantidad_mayores = 0
suma_numeros = 0

while True:
    numero = int(input("Ingresá un número entero: "))

    suma, cantidad, tiene_repetidos = analizar_digitos(numero)

    print("Suma de los dígitos repetidos:", suma)
    print("Cantidad de dígitos repetidos:", cantidad)

    cantidad_numeros += 1
    suma_numeros += numero

    if numero > 478:
        cantidad_mayores += 1

    if not tiene_repetidos:
        break

porcentaje = cantidad_mayores * 100 / cantidad_numeros
promedio = suma_numeros / cantidad_numeros

print("Porcentaje de números mayores que 478:", porcentaje, "%")
print("Promedio de los números procesados:", promedio)
