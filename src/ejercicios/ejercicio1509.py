def digitos(numero):
    return [int(d) for d in str(abs(numero))]

print("Ingresá un número entero (presioná Enter en blanco para salir):")
while True:
    entrada = input()
    if entrada == "":
        break
    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        num = int(entrada)
        print("Resultado:", digitos(num))
        break
    else:
        print("Por favor, ingresá un número entero válido.")



