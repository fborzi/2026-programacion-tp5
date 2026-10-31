# Datos iniciales
poblacion = {
    "Junin": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

# a. Informar la cantidad de habitantes que tiene Pergamino
print(f"Pergamino tiene {poblacion['Pergamino']} habitantes")
# también podés usar: poblacion.get("Pergamino")

# b. Agregar a Lincoln con 42.036 habitantes
poblacion["Lincoln"] = 42036

# c. Eliminar a Junin
del poblacion["Junin"]
# o: poblacion.pop("Junin")

# d. Incrementar los habitantes de Rojas en 1.000
poblacion["Rojas"] += 1000

# e. Modificar la cantidad de habitantes de Pergamino por 91.399
poblacion["Pergamino"] = 91399

print(poblacion)
# Resultado final: {'Rojas': 29654, 'Pergamino': 91399, 'Lincoln': 42036}