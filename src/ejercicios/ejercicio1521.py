linea = input("Ingrese una linea de texto: ")
texto = ""

while linea.endswith("*") == False:
    texto = texto + linea + " "
    linea = input("Ingrese otra linea de texto: ")
texto = texto + linea[:-1]

vocales = "aeiou"
palabras_vocales = []

for palabra in texto.split():
    palabra_minuscula = palabra.lower()

    palabra_minuscula = palabra_minuscula.replace("á", "a")
    palabra_minuscula = palabra_minuscula.replace("é", "e")
    palabra_minuscula = palabra_minuscula.replace("í", "i")
    palabra_minuscula = palabra_minuscula.replace("ó", "o")
    palabra_minuscula = palabra_minuscula.replace("ú", "u")

    contador = 0

    for vocal in vocales:
        if vocal in palabra_minuscula:
            contador += 1

    if contador >= 3:
        palabras_vocales.append(palabra)
print("Palabras con al menos 3 vocales diferentes:")
print(palabras_vocales)

oraciones = texto.split(".")
cantidad_oraciones = 0
oraciones_mas_cinco = 0

for oracion in oraciones:
    palabras = oracion.split()

    if len(palabras) > 0:
        cantidad_oraciones += 1

        if len(palabras) > 5:
            oraciones_mas_cinco += 1
print("Cantidad de oraciones:", cantidad_oraciones)

if cantidad_oraciones > 0:
    porcentaje = oraciones_mas_cinco * 100 / cantidad_oraciones
    print("Porcentaje de oraciones con mas de cinco palabras:", porcentaje, "%")
else:
    print("No se ingresaron oraciones.")