"""Ejercicio 1523: registro y consulta de pacientes."""

Paciente = dict[str, int | str | bool]
Registro = dict[int, Paciente]


def crear_pacientes() -> Registro:
    """Crea el registro inicial de pacientes."""
    return {
        11412625: {"edad": 60, "sexo": "Masculino", "diabetico": True},
        6409217: {"edad": 65, "sexo": "Femenino", "diabetico": False},
        19172162: {"edad": 45, "sexo": "Masculino", "diabetico": False},
        28141815: {"edad": 34, "sexo": "Femenino", "diabetico": True},
        14972142: {"edad": 58, "sexo": "Masculino", "diabetico": True},
        36843316: {"edad": 23, "sexo": "Femenino", "diabetico": False}
    }


def incrementar_edad(pacientes: Registro, dni: int) -> bool:
    """Incrementa la edad de un paciente si existe."""
    if dni not in pacientes:
        return False

    pacientes[dni]["edad"] = int(pacientes[dni]["edad"]) + 1
    return True


def pacientes_diabeticos(pacientes: Registro) -> list[int]:
    """Devuelve los DNI de los pacientes diabéticos."""
    return [
        dni for dni, datos in pacientes.items()
        if datos["diabetico"]
    ]


def promedio_diabeticos(pacientes: Registro) -> float:
    """Calcula el promedio de edad de pacientes diabéticos."""
    edades = [
        int(datos["edad"])
        for datos in pacientes.values()
        if datos["diabetico"]
    ]
    return sum(edades) / len(edades) if edades else 0.0


def existe_mayor_sin_diabetes(pacientes: Registro) -> bool:
    """Indica si existe un mayor de 80 años sin diabetes."""
    return any(
        int(datos["edad"]) > 80 and not datos["diabetico"]
        for datos in pacientes.values()
    )


def main() -> None:
    """Muestra los datos y realiza las consultas solicitadas."""
    pacientes = crear_pacientes()

    print("Cantidad de pacientes:", len(pacientes))
    print("Listado de pacientes:")

    for dni, datos in pacientes.items():
        print("DNI:", dni, "Datos:", datos)

    dni = int(input("Ingrese DNI para incrementar la edad: "))

    if incrementar_edad(pacientes, dni):
        print("Edad actualizada:", pacientes[dni]["edad"])
    else:
        print("Paciente no encontrado")

    print("Pacientes con diabetes:")
    for dni in (14972142, 6409217):
        print(dni, dni in pacientes_diabeticos(pacientes))

    print("Promedio de edad con diabetes:", promedio_diabeticos(pacientes))
    print(
        "Existe mayor de 80 años sin diabetes:",
        existe_mayor_sin_diabetes(pacientes)
    )


if __name__ == "__main__":
    main()
