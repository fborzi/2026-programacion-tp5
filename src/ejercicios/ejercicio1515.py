from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

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

print(obtenerCiudad(personas, 40173542))
print(obtenerProvincia(personas, ciudades, 26782345))
print(contarPoblacion(personas, ciudades, "Córdoba"))
print(contarPoblacion(personas, ciudades, "Buenos Aires"))
