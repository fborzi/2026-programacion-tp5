"""Programa que registra socios de un club en un diccionario,
utilizando el DNI como clave y guardando sus datos personales
y el estado de pago de la cuota. Permite consultar y mostrar
información de los socios registrados."""

socios = {}


dni = int(input("Ingrese el DNI del socio (0 para terminar): "))

while dni != 0:
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    respuesta = input("¿Tiene la cuota al día? (s/n): ")

    cuota_al_dia = respuesta.lower() == "s"

    socios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cuota_al_dia": cuota_al_dia
    }

    dni = int(input("Ingrese el DNI del socio (0 para terminar): "))



print("\na. Cantidad de socios:", len(socios))


morosos = 0

for socio in socios.values():
    if not socio["cuota_al_dia"]:
        morosos = morosos + 1

print("b. Cantidad de socios morosos:", morosos)

dni_buscar = 25123555

if dni_buscar in socios:
    print("c. Nombre:", socios[dni_buscar]["nombre"])
    print("   Apellido:", socios[dni_buscar]["apellido"])
else:
    print("c. No existe un socio con ese DNI.")


# d. Dar de alta al nuevo socio Esteban Quito
socios[40151724] = {
    "nombre": "Esteban",
    "apellido": "Quito",
    "edad": 17,
    "cuota_al_dia": True
}

print("d. Se dio de alta al socio Esteban Quito.")


# e. Informar el DNI del socio de mayor edad
dni_mayor = None
mayor_edad = -1

for dni, socio in socios.items():
    if socio["edad"] > mayor_edad:
        mayor_edad = socio["edad"]
        dni_mayor = dni

print("e. DNI del socio de mayor edad:", dni_mayor)


dni_baja = 15188125

if dni_baja in socios:
    if socios[dni_baja]["cuota_al_dia"]:
        del socios[dni_baja]
        print("f. Socio eliminado correctamente.")
    else:
        print("f. No se puede dar de baja: tiene la cuota atrasada.")
else:
    print("f. No existe un socio con ese DNI.")

dni_pago = 28731431

if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = True
    print("g. Se registró el pago de la cuota.")
else:
    print("g. No existe un socio con ese DNI.")
