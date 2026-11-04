"""Ejercicio 1522: gestión de población de ciudades con diccionarios
Almacena los habitantes de cada ciudad en un diccionario con el nombre
de la ciudad como clave, informa los habitantes de Pergamino, agrega
Lincoln, elimina Junín, incrementa Rojas y modifica Pergamino.
"""

habitantes: dict = {"Junín": 102023, "Rojas": 28654, "Pergamino": 80569}

print(habitantes["Pergamino"])

habitantes["Lincoln"] = 42036

del habitantes["Junín"]

habitantes["Rojas"] += 1000

habitantes["Pergamino"] = 91399
