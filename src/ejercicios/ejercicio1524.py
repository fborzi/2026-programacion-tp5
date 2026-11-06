"""Ejercicio 1524: administración de socios del Club CAVUL."""

from typing import Any


def cargar_socios() -> dict[int, dict[str, Any]]:
    """Carga socios por teclado hasta que se ingrese el DNI 0.

    Returns:
        dict[int, dict[str, Any]]: Socios indexados por DNI.
    """
    socios: dict[int, dict[str, Any]] = {}
    dni = int(input("DNI (0 para terminar): "))
    while dni != 0:
        socios[dni] = {
            "nombre": input("Nombre: "),
            "apellido": input("Apellido: "),
            "edad": int(input("Edad: ")),
            "al_dia": input("¿Cuota al día? (s/n): ").strip().lower() == "s",
        }
        dni = int(input("DNI (0 para terminar): "))
    return socios


def contar_morosos(socios: dict[int, dict[str, Any]]) -> int:
    """Cuenta los socios que no tienen la cuota al día.

    Args:
        socios (dict): Socios indexados por DNI.

    Returns:
        int: Cantidad de socios morosos.
    """
    return sum(1 for socio in socios.values() if not socio["al_dia"])


def dni_mayor_edad(socios: dict[int, dict[str, Any]]) -> int | None:
    """Obtiene el DNI del socio de mayor edad.

    Args:
        socios (dict): Socios indexados por DNI.

    Returns:
        int | None: DNI del socio más grande, o None si no hay socios.
    """
    if len(socios) == 0:
        return None
    return max(socios, key=lambda dni: socios[dni]["edad"])


def dar_de_baja(socios: dict[int, dict[str, Any]], dni: int) -> str:
    """Da de baja a un socio sólo si existe y tiene la cuota al día.

    Args:
        socios (dict): Socios indexados por DNI.
        dni (int): DNI del socio a dar de baja.

    Returns:
        str: Mensaje con el resultado de la operación.
    """
    mensaje = f"El DNI {dni} no es socio del club."
    if dni in socios and not socios[dni]["al_dia"]:
        mensaje = f"El socio {dni} adeuda la cuota, no se puede dar de baja."
    elif dni in socios:
        del socios[dni]
        mensaje = f"El socio {dni} fue dado de baja."
    return mensaje


def registrar_pago(socios: dict[int, dict[str, Any]], dni: int) -> str:
    """Marca la cuota de un socio como pagada.

    Args:
        socios (dict): Socios indexados por DNI.
        dni (int): DNI del socio que pagó.

    Returns:
        str: Mensaje con el resultado de la operación.
    """
    if dni not in socios:
        return f"El DNI {dni} no es socio del club."
    socios[dni]["al_dia"] = True
    return f"Se registró el pago del socio {dni}."


def main() -> None:
    """Carga los socios y resuelve los puntos del enunciado."""
    socios = cargar_socios()

    print(f"a. Cantidad de socios: {len(socios)}")
    print(f"b. Socios morosos: {contar_morosos(socios)}")

    dni_buscado = 25123555
    if dni_buscado in socios:
        socio = socios[dni_buscado]
        print(f"c. Socio {dni_buscado}: {socio['nombre']} "
              f"{socio['apellido']}")
    else:
        print(f"c. No existe un socio con DNI {dni_buscado}.")

    socios[40151724] = {"nombre": "Esteban", "apellido": "Quito",
                        "edad": 17, "al_dia": True}
    print("d. Se dio de alta a Esteban Quito (DNI 40151724).")

    print(f"e. DNI del socio de mayor edad: {dni_mayor_edad(socios)}")
    print(f"f. {dar_de_baja(socios, 15188125)}")
    print(f"g. {registrar_pago(socios, 28731431)}")


if __name__ == "__main__":
    main()
