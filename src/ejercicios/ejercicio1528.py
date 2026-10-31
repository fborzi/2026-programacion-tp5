peliculas = {}

titulo = input("Ingrese el título de la película (fin para terminar): ")

while titulo != "fin":
    director = input("Ingrese el director: ")
    anio = int(input("Ingrese el año de estreno: "))

    actores = []
    actor = input("Ingrese un actor (fin para terminar): ")

    while actor != "fin":
        actores.append(actor)
        actor = input("Ingrese otro actor (fin para terminar): ")

    peliculas[titulo] = {
        "director": director,
        "anio": anio,
        "actores": actores
    }

    titulo = input("Ingrese el título de otra película (fin para terminar): ")


directores = {}

for titulo in peliculas:
    director = peliculas[titulo]["director"]

    if director in directores:
        directores[director] = directores[director] + 1
    else:
        directores[director] = 1

print("Películas dirigidas por cada director:")

for director in directores:
    print(director, directores[director])


if len(directores) > 0:
    director_mayor = max(directores, key=directores.get)
    print("Director con más películas:", director_mayor)


buscar_titulo = input("Ingrese el título de una película: ")

if buscar_titulo in peliculas:
    print("Actores principales:")
    for actor in peliculas[buscar_titulo]["actores"]:
        print(actor)
else:
    print("La película no existe")

buscar_actor = input("Ingrese el nombre del actor: ")

encontradas = []

for titulo in peliculas:
    if buscar_actor in peliculas[titulo]["actores"]:
        encontradas.append(titulo)

if len(encontradas) > 0:
    print("Películas en las que participó:", buscar_actor)
    for titulo in encontradas:
        print(titulo)
else:
    print("No se encontraron películas de ese actor")