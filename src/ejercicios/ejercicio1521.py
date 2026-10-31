
"""Solicita un texto de una o más líneas hasta ingresar una línea
terminada en '*'.

Informa las palabras con al menos tres vocales diferentes,
la cantidad de oraciones y el porcentaje de oraciones
que tienen más de cinco palabras."""


from funciones import analizar_texto

texto = ""

while True:
    linea = input("Ingresá una línea de texto (* para finalizar): ")

    if linea.rstrip().endswith("*"):
        texto += linea.rstrip()[:-1]
        break

    texto += linea + "\n"

palabras, cantidad_oraciones, porcentaje = analizar_texto(texto)

print("Palabras con al menos 3 vocales diferentes:", palabras)
print("Cantidad de oraciones:", cantidad_oraciones)
print("Porcentaje de oraciones con más de 5 palabras:", porcentaje, "%")
