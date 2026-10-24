# Ejercicio 1508: juego de piedra, papel o tijera 
"""Este código determina el ganador de un 
juego de piedra, papel o tijera entre dos jugadores."""

from funciones import piedra_papel_tijera

uno = input("Jugador 1, elegi piedra, papel o tijera: ")
dos = input("Jugador 2, elegi piedra, papel o tijera: ")

resultado = piedra_papel_tijera(uno, dos)

if resultado == 1:
    print("Gano el jugador 1.")
elif resultado == 2:
    print("Gano el jugador 2.")
else:
    print("empate.")

