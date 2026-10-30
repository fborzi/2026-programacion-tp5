"""Programa que crea un conjunto de números enteros, agrega nuevos
elementos sin repetirlos y muestra el menor y el mayor número,
verifica si determinados números pertenecen al conjunto y cuenta
la cantidad total de elementos."""

numeros = set(range(1, 11))

numeros.add(11)
numeros.add(12)

numeros.update(range(30, 36))

numeros.add(232)
numeros.add(-264)


print("Primer numero:", min(numeros))
print("Ultimo numero:", max(numeros))


print("¿El 7 pertenece?", 7 in numeros)
print("¿El 20 pertenece?", 20 in numeros)

print("Cantidad de elementos:", len(numeros))
