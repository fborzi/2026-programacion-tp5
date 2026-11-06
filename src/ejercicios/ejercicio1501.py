from funciones import comparar_elementos_en_lista

print(comparar_elementos_en_lista(
    [4, "palabra", [0, 1], 9.6, False], [9.6, 0, False, [0, 1], 4.0, "p"]))

lista1 = [4, "palabra", [0, 1], 9.6, False]
print(lista1.index([0, 1]))
