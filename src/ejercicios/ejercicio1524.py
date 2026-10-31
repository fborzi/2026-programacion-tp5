socios = {}

dni = input("Ingrese DNI (0 para finalizar): ")

while dni != "0":
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))
    cuota = input("¿Tiene la cuota al día? (si/no): ")

    socios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cuota": cuota
    }

    dni = input("Ingrese DNI (0 para finalizar): ")


print("Cantidad de socios:", len(socios))

morosos = 0

for dni in socios:
    if socios[dni]["cuota"] == "no":
        morosos = morosos + 1

print("Cantidad de socios morosos:", morosos)


if "25123555" in socios:
    print("Socio:", socios["25123555"]["nombre"],
          socios["25123555"]["apellido"])
else:
    print("No existe un socio con ese DNI")

socios["40151724"] = {
    "nombre": "Esteban",
    "apellido": "Quito",
    "edad": 17,
    "cuota": "si"
}


mayor_edad = -1
dni_mayor = ""

for dni in socios:
    if socios[dni]["edad"] > mayor_edad:
        mayor_edad = socios[dni]["edad"]
        dni_mayor = dni

print("DNI del socio de mayor edad:", dni_mayor)

dni_baja = "15188125"

if dni_baja in socios:
    if socios[dni_baja]["cuota"] == "si":
        del socios[dni_baja]
        print("Socio eliminado correctamente")
    else:
        print("No se puede eliminar: tiene la cuota pendiente")
else:
    print("El socio no existe")


dni_pago = "28731431"

if dni_pago in socios:
    socios[dni_pago]["cuota"] = "si"
    print("Pago registrado correctamente")
else:
    print("No existe un socio con ese DNI")