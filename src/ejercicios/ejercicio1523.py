pacientes = {
    11412625: [60, "Masculino", "Sí"],
    6409217: [65, "Femenino", "No"],
    19172162: [45, "Masculino", "No"],
    28141815: [34, "Femenino", "Sí"],
    14972142: [58, "Masculino", "Sí"],
    36843316: [23, "Femenino", "No"]
}

print("Cantidad de pacientes:", len(pacientes))


for dni, datos in pacientes.items():
    print("DNI:", dni)
    print("Edad:", datos[0])
    print("Sexo:", datos[1])
    print("Diabético:", datos[2])
    print()


dni = int(input("Ingrese el DNI del paciente: "))

if dni in pacientes:
    pacientes[dni][0] += 1
    print("Nueva edad:", pacientes[dni][0])
else:
    print("No existe un paciente con ese DNI")


for dni in [14972142, 6409217]:
    if pacientes[dni][2] == "Sí":
        print("El paciente", dni, "tiene diabetes")
    else:
        print("El paciente", dni, "no tiene diabetes")


suma_edades = 0
cantidad_diabeticos = 0

for datos in pacientes.values():
    if datos[2] == "Sí":
        suma_edades += datos[0]
        cantidad_diabeticos += 1

promedio = suma_edades / cantidad_diabeticos
print("Edad promedio de pacientes con diabetes:", promedio)

hay_paciente = False

for datos in pacientes.values():
    if datos[0] > 80 and datos[2] == "No":
        hay_paciente = True

if hay_paciente:
    print("Hay pacientes mayores de 80 años sin diabetes")
else:
    print("No hay pacientes mayores de 80 años sin diabetes")
