
"""Prueba la consulta de ciudades y provincias de las personas
y cuenta cuántas personas viven en una provincia determinada."""

from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion


def main():
    ciudades = [
        ["Rosario", "Santa Fe"],
        ["Carlos Paz", "Córdoba"],
        ["Balcarce", "Buenos Aires"],
        ["Cosquín", "Córdoba"]
    ]

    personas = [
        ["Juan Perez", 26782345, "Carlos Paz"],
        ["María Gomez", 40173542, "Rosario"],
        ["Ana Ríos", 9216378, "Cosquín"]
    ]

 
    print("a. Ciudad:", obtenerCiudad(personas, 26782345))

   
    print("b. Provincia:", obtenerProvincia(personas, ciudades, 26782345))

   
    print("c. Población de Córdoba:",
          contarPoblacion(personas, ciudades, "Córdoba"))


if __name__ == "__main__":
    main()
