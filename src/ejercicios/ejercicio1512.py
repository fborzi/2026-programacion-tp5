entrada = input("Ingrese números separados por espacio: ")

numeros = [int(x) for x in entrada.split()]

resultado = sumatoria_digitos(numeros)
print("La suma de dígitos de cada número es:", resultado)
