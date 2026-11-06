"""Ejercicio 1515: gestión de ciudades y personas."""

Persona = list[str | int]
Ciudad = list[str]


def obtenerCiudad(personas: list[Persona], DNI: int) -> str | None:
    """Busca la ciudad correspondiente a un DNI."""
    for persona in personas:
        if persona[1] == DNI:
            return str(persona[2])
    return None


def obtenerProvincia(
    personas: list[Persona], ciudades: list[Ciudad], DNI: int
) -> str | None:
    """Busca la provincia utilizando obtenerCiudad."""
    ciudad_persona = obtenerCiudad(personas, DNI)
    for ciudad in ciudades:
        if ciudad[0] == ciudad_persona:
            return ciudad[1]
    return None


def contarPoblacion(
    personas: list[Persona], ciudades: list[Ciudad], provincia: str
) -> int:
    """Cuenta las personas que viven en una provincia."""
    cantidad = 0
    for persona in personas:
        provincia_persona = obtenerProvincia(
            personas, ciudades, int(persona[1])
        )
        if provincia_persona == provincia:
            cantidad += 1
    return cantidad


def main() -> None:
    """Ejecuta ejemplos de las funciones."""
    ciudades: list[Ciudad] = [
        ["Rosario", "Santa Fe"],
        ["Carlos Paz", "Córdoba"],
        ["Balcarce", "Buenos Aires"],
        ["Cosquín", "Córdoba"]
    ]
    personas: list[Persona] = [
        ["Juan Perez", 26782345, "Carlos Paz"],
        ["María Gomez", 40173542, "Rosario"],
        ["Ana Ríos", 9216378, "Cosquín"]
    ]

    print(obtenerCiudad(personas, 26782345))
    print(obtenerProvincia(personas, ciudades, 26782345))
    print(contarPoblacion(personas, ciudades, "Córdoba"))


if __name__ == "__main__":
    main()
