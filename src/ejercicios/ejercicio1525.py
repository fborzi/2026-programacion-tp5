from funciones import  frecuencia_caracteres

print("Ingrese una cadena de caracteres:")
cadena = input()

frecuencia = frecuencia_caracteres(cadena)

print("Frecuencia de caracteres:")
for caracter, cantidad in frecuencia.items():
    print(f"'{caracter}': {cantidad}")
