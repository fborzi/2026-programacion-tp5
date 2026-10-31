"""Programa que solicita nombres de ciudades y sus países,
cuenta cuántas ciudades pertenecen a cada país y muestra
la cantidad total de ciudades registradas por país."""

from funciones import version_a, version_b

opcion = input("¿Qué versión querés ejecutar? (a/b): ")

if opcion == "a":
    version_a()
elif opcion == "b":
    version_b()
else:
    print("Opción incorrecta")
