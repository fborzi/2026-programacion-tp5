# ejercicio 1520 analisis de palabras y letras repetidas en un texto
"""Este codigo analiza un texto ingresado por el usuario, cuenta la cantidad de palabras y
muestra las letras que se repiten en cada palabra."""

from funciones import letras_repetidas
texto = input("Ingrese un texto: ")

palabras = texto.split()

print("Cantidad de palabras:", len(palabras))

for palabra in palabras:
   
    repetidas = letras_repetidas(palabra)

    
    if repetidas:
        print(f"{palabra}: letras repetidas {repetidas}")


