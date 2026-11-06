socios = {}

dni = int(input("Ingrese DNI (0 para terminar): "))
while dni != 0:
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    cuota = input("¿Cuota al día? (s/n): ").lower() == "s"

    socios[dni] = {
        "apellido": apellido,
        "nombre": nombre,
        "edad": edad,
        "cuota": cuota
    }

    dni = int(input("Ingrese DNI (0 para terminar): "))

print("Cantidad de socios:", len(socios))

# socios morosos
morosos = sum(1 for s in socios.values() if not s["cuota"])
print("Cantidad de socios morosos:", morosos)

#Buscar socio por DNI
dni_buscar = 25123555
if dni_buscar in socios:
    socio = socios[dni_buscar]
    print(f"Socio encontrado: {socio['nombre']} {socio['apellido']}")
else:
    print("No existe socio con ese DNI.")

#Alta de nuevo socio
socios[40151724] = {"apellido": "Quito", "nombre": "Esteban", "edad": 17, "cuota": True}

# socio de mayor edad
dni_mayor = max(socios, key=lambda d: socios[d]["edad"])
print("DNI del socio de mayor edad:", dni_mayor)

#Baja de socio 
dni_baja = 15188125
if dni_baja in socios:
    if socios[dni_baja]["cuota"]:
        del socios[dni_baja]
        print("Socio dado de baja.")
    else:
        print("No se puede dar de baja: cuota no al día.")
else:
    print("No existe socio con ese DNI.")

#pago
dni_pago = 28731431
if dni_pago in socios:
    socios[dni_pago]["cuota"] = True
    print("Pago registrado.")
else:
    print("No existe socio con ese DNI.")
