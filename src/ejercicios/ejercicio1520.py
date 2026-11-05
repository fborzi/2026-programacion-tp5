""" Analisis de palabras y letras repetidas en un texto """

texto = input("Ingrese un texto: ")

palabras = texto.split(" ")

print(f"Hay {len(palabras)} palabras en total.")

for palabra in palabras:
    
    palabra_limpia = palabra.lower()
    
    letras_de_palabra = ""
    for caracter in palabra_limpia:
        if caracter.isalpha():
            letras_de_palabra += caracter
            
    repetidas = []
    for letra in letras_de_palabra:
        if letras_de_palabra.count(letra) > 1 and letra not in repetidas:
            repetidas.append(letra)
            
    if repetidas:
        letras_formateadas = ", ".join(f'"{l}"' for l in repetidas)
        print(f'Las letras repetidas en "{letras_de_palabra}" son la/s {letras_formateadas}.')
    else:
        print(f'En "{letras_de_palabra}" no se repite ninguna letra.')
