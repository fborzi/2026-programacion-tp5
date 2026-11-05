socios = {}

dni =int (input("Ingrese el DNI del socio (0 para terminar): "))   

while dni != 0:
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    cuota_al_dia = input("¿Tiene la cuota al día? (si/no): ").lower() == "si"
    
    socios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cuota_al_dia": cuota_al_dia
    }
    dni =int (input("Ingrese el DNI del socio (0 para terminar): "))   
    
print(f"Cantidad de socios del club: {len(socios)}")
morosos = sum(1 for datos in socios.values() if not datos["cuota_al_dia"])
print(f"Cantidad de socios morosos: {morosos}")

dni_buscado = "25123555"
if dni_buscado in socios:
    socio = socios[dni_buscado]
    print(f"c. El socio con DNI {dni_buscado} es: {socio['nombre']} {socio['apellido']}")
else:
    print(f"Situación: No existe ningún socio con el DNI {dni_buscado}")

socios["40151724"] = {
    "nombre": "Esteban",
    "apellido": "Quito",
    "edad": 17,
    "cuota_al_dia": True
}
print("Nuevo socio Esteban Quito dado de alta con éxito.")

edad_maxima = -1
dni_del_mayor = ""

for dni, datos in socios.items():
    if datos["edad"] > edad_maxima:
        edad_maxima = datos["edad"] 
        dni_del_mayor = dni         

print(f"El DNI del socio de mayor edad es: {dni_del_mayor} (Edad: {edad_maxima})")

dni_baja = "15188125"
if dni_baja in socios:
    if socios[dni_baja]["cuota_al_dia"]:
        del socios[dni_baja]
        print(f"El socio con DNI {dni_baja} fue dado de baja correctamente.")
    else:
        print(f"No se puede aceptar la baja: El socio con DNI {dni_baja} es moroso.")
else:
    print(f"f. Error: El DNI {dni_baja} no pertenece a ningún socio del club.")
    
dni_pago = "28731431"
if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = True
    print(f"Se registró el pago del mes para el socio con DNI {dni_pago}.")
print(socios)