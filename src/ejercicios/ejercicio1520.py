"""Programa que cuenta la cantidad de palabras de un texto y busca,
en cada palabra, las letras que se repiten sin distinguir entre
mayúsculas y minúsculas, ignorando números y símbolos."""

texto = input("Ingresá un texto: ")

palabras = texto.split()

print("Cantidad de palabras:", len(palabras))

for palabra in palabras:
    palabra = palabra.lower()
    vistos = []
    repetidas = []

    for letra in palabra:
        if letra.isalpha():
            if letra in vistos and letra not in repetidas:
                repetidas.append(letra)
            vistos.append(letra)

    if repetidas:
        print("En", palabra, "se repiten:", repetidas)
    else:
        print("En", palabra, "no hay letras repetidas")
