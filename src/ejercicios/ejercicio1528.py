"""Ejercicio 1528: catálogo de películas y actores con acceso directo."""

from typing import Any

from src.ejercicios.funciones import (
    actores_de_pelicula,
    director_con_mas_peliculas,
    peliculas_de_actor,
    peliculas_por_director,
)


def cargar_peliculas() -> dict[str, dict[str, Any]]:
    """Carga películas hasta que se ingrese un título en blanco.

    Returns:
        dict[str, dict[str, Any]]: Películas indexadas por título.
    """
    peliculas: dict[str, dict[str, Any]] = {}
    titulo = input("Título (Enter para terminar): ")
    while titulo != "":
        director = input("Director: ")
        anio = int(input("Año de estreno: "))
        actores = input("Actores principales (separados por coma): ")
        peliculas[titulo] = {
            "director": director,
            "anio": anio,
            "actores": [actor.strip() for actor in actores.split(",")],
        }
        titulo = input("Título (Enter para terminar): ")
    return peliculas


def main() -> None:
    """Carga el catálogo y resuelve las consultas del enunciado."""
    peliculas = cargar_peliculas()

    print("a. Películas por director:")
    for director, cantidad in peliculas_por_director(peliculas).items():
        print(f"   {director}: {cantidad}")
    print(f"b. Director con más películas: "
          f"{director_con_mas_peliculas(peliculas)}")

    titulo = input("c. Título a consultar: ")
    print(f"   Actores: {actores_de_pelicula(peliculas, titulo)}")

    actor = input("d. Actor a consultar: ")
    print(f"   Películas: {peliculas_de_actor(peliculas, actor)}")


if __name__ == "__main__":
    main()
