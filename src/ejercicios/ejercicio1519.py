procesados = []

while True:
    num_str = input("Ingresá un número entero: ").strip()
    if not num_str.lstrip('-').isdigit():
        continue

    digitos = [d for d in num_str if d.isdigit()]
    if len(digitos) == len(set(digitos)):
        break

    num = int(num_str)
    procesados.append(num)

    repetidos = set([d for d in digitos if digitos.count(d) > 1])
    suma_rep = sum(int(d) * digitos.count(d) for d in repetidos)
    cant_rep = sum(digitos.count(d) for d in repetidos)

    print(f"a. Suma de dígitos que se repiten: {suma_rep}")
    print(f"b. Cantidad de dígitos que se repiten: {cant_rep}")

if procesados:
    mayores_478 = sum(1 for x in procesados if x > 478)
    porcentaje = (mayores_478 / len(procesados)) * 100
    promedio = sum(procesados) / len(procesados)
    print(f"c. Porcentaje de números mayores que 478: {porcentaje:.2f}%")
    print(f"d. Promedio de los números procesados: {promedio:.2f}")
else:
    print("No se procesaron números repetidos.")