"""Programa que crea un catálogo de películas con sus directores,
años de estreno y actores principales. Cuenta las películas por
director, identifica al director con más películas y muestra los
actores de cada película y las películas en las que participa cada actor."""

peliculas = {}

titulo = input("Ingrese el título (fin para terminar): ")

while titulo.lower() != "fin":
    director = input("Ingrese el director: ")
    anio = int(input("Ingrese el año de estreno: "))

    actores = []
    actor = input("Ingrese un actor (listo para terminar): ")

    while actor.lower() != "listo":
        actores.append(actor)
        actor = input("Ingrese otro actor (listo para terminar): ")

    peliculas[titulo] = {
        "director": director,
        "anio": anio,
        "actores": actores
    }

    titulo = input("Ingrese otra película (fin para terminar): ")


peliculas_por_director = {}

for pelicula in peliculas.values():
    director = pelicula["director"]

    if director in peliculas_por_director:
        peliculas_por_director[director] += 1
    else:
        peliculas_por_director[director] = 1

print("\na. Cantidad de películas por director:")

for director, cantidad in peliculas_por_director.items():
    print(director, ":", cantidad)


if peliculas_por_director:
    director_mayor = max(
        peliculas_por_director,
        key=peliculas_por_director.get
    )
    print("\nb. Director que dirigió más películas:", director_mayor)
    print("Cantidad:", peliculas_por_director[director_mayor])
else:
    print("\nb. No se ingresaron películas.")


print("\nc. Actores principales por película:")

for titulo, pelicula in peliculas.items():
    print("Película:", titulo)

    for actor in pelicula["actores"]:
        print("  -", actor)


print("\nd. Películas por actor:")

peliculas_por_actor = {}

for titulo, pelicula in peliculas.items():
    for actor in pelicula["actores"]:
        if actor in peliculas_por_actor:
            peliculas_por_actor[actor].append(titulo)
        else:
            peliculas_por_actor[actor] = [titulo]

for actor, titulos in peliculas_por_actor.items():
    print("Actor:", actor)

    for titulo in titulos:
        print("  -", titulo)
