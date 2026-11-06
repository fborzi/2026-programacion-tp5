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

def obtenerCiudad(personas, DNI):
    for p in personas:
        if p[1] == DNI:
            return p[2]
    return None

def obtenerProvincia(personas, ciudades, DNI):
    ciudad = obtenerCiudad(personas, DNI)
    if ciudad:
        for c in ciudades:
            if c[0] == ciudad:
                return c[1]
    return None

def contarPoblacion(personas, ciudades, provincia):
    cantidad = 0
    for p in personas:
        prov = obtenerProvincia(personas, ciudades, p[1])
        if prov == provincia:
            cantidad += 1
    return cantidad

print("Ciudad de DNI 26782345:", obtenerCiudad(personas, 26782345))
print("Provincia de DNI 26782345:", obtenerProvincia(personas, ciudades, 26782345))
print("Población en Córdoba:", contarPoblacion(personas, ciudades, "Córdoba"))
