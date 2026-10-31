nombres = []

nombre = input("Ingrese un nombre: ")

while nombre != "":
    nombres.append(nombre)
    nombre = input("Ingrese un nombre: ")

nombres_mayusculas = []

for nombre in nombres:
    if nombre.isupper():
        nombres_mayusculas.append(nombre)

print(nombres_mayusculas)
