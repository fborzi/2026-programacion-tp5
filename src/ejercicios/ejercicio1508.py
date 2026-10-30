"""Programa que determina el ganador de una partida de piedra,
papel o tijera entre dos jugadores. Retorna 1 si gana el primero,
2 si gana el segundo y 0 si hay empate, ignorando mayúsculas
y minúsculas."""

from funciones import piedra_papel_tijera

print(piedra_papel_tijera("piedra", "tijera"))
print(piedra_papel_tijera("papel", "papel"))
print(piedra_papel_tijera("tijera", "piedra"))
