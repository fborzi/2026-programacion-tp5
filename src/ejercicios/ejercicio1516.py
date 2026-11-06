"""Ejercicio 1516: operaciones básicas con conjuntos numéricos."""


def main() -> None:
    """Arma el conjunto pedido e informa lo solicitado."""
    numeros = set(range(1, 11))
    numeros.add(11)
    numeros.add(12)
    numeros.update(range(30, 36))
    numeros.update({232, -264})

    print(f"Conjunto: {sorted(numeros)}")
    print("a. Un set no tiene orden, así que no existe un 'primero' ni un "
          "'último' almacenado.")
    print(f"   Como referencia, el menor es {min(numeros)} "
          f"y el mayor es {max(numeros)}.")
    print(f"b. ¿Está el 7? {7 in numeros}. ¿Está el 20? {20 in numeros}.")
    print(f"c. Cantidad de elementos: {len(numeros)}")


if __name__ == "__main__":
    main()
