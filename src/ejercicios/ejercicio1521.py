texto = ""
linea = input("ingrese una línea: ")

while not linea.endswith("*"):
    texto += linea + " "
    linea = input("ingrese una línea: ")

texto += linea[:-1]

# a) Palabras con al menos 3 vocales diferentes
vocales = "aeiou"
vocales_acentuadas = "áéíóú"
palabras = texto.split()
palabras_validas = []

for palabra in palabras:
    palabra = palabra.lower()

    for vocal in vocales_acentuadas:
        palabra = palabra.replace(vocal, vocales["áéíóú".index(vocal)])

    diferentes = []

    for letra in palabra:
        if letra in vocales and letra not in diferentes:
            diferentes.append(letra)

    if len(diferentes) >= 3:
        palabras_validas.append(palabra)

print("palabras con al menos 3 vocales diferentes:", palabras_validas)

oraciones = texto.count(".")
print("Cantidad de oraciones:", oraciones)

lista_oraciones = texto.split(".")
oraciones_largas = 0

for oracion in lista_oraciones:
    if len(oracion.split()) > 5:
        oraciones_largas += 1

if oraciones > 0:
    porcentaje = oraciones_largas * 100 / oraciones
    print("porcentaje de oraciones con más de cinco palabras:", porcentaje)
else:
    print("no hay oraciones para calcular el porcentaje")