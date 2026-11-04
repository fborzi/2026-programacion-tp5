"""Ejercicio 1526: conteo y agrupación de ciudades por país.

Resuelve el conteo de ciudades total y por país en dos versiones: en
la versión a las ciudades no se almacenan a medida que se ingresan, y
en la versión b se almacenan en una lista que luego se procesa.
"""

from funciones import (
    cargar_ciudades,
    contar_ciudades_sin_almacenar,
    contar_por_pais,
)

print("Version a")
resultado: tuple = contar_ciudades_sin_almacenar()
print(f"Cantidad total de ciudades: {resultado[0]}")
print(resultado[1])

print("Version b")
ciudades: list = cargar_ciudades()
print(f"Cantidad total de ciudades: {len(ciudades)}")
print(contar_por_pais(ciudades))
