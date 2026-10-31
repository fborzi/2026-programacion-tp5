cantidad_numeros = 0
suma_numeros = 0
mayores_478 = 0

numero = int(input("ingrese un número: "))
repetidos = [1]

while len(repetidos) != 0:
    digitos = str(abs(numero))
    repetidos = []

    for digito in digitos:
        if digitos.count(digito) > 1 and digito not in repetidos:
            repetidos.append(digito)

    suma_repetidos = 0
    cantidad_repetidos = 0

    for digito in repetidos:
        suma_repetidos += int(digito) * digitos.count(digito)
        cantidad_repetidos += digitos.count(digito)

    print("suma de los dígitos repetidos:", suma_repetidos)
    print("cantidad de dígitos repetidos:", cantidad_repetidos)

    cantidad_numeros += 1
    suma_numeros += numero

    if numero > 478:
        mayores_478 += 1

    if len(repetidos) != 0:
        numero = int(input("Ingrese otro número: "))

print("porcentaje de números mayores que 478:", mayores_478 * 100 / cantidad_numeros)
print("promedio de los números procesados:", suma_numeros / cantidad_numeros)