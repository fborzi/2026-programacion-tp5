"""Ejercicio 1528: catálogo de películas y actores con acceso directo, carga
las películas en un diccionario con el título como clave.
Informa cuántas películas dirigió cada director y cuál dirigió más,
lista los actores de un título ingresado y los títulos en los que
participó un actor ingresado.
"""

from funciones import (
    cargar_peliculas,
    director_con_mas_peliculas,
    peliculas_de_actor,
    peliculas_por_director,
)

peliculas: dict = cargar_peliculas()

print(peliculas_por_director(peliculas))

print(director_con_mas_peliculas(peliculas))

titulo: str = input("Ingrese un titulo: ")
if titulo in peliculas:
    for actor in peliculas[titulo][2]:
        print(actor)
else:
    print("No existe una pelicula con ese titulo")

actor_buscado: str = input("Ingrese un actor: ")
for titulo_actor in peliculas_de_actor(peliculas, actor_buscado):
    print(titulo_actor)
