"""Ejercicio 1526: conteo y agrupación de ciudades por país."""

from src.ejercicios.funciones import contar_por_pais

FIN_CARGA = "zz"


def version_sin_almacenar() -> tuple[int, dict[str, int]]:
    """Cuenta las ciudades a medida que se ingresan, sin guardarlas.

    Returns:
        tuple[int, dict[str, int]]: Total de ciudades y conteo por país.
    """
    total = 0
    por_pais: dict[str, int] = {}
    ciudad = input("Ciudad (zz para terminar): ")
    while ciudad.lower() != FIN_CARGA:
        pais = input("País: ")
        total += 1
        por_pais[pais] = por_pais.get(pais, 0) + 1
        ciudad = input("Ciudad (zz para terminar): ")
    return total, por_pais


def cargar_ciudades() -> list[list[str]]:
    """Guarda cada ciudad con su país hasta que se ingrese zz.

    Returns:
        list[list[str]]: Pares [ciudad, país] en el orden de carga.
    """
    ciudades: list[list[str]] = []
    ciudad = input("Ciudad (zz para terminar): ")
    while ciudad.lower() != FIN_CARGA:
        pais = input("País: ")
        ciudades.append([ciudad, pais])
        ciudad = input("Ciudad (zz para terminar): ")
    return ciudades


def mostrar_resultados(total: int, por_pais: dict[str, int]) -> None:
    """Muestra el total de ciudades y el detalle por país.

    Args:
        total (int): Cantidad total de ciudades ingresadas.
        por_pais (dict[str, int]): Cantidad de ciudades por país.
    """
    print(f"Total de ciudades ingresadas: {total}")
    for pais, cantidad in por_pais.items():
        print(f"  {pais}: {cantidad}")


def main() -> None:
    """Permite elegir la versión del programa y la ejecuta."""
    opcion = input("Versión a (sin guardar) o b (con lista): ").lower()
    if opcion == "a":
        total, por_pais = version_sin_almacenar()
    else:
        ciudades = cargar_ciudades()
        total, por_pais = len(ciudades), contar_por_pais(ciudades)
    mostrar_resultados(total, por_pais)


if __name__ == "__main__":
    main()
