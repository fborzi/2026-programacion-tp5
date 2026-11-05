from funciones import obtenerCiudad, obtenerProvincia, contarPoblacion


personas = [
    {"nombre": "Juan Perez", "DNI": 26782345, "ciudad": "Carlos Paz"},
    {"nombre": "Maria Gomez", "DNI": 40173542, "ciudad": "Rosario"},
    {"nombre": "Ana Rios", "DNI": 9216378, "ciudad": "Cosquin"}
]

ciudades = [
    {"nombre": "Rosario", "provincia": "Santa Fe"},
    {"nombre": "Carlos Paz", "provincia": "Cordoba"},
    {"nombre": "Balcarce", "provincia": "Buenos Aires"},
    {"nombre": "Cosquin", "provincia": "Cordoba"}
]

print(obtenerCiudad(personas, 26782345))
print(obtenerProvincia(personas, ciudades, 40173542))
print(contarPoblacion(personas, ciudades, "Cordoba"))