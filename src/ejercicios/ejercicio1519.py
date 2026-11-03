"""Secuencia iterativa de numeros y analisis de digitos"""

suma_total = 0
cantidad = 0
mayores = 0
continuar = True

while continuar:
    n = int(input("Ingresá un número entero: "))
    texto = str(abs(n))

    suma_rep = 0
    cant_rep = 0
    for d in texto:
        if texto.count(d) > 1:   
            suma_rep += int(d)
            cant_rep += 1

    print("Suma de dígitos repetidos:", suma_rep)
    print("Cantidad de dígitos repetidos:", cant_rep)

    cantidad += 1
    suma_total += n
    if n > 478:
        mayores += 1

    if cant_rep == 0:   
        continuar = False

print(f"Porcentaje de números mayores que 478: {mayores / cantidad * 100:.2f}%")
print(f"Promedio: {suma_total / cantidad:.2f}")