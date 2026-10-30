"""
Importamos la funcion que convierte nombres a mayusculas.
"""

from funciones import cargar_nombres, convertir_mayusculas

nombres = cargar_nombres()
nombres_convertidos = convertir_mayusculas(nombres)

print("Nombres en mayusculas: ")

for nombre in nombres_convertidos:
    print(nombre)
    