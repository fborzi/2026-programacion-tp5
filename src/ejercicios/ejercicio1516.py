numeros = set(range(1, 11))

numeros.add(11)
numeros.add(12)

numeros.update(range(30, 36))

numeros.add(232)
numeros.add(-264)

# a. Los conjuntos no tienen orden, asi que no existe un primer ni un ultimo elemento
print("No se puede informar el primero y el ultimo: los conjuntos no tienen orden")

# b.
print("El 7 pertenece al conjunto:", 7 in numeros)
print("El 20 pertenece al conjunto:", 20 in numeros)

# c.
print("Cantidad de elementos:", len(numeros))
