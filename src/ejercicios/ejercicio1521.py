


oracion = []
continuar = True

while continuar:
    oracion = input("Ingresá una oración: ")
    if oracion.endswith("."):
        oracion.append(oracion[:-1])  
        break
    oracion.append(oracion)