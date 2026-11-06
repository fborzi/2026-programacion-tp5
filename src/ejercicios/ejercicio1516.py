numeros = set(range(1, 11)) #cuento del uno al 10

#agrego 11 y 12
numeros.add(11)
numeros.add(12)

#ahora el 30 al 35 sin hacerlo uno por uno
numeros.update(range(30, 36))

#agregar 232 y -264
numeros.update([232, -264])

print("Primer número (mínimo):", min(numeros))
print("Último número (máximo):", max(numeros))

print("¿Está el 7?", 7 in numeros)
print("¿Está el 20?", 20 in numeros)

print("Cantidad de elementos:", len(numeros))
