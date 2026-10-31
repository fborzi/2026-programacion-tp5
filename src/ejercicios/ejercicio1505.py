"""Programa que genera una nueva lista a partir de una lista
de nombres, convirtiendo todos sus elementos a mayúsculas."""

nombres = ["ana", "juan", "maria", "pedro", "laura"]

nombres_mayusculas = []

for nombre in nombres:
    nombres_mayusculas.append(nombre.upper())

print("Lista original:", nombres)
print("Lista en mayusculas:", nombres_mayusculas)
