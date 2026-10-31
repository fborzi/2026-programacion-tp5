def comprimir_rle(texto):
    if not texto:
        return []

    comprimida = []
    caracter_actual = texto[0]
    contador = 1

    for c in texto[1:]:
        if c == caracter_actual:
            contador += 1
        else:
            comprimida.append((caracter_actual, contador))
            caracter_actual = c
            contador = 1
    
    # agregar el último grupo
    comprimida.append((caracter_actual, contador))
    return comprimida

def descomprimir_rle(lista_comprimida):
    texto = ""
    for caracter, cantidad in lista_comprimida:
        texto += caracter * cantidad
    return texto

def tasa_compresion(texto_original, lista_comprimida):
    if len(texto_original) == 0:
        return 0, False
    
    tasa = (1 - len(lista_comprimida) / len(texto_original)) * 100
    efectiva = len(lista_comprimida) < len(texto_original)
    return tasa, efectiva

# --- Prueba del enunciado ---
texto = "aaabbbbaac"
comprimido = comprimir_rle(texto)
print(comprimido)  # [('a', 3), ('b', 4), ('a', 2), ('c', 1)]

original = descomprimir_rle(comprimido)
print(original)  # aaabbbbaac

tasa, es_efectiva = tasa_compresion(texto, comprimido)
print(f"Tasa: {tasa:.2f}% - ¿Efectiva?: {es_efectiva}")
# Tasa: 60.0% - ¿Efectiva?: True -> pasó de 10 caracteres a 4 tuplas