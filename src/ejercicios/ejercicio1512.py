def sumatoria_digitos(lista):
    resultado = []
    for num in lista:
        suma = 0
        for digito in str(num):
            suma += int(digito)
        resultado.append(suma)
    return resultado

# Ejemplos:
print(sumatoria_digitos([123, 45, 9, 1000]))
# -> [6, 9, 9, 1]

print(sumatoria_digitos([10, 99, 101]))
# -> [1, 18, 2]