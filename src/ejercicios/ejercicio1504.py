"""Programa que solicita nombres por teclado hasta que se ingresa
un nombre vacío. Guarda los nombres en una lista y luego los
muestra en pantalla, uno por línea."""

nombres = []

nombre = input("Ingrese un nombre (Enter para terminar): ")

while nombre != "":
    nombres.append(nombre)
    nombre = input("Ingrese un nombre (Enter para terminar): ")

for nombre in nombres:
    print (nombre)
