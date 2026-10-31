numeros = set(range(1, 11))

numeros.add(11)
numeros.add(12)

numeros.update(range(30, 36))

numeros.update([232, -264])

print("Menor número:", min(numeros))
print("Mayor número:", max(numeros))

print("¿El 7 pertenece?", 7 in numeros)
print("¿El 20 pertenece?", 20 in numeros)

print("Cantidad de elementos:", len(numeros))