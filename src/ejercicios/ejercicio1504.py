nombres = []
nombre = "x"

while nombre != "":
    nombre = input("Ingrese un nombre (ENTER para terminar): ")
    if nombre != "":
        nombres.append(nombre)

print("\nLista de nombres ingresados:")
for n in nombres:
    print(n)
