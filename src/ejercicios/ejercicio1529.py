
# EJERCICIO 1529 - SUCESION MIRA Y DECI (LOOK-AND-SAY)

def sucesion_mira_y_deci(n):

    # Verificar que la cantidad de numeros sea valida
    if n < 0:
        raise ValueError("La cantidad de numeros no puede ser negativa")

    # Lista que almacena la sucesion
    L = [1]

    # Generar los siguientes numeros de la sucesion
    while len(L) < n:

        anterior = str(L[-1])
        nuevo = ""
        contador = 1

        # Recorrer los digitos del numero anterior
        for i in range(len(anterior)):

            if i + 1 < len(anterior) and anterior[i] == anterior[i + 1]:
                contador += 1

            else:
                nuevo += str(contador) + anterior[i]
                contador = 1

        # Agregar el nuevo numero a la lista
        L.append(int(nuevo))

    return L


# Solicitar la cantidad de numeros de la sucesion
n = int(input("Ingrese la cantidad de numeros de la sucesion: "))

# Mostrar el resultado
resultado = sucesion_mira_y_deci(n)

print("\nSucesion Mira y Deci:")
print(resultado)

