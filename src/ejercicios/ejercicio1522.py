"""Programa que crea un diccionario con los nombres de ciudades y
sus poblaciones. Muestra la población de una ciudad, agrega una
nueva ciudad, elimina otra y modifica las poblaciones existentes."""

ciudades = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

print("a. Habitantes de Pergamino:", ciudades["Pergamino"])

ciudades["Lincoln"] = 42036

del ciudades["Junín"]

ciudades["Rojas"] += 1000

ciudades["Pergamino"] = 91399

print("\nDiccionario actualizado:")

for ciudad, poblacion in ciudades.items():
    print("Ciudad:", ciudad, "- Población:", poblacion)
