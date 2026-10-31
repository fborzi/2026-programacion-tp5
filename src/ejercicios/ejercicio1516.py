# 1. conjunto con los números del uno al diez
numeros = set(range(1, 11))
print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 2. luego añadi el once y el doce
numeros.add(11)
numeros.add(12)

# 3. actualiza incorporando del 30 al 35 sin agregar de a uno
numeros.update(range(30, 36)) # update agrega todo un iterable de golpe
print(numeros)

# 4. finalmente agrega los numeros 232 y 264
numeros.update([232, 264])

# 5. informa de ser posible el primero y el ultimo numero almacenado
# Como el set es desordenado, lo ordenamos para mostrarlo
ordenados = sorted(numeros)
print(f"Primero (ordenado): {ordenados[0]}")
print(f"Último (ordenado): {ordenados[-1]}")
print(f"Conjunto ordenado: {ordenados}")

# 6. informa si el 7 y el 20 pertenece al conjunto
print(f"¿El 7 pertenece? {7 in numeros}")
print(f"¿El 20 pertenece? {20 in numeros}")

# 7. informa cuantos elementos hay almacenados
print(f"Cantidad de elementos: {len(numeros)}")