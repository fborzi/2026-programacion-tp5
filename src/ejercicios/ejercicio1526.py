paises = {}
total = 0

ciudad = input("Ingrese una ciudad (zz para terminar): ")

while ciudad != "zz":
    pais = input("Ingrese el país: ")

    total = total + 1

    if pais in paises:
        paises[pais] = paises[pais] + 1
    else:
        paises[pais] = 1

    ciudad = input("Ingrese una ciudad (zz para terminar): ")

print("Total de ciudades:", total)
print("Cantidad de ciudades por país:")

for pais in paises:
    print(pais, paises[pais])