entrada = input("Ingrese números separados por espacio: ")
lista = [int(x) for x in entrada.split()]

objetivo = int(input("Ingrese el número resultado: "))

indices = dos_sumandos(lista, objetivo)

if indices:
    print("Los índices encontrados son:", indices)
else:
    print("No hay dos números que sumen", objetivo)
