texto = "aaabbbbaac"

comprimido = comprimir_rle(texto)

print("Comprimido:", comprimido)
print("Descomprimido:", descomprimir_rle(comprimido))
print("Tasa:", tasa_compresion(texto, comprimido))