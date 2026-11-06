def frecuencia_caracteres(cadena):
    frecuencias = {}
    for caracter in cadena:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias

texto = input("Ingresá un texto: ")
print(frecuencia_caracteres(texto))
