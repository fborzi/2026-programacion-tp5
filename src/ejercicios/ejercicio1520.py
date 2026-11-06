def analizar_texto():
    """
    Solicita el ingreso de un texto por teclado e informa la cantidad total 
    de palabras y las letras repetidas dentro de cada una de ellas.
    """
    texto = input("Ingresá un texto: ")
    
    palabras = texto.split()
    print(f"\na. Cantidad total de palabras: {len(palabras)}")
    
    print("b. Letras repetidas por palabra:")
    
    for palabra in palabras:
        solo_letras = "".join([c for c in palabra if c.isalpha()])
        
        if not solo_letras:
            continue
            
        palabra_lower = solo_letras.lower()
        
        vistos = set()
        repetidas = set()
        
        for letra in palabra_lower:
            if letra in vistos:
                repetidas.add(letra)
            else:
                vistos.add(letra)
                
        if repetidas:
            letras_ordenadas = sorted(list(repetidas))
            print(f"   - En '{solo_letras}', las letras repetidas son: {letras_ordenadas}")
        else:
            print(f"   - En '{solo_letras}' no se repiten letras.")

if __name__ == "__main__":
    analizar_texto()