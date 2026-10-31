ciudades = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

print("Habitantes de Pergamino:", ciudades["Pergamino"])

ciudades["Lincoln"] = 42036

del ciudades["Junín"]

ciudades["Rojas"] = ciudades["Rojas"] + 1000

ciudades["Pergamino"] = 91399

print(ciudades)