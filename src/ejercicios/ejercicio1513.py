
def indice_mayor(lista):
    if not lista:
        return None
    max_val = lista[0]
    idx_max = 0
    for i in range(1, len(lista)):
        if lista[i] > max_val:
            max_val = lista[i]
            idx_max = i
    return idx_max

print(indice_mayor([6, 1, 7, 19, 2]))