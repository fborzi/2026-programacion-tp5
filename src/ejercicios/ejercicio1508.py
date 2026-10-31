def piedra_papel_tijeras(jugador1, jugador2):
    # normalizamos a minúsculas
    j1 = jugador1.lower()
    j2 = jugador2.lower()

    opciones = ["piedra", "papel", "tijeras"]
    
    if j1 not in opciones or j2 not in opciones:
        return "Opción no válida. Usá piedra, papel o tijeras."

    if j1 == j2:
        return "Empate"

    # reglas: piedra gana a tijeras, tijeras a papel, papel a piedra
    gana_j1 = (j1 == "piedra" and j2 == "tijeras") or \
              (j1 == "tijeras" and j2 == "papel") or \
              (j1 == "papel" and j2 == "piedra")

    if gana_j1:
        return f"Gana jugador 1: {j1} le gana a {j2}"
    else:
        return f"Gana jugador 2: {j2} le gana a {j1}"


print(piedra_papel_tijeras("Piedra", "TIJERAS"))  # Gana jugador 1
print(piedra_papel_tijeras("papel", "Piedra"))    # Gana jugador 1
print(piedra_papel_tijeras("PAPEL", "papel"))     # Empate