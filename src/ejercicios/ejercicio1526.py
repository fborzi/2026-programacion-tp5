ciudades_por_pais = {}
total_ciudades = 0

ciudad = input("Ingrese ciudad (zz para terminar): ")
while ciudad.lower() != "zz":
    pais = input("Ingrese país: ")
    total_ciudades += 1

    # Incrementar contador de ciudades por país
    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1

    ciudad = input("Ingrese ciudad (zz para terminar): ")

print("Cantidad total de ciudades:", total_ciudades)
print("Cantidad de ciudades por país:", ciudades_por_pais)


lista_ciudades = []

ciudad = input("Ingrese ciudad (zz para terminar): ")
while ciudad.lower() != "zz":
    pais = input("Ingrese país: ")
    lista_ciudades.append([ciudad, pais])
    ciudad = input("Ingrese ciudad (zz para terminar): ")


ciudades_por_pais = {}
for ciudad, pais in lista_ciudades:
    if pais in ciudades_por_pais:
        ciudades_por_pais[pais] += 1
    else:
        ciudades_por_pais[pais] = 1

print("Cantidad total de ciudades:", len(lista_ciudades))
print("Cantidad de ciudades por país:", ciudades_por_pais)
