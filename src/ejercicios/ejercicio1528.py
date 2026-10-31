"""ejercicio 1528.
este codigo permite administrar peliculas, incluyendo carga, busqueda, actualizacion y 
eliminacion de peliculas.
"""

def cargar_peliculas(peliculas):
    titulo = input("Titulo (vacio para terminar): ").strip()
    if not titulo:
        return
    director = input("Director: ").strip()
    anio = int(input("Año de estreno: "))
    actores = [a.strip() for a in input("Actores principales separados por coma: ").split(",") if a.strip()]
    peliculas[titulo] = {"director": director, "anio": anio, "actores": actores}
    cargar_peliculas(peliculas)

peliculas = {}
cargar_peliculas(peliculas)

por_director = {}
for pelicula in peliculas.values():
    director = pelicula["director"]
    por_director[director] = por_director.get(director, 0) + 1
print("Películas dirigidas por cada director:", por_director)
print("Director con más películas:",
      max(por_director.items(), key=lambda item: item[1], default=None))

titulo = input("Titulo para consultar actores: ").strip()
print("Actores principales:", peliculas[titulo]["actores"] if titulo in peliculas else "No existe")

actor = input("Nombre de actor para buscar peliculas: ").strip().lower()
titulos = [titulo for titulo, datos in peliculas.items()
           if any(nombre.lower() == actor for nombre in datos["actores"])]
print("Peliculas en las que participo:", titulos)
