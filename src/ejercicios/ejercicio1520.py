def letras_repetidas_palabra(palabra):
    # solo letras, ignorando mayúsculas
    letras = [c.lower() for c in palabra if c.isalpha()]
    
    vistos = set()
    repetidas = set()
    
    for letra in letras:
        if letra in vistos:
            repetidas.add(letra)
        else:
            vistos.add(letra)
            
    return sorted(repetidas)

texto = input("Ingresá un texto: ")

# A - cantidad de palabras separadas por espacios
# split() sin argumentos ignora espacios de más
palabras = texto.split()
print(f"\nHay {len(palabras)} palabras en total")

# B - para cada palabra, letras que se repiten
for p in palabras:
    rep = letras_repetidas_palabra(p)
    # sacamos los puntos/comas del final solo para mostrar lindo
    palabra_limpia = p.strip(".,;:!¡?¿\"'()")
    
    if rep:
        letras_str = ", ".join([f"'{l}'" for l in rep])
        print(f"En '{palabra_limpia}' las letras repetidas son: {letras_str}")
    else:
        print(f"En '{palabra_limpia}' no hay letras repetidas")