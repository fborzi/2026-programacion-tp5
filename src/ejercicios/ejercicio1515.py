"""Ejercicio  1515 gestión de ciudades y personas con listas anidadas
Usa las Funciones obtenerCiudad, obtenerProvincia y contarPoblacion. solo es 
un ejemplo de uso, para probar las funciones.
"""

from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

ciudades: list = [
    ["Rosario", "Santa Fe"],
    ["Carlos Paz", "Córdoba"],
    ["Balcarce", "Buenos Aires"],
    ["Cosquín", "Córdoba"]
]
personas: list = [
    ["Juan Perez", 26782345, "Carlos Paz"],
    ["María Gomez", 40173542, "Rosario"],
    ["Ana Ríos", 9216378, "Cosquín"]
]

print(obtenerCiudad(personas, 40173542))
print(obtenerProvincia(personas, ciudades, 40173542))
print(contarPoblacion(personas, ciudades, "Córdoba"))
