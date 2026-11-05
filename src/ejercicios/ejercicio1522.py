""" Gestion de poblacion de ciudades con Diccionarios """

ciudades = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

ciudades["Lincoln"] = 42036
del ciudades["Junín"]
ciudades["Rojas"] += 1000
ciudades["Pergamino"] = 91399

print("Habitantes de Pergamino:", ciudades["Pergamino"])
print(ciudades)
