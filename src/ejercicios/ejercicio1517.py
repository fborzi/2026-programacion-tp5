"""Resolución del ejercicio 1517.
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Verifica si dos conjuntos tienen elementos en comun y comprueba la relacions de
subconjunto entre ellos y obtiene la union de todos los conjuntos.
"""

horm1 = {"melanina", "oxitocina", "dopamina"}
horm2 = {"testosterona", "melanina"}
horm3 = {"calcitonina", "estradiol"}

print("¿horm1 y horm2 comparten alguna hormona?:", bool(horm1 & horm2))
print("¿horm1 y horm3 comparten alguna hormona?:", bool(horm1 & horm3))
print("¿horm2 es subconjunto de horm1?:", horm2.issubset(horm1))
print("Conjunto de todas las hormonas:", horm1 | horm2 | horm3)