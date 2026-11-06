"""Ejercicio 1522: gestión de población de ciudades con diccionarios."""


def main() -> None:
    """Realiza las operaciones pedidas sobre el diccionario de ciudades."""
    poblacion = {"Junín": 102023, "Rojas": 28654, "Pergamino": 80569}

    print(f"a. Habitantes de Pergamino: {poblacion['Pergamino']}")
    poblacion["Lincoln"] = 42036
    print(f"b. Se agregó Lincoln: {poblacion}")
    del poblacion["Junín"]
    print(f"c. Se eliminó Junín: {poblacion}")
    poblacion["Rojas"] += 1000
    print(f"d. Rojas ahora tiene {poblacion['Rojas']} habitantes")
    poblacion["Pergamino"] = 91399
    print(f"e. Pergamino ahora tiene {poblacion['Pergamino']} habitantes")


if __name__ == "__main__":
    main()
