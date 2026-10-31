"""Ejercicio 1508: juego de piedra, papel o tijera."""

from src.ejercicios.funciones import piedra_papel_tijera


def main() -> None:
    """Pide la elección de dos jugadores e informa el resultado."""
    opciones = ("piedra", "papel", "tijera")
    uno = input("Jugador 1 (piedra/papel/tijera): ").strip().lower()
    dos = input("Jugador 2 (piedra/papel/tijera): ").strip().lower()
    if uno in opciones and dos in opciones:
        resultado = piedra_papel_tijera(uno, dos)
        mensajes = {0: "Empate.", 1: "Gana el jugador 1.",
                    2: "Gana el jugador 2."}
        print(mensajes[resultado])
    else:
        print("Opción inválida.")


if __name__ == "__main__":
    main()
