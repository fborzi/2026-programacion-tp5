"""Carga interactiva de nombres en un listado y convertida a mayusculas"""


nombre= input("ingrege un nombre: ")
listado=[]

while nombre != "":
    listado.append(nombre)
    nombre= input("ingrege un nombre: ")


for nombre in listado:
    print(nombre.upper())