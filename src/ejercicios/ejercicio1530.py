from funciones import descomprimir_rle, comprimir_rle, tasa_compresion


texto_ejemplo = "aaabbbbaac"

resultado_compresion = comprimir_rle(texto_ejemplo)
print("Lista comprimida:", resultado_compresion)

resultado_descompresion = descomprimir_rle(resultado_compresion)
print("Texto reconstruido:", resultado_descompresion)

porcentaje, es_efectiva = tasa_compresion(texto_ejemplo, resultado_compresion)
print(f"Tasa de reducción: {porcentaje:.2f}% | ¿Fue efectiva?: {es_efectiva}")
