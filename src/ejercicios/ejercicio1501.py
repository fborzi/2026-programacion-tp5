#EJERCICIO 1501 - PERTENENCIA A UNA LISTA

b = [4, "palabra", [0, 1], 9.6, False]

if 9.6 in b:
    print("9.6 pertenece a la lista")
else:
    print("9.6 no pertenece a la lista")

if 0 in b:
    print("0 pertenece a la lista")
else:
    print("0 no pertenece a la lista")

if False in b:
    print("False pertenece a la lista")
else:
    print("False no pertenece a la lista")

if [0, 1] in b:
    print("[0, 1] pertenece a la lista")
else:
    print("[0, 1] no pertenece a la lista")

if 4.0 in b:
    print("4.0 pertenece a la lista")
else:
    print("4.0 no pertenece a la lista")

if "p" in b:
    print("'p' pertenece a la lista")
else:
    print("'p' no pertenece a la lista")


