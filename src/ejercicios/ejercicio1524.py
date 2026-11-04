"""Ejercicio 1524: administración de socios del Club CAVUL.

Carga los socios en un diccionario con el DNI como clave. Informa la
cantidad de socios y de morosos, busca un socio por DNI, da de alta a
un socio nuevo, informa el DNI del socio de mayor edad, da de baja a
un socio solo si tiene la cuota al día y registra el pago de otro.
"""

from funciones import cargar_socios, contar_morosos, dni_mayor_edad

socios: dict = cargar_socios()

print(f"Cantidad de socios: {len(socios)}")

print(f"Cantidad de socios morosos: {contar_morosos(socios)}")

if 25123555 in socios:
    print(socios[25123555][0], socios[25123555][1])
else:
    print("No existe un socio con DNI 25123555")

socios[40151724] = ["Esteban", "Quito", 17, True]

print(f"DNI del socio de mayor edad: {dni_mayor_edad(socios)}")

if 15188125 not in socios:
    print("El DNI 15188125 no corresponde a un socio")
elif not socios[15188125][3]:
    print("No se acepta la baja: el socio no tiene la cuota al dia")
else:
    del socios[15188125]

if 28731431 in socios:
    socios[28731431][3] = True
else:
    print("No existe un socio con DNI 28731431")
    