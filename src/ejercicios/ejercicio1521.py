"""Ejercicio 1521: Procesamiento de oraciones y vocales en un texto.

lee líneas de texto hasta recibir una terminada en '*'. Informa las
palabras con al menos  3 vocales diferentes, la cantidad de oraciones
(cada una termina con '.' ) y el porcentaje de oraciones con más de cinco palabras
"""

from funciones import (
    cantidad_vocales_diferentes,
    contar_oraciones_largas,
    leer_texto,
)

texto: str = leer_texto()
oraciones: list = texto.split(".")[:-1]

for palabra in texto.split():
    if cantidad_vocales_diferentes(palabra) >= 3:
        print(palabra.strip(".,;:"))

print(f"Cantidad de oraciones: {len(oraciones)}")

if len(oraciones) > 0:
    print(f"Porcentaje de oraciones con mas de cinco palabras: "
          f"{contar_oraciones_largas(oraciones) * 100 / len(oraciones)}")
