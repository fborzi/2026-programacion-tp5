# Ejercicio 1516: operaciones basicas con conjuntos numericos.

"""este archivo crea un conjunto de numeros,
obtiene el primero y el ultimo, verifica pertenencia
y muestra la cantidad de elemento"""

numeros = set(range(1, 11))

numeros.update({11, 12})

numeros.update(range(30, 36))

numeros.update({232, 264})

ordenados = sorted(numeros)

print("Primer numero:", ordenados[0] if ordenados else None)

print("ultimo numero:", ordenados[-1] if ordenados else None)

print("¿esta el 7?:", 7 in numeros)

print("¿esta el 20?:", 20 in numeros)

print("Cantidad de elementos:", len(numeros))

