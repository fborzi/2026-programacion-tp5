poblacion_ciudades = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

print("--- Estado Inicial ---")
print(poblacion_ciudades)
print("-" * 30)

print(f"a. La cantidad de habitantes que tiene Pergamino es: {poblacion_ciudades['Pergamino']}")

poblacion_ciudades["Lincoln"] = 42036
print(f"b. Se agregó a Lincoln con {poblacion_ciudades['Lincoln']} habitantes.")

del poblacion_ciudades["Junín"]
print("c. Se ha eliminado a Junín del diccionario.")

poblacion_ciudades["Rojas"] += 1000
print(f"d. Habitantes de Rojas incrementados. Nuevo total: {poblacion_ciudades['Rojas']}")

poblacion_ciudades["Pergamino"] = 91399
print(f"e. Habitantes de Pergamino modificados. Nuevo total: {poblacion_ciudades['Pergamino']}")

print("-" * 30)
print("--- Estado Final del Diccionario ---")
print(poblacion_ciudades)