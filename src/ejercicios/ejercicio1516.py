numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numeros.add(11)
numeros.add(12)

numeros.update(range(30, 36)) 

numeros.update([232, -264])

print("--- Resultados de los incisos ---")

numeros_ordenados = sorted(list(numeros))
print(f"a. Primer número (ordenado): {numeros_ordenados[0]}")
print(f"a. Último número (ordenado): {numeros_ordenados[-1]}")

print(f"b. ¿El 7 pertenece al conjunto?: {7 in numeros}")
print(f"b. ¿El 20 pertenece al conjunto?: {20 in numeros}")

print(f"c. Cantidad de elementos almacenados: {len(numeros)}")