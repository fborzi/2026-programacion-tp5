numero = int(input("Ingrese un numero entero: "))

cantidad = 0
mayores = 0
suma_numeros = 0

texto = str(abs(numero))
repetidos = []

for digito in texto:
    if texto.count(digito) > 1 and digito not in repetidos:
        repetidos.append(digito)

while len(repetidos) > 0:
    suma_digitos = 0

    for digito in repetidos:
        suma_digitos = suma_digitos + int(digito)

    print("Suma de digitos repetidos:", suma_digitos)
    print("Cantidad de digitos repetidos:", len(repetidos))

    cantidad += 1
    suma_numeros += numero

    if numero > 478:
        mayores += 1
    numero  = int(input("Ingrese otro numero: "))
    texto = str(abs(numero))
    repetidos = []

    for digito in texto:
        if texto.count(digito) > 1 and digito not in repetidos:
            repetidos.append(digito)
print("Cantidad de numeros procesados:", cantidad)
if cantidad > 0:
    porcentaje = mayores * 100 / cantidad
    promedio = suma_numeros / cantidad

    print("Porcentaje de numeros mayores a 478:", porcentaje, "%")
    print("Promedio de los numeros procesados:", promedio)
else:
    print("No se procesaron numeros.")