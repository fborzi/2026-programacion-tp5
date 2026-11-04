pacientes = {
    11412625: [60, "Masculino", "Sí"],
    6409217: [65, "Femenino", "No"],
    19172162: [45, "Maculino", "No"],
    28141815: [34, "Femenino", "Sí"],
    14982142: [58, "Masculino", "Sí"],
    36843316: [23, "Femenino", "No"]
}

print("Cantidad de pacientes:", len(pacientes))

print("Listado de pacientes:")
for dni in pacientes:
    print("DNI:", dni)
    print("Edad:", pacientes[dni][0])
    print("Sexo:", pacientes[dni][1])
    print("Diabético:", pacientes[dni][2])

dni = int(input("Ingrese el DNI del paciente: "))
if dni in pacientes:
    pacientes[dni][0] += 1
    print("Nueva edad:", pacientes[dni][0])
else:
    print("No existe ese paciente.")


if pacientes[14972142][2] == "Sí":
    print("El paciente 14972142 tiene diabetes.")
else:
    print("El paciente 14972142 no tiene diabetes.")

if pacientes[6409217][2] == "Sí":
    print("El paciente 6409217 tiene diabetes.")
else:
    print("El paciente 6409217 no tiene diabetes.")


suma_edades = 0
cantidad_diabeticos = 0

for dni in pacientes:

    if pacientes[dni][2] == "Sí":
        suma_edades = suma_edades + pacientes[dni][0]
        cantidad_diabeticos = cantidad_diabeticos + 1

if cantidad_diabeticos > 0:
    promedio = suma_edades / cantidad_diabeticos
    print("Edad promedio de pacientes con diabetes:", promedio)



hay_paciente = False

for dni in pacientes:
    if pacientes[dni][0] > 80 and pacientes[dni][2] == "No":
        hay_paciente = True

if hay_paciente:
    print("Existe un paciente mayor de 80 años sin diabetes.")
else:
    print("No existe ningún paciente mayor de 80 años sin diabetes.")
