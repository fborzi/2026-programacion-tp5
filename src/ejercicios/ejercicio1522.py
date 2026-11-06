ciudades = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

# Pergamino
print("Habitantes de Pergamino:", ciudades["Pergamino"])

#Agregar Lincoln
ciudades["Lincoln"] = 42036
print("Agregada Lincoln:", ciudades)

#Eliminar Junín
del ciudades["Junín"]
print("Eliminada Junín:", ciudades)

#Incrementar habitantes de Rojas en 1000
ciudades["Rojas"] += 1000
print("Rojas incrementada:", ciudades)

# Modificar Pergamino a 91399
ciudades["Pergamino"] = 91399
print("Pergamino actualizado:", ciudades)

#resultado final
print("\nDiccionario final:", ciudades)
