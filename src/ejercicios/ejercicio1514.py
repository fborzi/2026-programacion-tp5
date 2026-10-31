def dos_sumandos(lista, resultado):
    vistos = {}  # valor -> indice

    for i, num in enumerate(lista):
        falta = resultado - num
        if falta in vistos:
            return [vistos[falta], i]
        vistos[num] = i
    
    return [] # si no hay solución

# Ejemplos:
print(dos_sumandos([2, 7, 11, 15], 9))
# -> [0, 1] porque lista[0] + lista[1] = 2 + 7 = 9

print(dos_sumandos([3, 2, 4], 6))
# -> [1, 2] porque 2 + 4 = 6

print(dos_sumandos([3, 3], 6))
# -> [0, 1] usa dos posiciones distintas, no el mismo número dos veces