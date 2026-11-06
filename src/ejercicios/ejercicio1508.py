jugador1 = input("Jugador 1, elija piedra, papel o tijera: ")
jugador2 = input("Jugador 2, elija piedra, papel o tijera: ")

resultado = piedra_papel_tijera(jugador1, jugador2)

if resultado == 0:
    print("Empate")
elif resultado == 1:
    print("Ganó el jugador 1")
else:
    print("Ganó el jugador 2")
