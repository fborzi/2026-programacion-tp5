def ocurrencias(lista):
   
    if not lista:
        return []
    resultado = []
    elem_actual = lista[0]
    contador = 1
    for elem in lista[1:]:
        if elem == elem_actual:
            contador += 1
        else:
            resultado.append([elem_actual, contador])
            elem_actual = elem
            contador = 1
    resultado.append([elem_actual, contador])
    return resultado

print(ocurrencias(['z', 7, True, True, 34, 'z', 'z', 'z', 3.14]))