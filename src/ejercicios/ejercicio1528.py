peliculas = {}

titulo = input("Ingrese título de la película (zz para terminar): ")
while titulo.lower() != "zz":
    director = input("Director: ")
    anio = int(input("Año de estreno: "))
    actores = input("Actores principales (separados por coma): ").split(",")

    peliculas[titulo] = {
        "director": director,
        "anio": anio,
        "actores": [a.strip() for a in actores]
    }

    titulo = input("Ingrese título de la película (zz para terminar): ")

# películas por director
pelis_por_director = {}
for datos in peliculas.values():
    d = datos["director"]
    pelis_por_director[d] = pelis_por_director.get(d, 0) + 1

print("Películas por director:", pelis_por_director)

#Director con más películas
director_top = max(pelis_por_director, key=pelis_por_director.get)
print("Director con más películas:", director_top)

# Actores de una película
titulo_buscar = input("Ingrese título para ver actores: ")
if titulo_buscar in peliculas:
    print("Actores:", peliculas[titulo_buscar]["actores"])
else:
    print("No existe esa película.")

# Películas de un actor
actor_buscar = input("Ingrese nombre de actor: ")
pelis_actor = [t for t, datos in peliculas.items() if actor_buscar in datos["actores"]]

if pelis_actor:
    print("Películas de", actor_buscar, ":", pelis_actor)
else:
    print("Ese actor no figura en la base.")
