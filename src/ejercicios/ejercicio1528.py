""" Catalogo de peliculas y actores con acceso directo """

catalogo = {}

titulo = input("Ingrese el título de la película o fin para terminar: ")

while titulo.lower() != "fin":
    director = input(f"Director de '{titulo}': ")
    año = int(input("Año de estreno: "))
    
    # Carga de la lista de actores principales para esta película
    actores = []
    actor = input("Ingrese un actor principal o fin para terminar el listado: ")
    while actor.lower() != "fin":
        actores.append(actor)
        actor = input("Ingrese otro actor principal o fin para terminar: ")
        
    catalogo[titulo] = {
        "director": director,
        "año": año,
        "actores": actores
    }

    titulo = input("Ingrese el título de la siguiente película o fin para terminar: ")

conteo_directores = {}
for info in catalogo.values():
    dir_actual = info["director"]
    if dir_actual in conteo_directores:
        conteo_directores[dir_actual] += 1
    else:
        conteo_directores[dir_actual] = 1

print("\n Películas dirigidas por cada director:")
for dir_actual, cantidad in conteo_directores.items():
    print(f"- {dir_actual}: {cantidad} película(s)")

max_peliculas = -1
director_maximo = ""
for dir_actual, cantidad in conteo_directores.items():
    if cantidad > max_peliculas:
        max_peliculas = cantidad
        director_maximo = dir_actual

print(f"\n El director con más películas es: {director_maximo} ({max_peliculas} películas)")

print("\n Búsqueda de actores por título:")
titulo_buscar = input("Ingrese el título de la película a buscar: ")

if titulo_buscar in catalogo:
    print(f"Los actores principales de '{titulo_buscar}' son:")
    print(*catalogo[titulo_buscar]["actores"], sep=", ")
else:
    print(f"La película '{titulo_buscar}' no se encuentra en el catálogo.")

print("\nd. Búsqueda de películas por actor:")
actor_buscar = input("Ingrese el nombre del actor a buscar: ")
peliculas_participo = []

for tit, info in catalogo.items():
    if actor_buscar in info["actores"]:
        peliculas_participo.append(tit)

if peliculas_participo:
    print(f"El actor '{actor_buscar}' participó en las siguientes películas:")
    print(*peliculas_participo, sep=", ")
else:
    print(f"No se encontraron películas en el catálogo donde participe '{actor_buscar}'.")
