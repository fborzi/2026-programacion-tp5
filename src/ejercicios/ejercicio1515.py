from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion

ciudades = [
    ["Rosario", "Santa Fe"],
    ["Carlos Paz", "Cordoba"],
    ["Balcarce", "Buenos Aires"],
    ["Cosquin", "Cordoba"]
]

personas = [
    ["Juan Perez", 26782345, "Carlos Paz"],
    ["Maria Gomez", 40173542, "Rosario"],
    ["Ana Rios", 9216378, "Cosquin"]
]

print(obtenerCiudad(personas, 26782345))
print(obtenerProvincia(personas, ciudades, 26782345))
print(contarPoblacion(personas, ciudades, "Cordoba"))