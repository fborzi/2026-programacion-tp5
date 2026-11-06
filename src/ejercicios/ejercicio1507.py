def dos_minimos(lista):
    ordenada = sorted(lista)

    if len(ordenada) == 0:
        return (None, None)
    elif len(ordenada) == 1:
        return (ordenada[0], None)
    else:
        return (ordenada[0], ordenada[1])

elementos = []
print("Ingresá los elementos uno a uno (presioná Enter en blanco para finalizar):")
while True:
    entrada = input()
    if entrada == "":
        break
    try:
        if "." in entrada:
            val = float(entrada)
        else:
            val = int(entrada)
    except ValueError:
        val = entrada
    elementos.append(val)

print("Resultado:", dos_minimos(elementos))
