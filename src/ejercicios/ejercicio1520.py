from funciones import letras_repetidas

texto = input("Ingresa un texto: ")
palabras = texto.split()

print("Cantidad de palabras:", len(palabras))

for palabra in palabras:
    repetidas = letras_repetidas(palabra)
    if len(repetidas) > 0:
        print("Letras repetidas en", palabra, ":", repetidas)
