#ejercicio 1526 conteo y agrupacion de ciudades por pais
"""Resolucion del ejercicio 1526 a.

Este archivo importa las funciones necesarias desde funciones py cuando corresponde,
utiliza los datos de la consigna y muestra los resultados solicitados.
No se redefinen aquí las funciones compartidas.
"""

from funciones import cargar_ciudades_por_pais

total, por_pais, _ = cargar_ciudades_por_pais(guardar_lista=False)
print("Cantidad total de ciudades:", total)
print("Ciudades por país:", por_pais)

"""Resolucion del ejercicio 1526 b.

Este archivo importa las funciones necesarias desde funciones py cuando corresponde,
utiliza los datos de la consigna y muestra los resultados solicitados.
No se redefinen aquí las funciones compartidas.
"""

from funciones import cargar_ciudades_por_pais

total, por_pais, ciudades = cargar_ciudades_por_pais(guardar_lista=True)
print("Lista de ciudades y paises:", ciudades)
print("Cantidad total de ciudades:", total)
print("Ciudades por pais:", por_pais)

