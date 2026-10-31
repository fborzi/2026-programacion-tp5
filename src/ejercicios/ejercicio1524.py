socios = {}  # clave: DNI, valor: dict con datos

# --- CARGA DE DATOS ---
# La lectura finaliza con DNI '0'
while True:
    dni = input("DNI del socio (0 para terminar): ").strip()
    if dni == "0" or dni == "0.": # por si lo ponen con punto
        break
    if not dni:
        continue
        
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    cuota_input = input("¿Cuota al día? (s/n): ").lower()
    cuota_al_dia = cuota_input == 's'

    socios[dni] = {
        "apellido": apellido,
        "nombre": nombre,
        "edad": edad,
        "cuota_al_dia": cuota_al_dia
    }

# --- Si querés probar sin cargar todo a mano, usá estos datos de ejemplo: ---
# socios = {
#     "25.123.555": {"apellido": "Perez", "nombre": "Juan", "edad": 30, "cuota_al_dia": False},
#     "15.188.125": {"apellido": "Gomez", "nombre": "Ana", "edad": 45, "cuota_al_dia": True},
#     "28.731.431": {"apellido": "Lopez", "nombre": "Luis", "edad": 22, "cuota_al_dia": False},
# }

# a. Informar la cantidad de socios del club
print(f"\na) Cantidad de socios: {len(socios)}")

# b. Informar la cantidad de socios morosos
morosos = sum(1 for datos in socios.values() if not datos["cuota_al_dia"])
print(f"b) Cantidad de morosos: {morosos}")

# c. Informar nombre y apellido del socio cuyo DNI es 25.123.555
dni_buscar = "25.123.555"
if dni_buscar in socios:
    s = socios[dni_buscar]
    print(f"c) El socio {dni_buscar} es {s['nombre']} {s['apellido']}")
else:
    print(f"c) No existe un socio con DNI {dni_buscar}")

# d. Dar de alta a un nuevo socio: DNI 40.151.724, apellido Quito, nombre Esteban, edad 17, cuota paga
socios["40.151.724"] = {
    "apellido": "Quito",
    "nombre": "Esteban",
    "edad": 17,
    "cuota_al_dia": True
}
print(f"d) Alta de Esteban Quito realizada.")

# e. Informar el número de documento del socio de mayor edad
if socios:
    dni_mayor = max(socios, key=lambda d: socios[d]["edad"])
    print(f"e) Socio de mayor edad: DNI {dni_mayor} - {socios[dni_mayor]['nombre']} {socios[dni_mayor]['apellido']} ({socios[dni_mayor]['edad']} años)")
else:
    print("e) No hay socios cargados")

# f. Dar de baja al socio con DNI 15.188.125, solo si existe y tiene cuota al día
dni_baja = "15.188.125"
if dni_baja not in socios:
    print(f"f) No se puede dar de baja: el DNI {dni_baja} no es socio del club")
elif not socios[dni_baja]["cuota_al_dia"]:
    print(f"f) No se puede dar de baja a {dni_baja} porque no tiene la cuota al día")
else:
    del socios[dni_baja]
    print(f"f) Socio {dni_baja} dado de baja correctamente")

# g. Registrar que el socio DNI 28.731.431 acaba de pagar la cuota
dni_pago = "28.731.431"
if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = True
    print(f"g) Se registró el pago de cuota del socio {dni_pago}")
else:
    print(f"g) No existe socio con DNI {dni_pago} para registrar el pago")

print("\nListado final:", socios)