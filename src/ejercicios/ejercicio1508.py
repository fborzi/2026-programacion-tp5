def piedra_papel_tijera(uno, dos):
    """
    Simula el juego de Piedra, Papel o Tijera entre dos jugadores.
    
    Args:
        uno (str): Elemento elegido por el primer jugador ('piedra', 'papel' o 'tijera').
        dos (str): Elemento elegido por el segundo jugador ('piedra', 'papel' o 'tijera').
        
    Returns:
        int: 1 si gana el primer jugador, 2 si gana el segundo, o 0 si hubo empate.
    """
    j1 = uno.strip().lower()
    j2 = dos.strip().lower()
    
    if j1 == j2:
        return 0
    
    if (j1 == 'piedra' and j2 == 'tijera') or \
       (j1 == 'tijera' and j2 == 'papel') or \
       (j1 == 'papel' and j2 == 'piedra'):
        return 1
    
    return 2