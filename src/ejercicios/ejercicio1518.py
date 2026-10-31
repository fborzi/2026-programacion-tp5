def digitos_repetidos(n):
    texto = str(abs(n)) # abs por si n es negativo
    vistos = set()
    repetidos = set()
    
    for digito in texto:
        if digito in vistos:
            repetidos.add(int(digito))
        else:
            vistos.add(digito)
            
    return list(repetidos)

# Ejemplos:
print(digitos_repetidos(1223455331))
# -> [2, 3, 1]  (el orden puede variar porque es set)

print(digitos_repetidos(12345))
# -> [] no hay repetidos

print(digitos_repetidos(112233))
# -> [1, 2, 3]

print(digitos_repetidos(1000))
# -> [0]