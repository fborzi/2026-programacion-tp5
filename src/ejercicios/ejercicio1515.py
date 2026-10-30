"""Resolución del ejercicio 1515.
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Permite buscar la ciudad de residencia de una persona mediante su DNI, determina la
provincia correspondiente y cuantas personas viven.
"""
from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

ciudades = [
    ["Rosario", "Santa Fe"],
    ["Carlos Paz", "Córdoba"],
    ["Balcarce", "Buenos Aires"],
    ["Cosquín", "Córdoba"],
]

personas = [
    ["Juan Perez", 26782345, "Carlos Paz"],
    ["María Gomez", 40173542, "Rosario"],
    ["Ana Ríos", 9216378, "Cosquín"],
]

dni = input("Ingrese DNI para consultar ciudad y provincia: ").strip()
print("Ciudad:", obtenerCiudad(personas, dni))
print("Provincia:", obtenerProvincia(personas, ciudades, dni))

provincia = input("Ingrese una provincia para contar personas: ").strip()
print("Personas en esa provincia:", contarPoblacion(personas, ciudades, provincia))
