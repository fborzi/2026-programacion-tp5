entrada = input("Ingrese números separados por espacio: ")

numeros = [int(x) for x in entrada.split()]

resultado = minimo_elemento(numeros)
print("El mínimo es:", resultado)
