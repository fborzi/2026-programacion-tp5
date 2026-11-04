""" ejercicio 1523 registro y consulta de pacientes con diccionariosd

Registra los pacientes en un Diccionario con el DNI como clave y una
lista con edad, sexo y si es diabético como valor. informa la cantidad
de pacientes, los lista, incrementa la edad del paciente con el DNI
ingresado, indica si dos pacientes son diabeticos, calcula la edad
promedio de los diabeticos e indica si hay algún paciente mayor de 80
años sin diabetes.
"""

from funciones import edad_promedio_diabeticos, hay_mayor_sin_diabetes

pacientes: dict = {
    11412625: [60, "Masculino", True],
    6409217: [65, "Femenino", False],
    19172162: [45, "Masculino", False],
    28141815: [34, "Femenino", True],
    14972142: [58, "Masculino", True],
    36843316: [23, "Femenino", False]
}

print(len(pacientes))

for dni in pacientes:
    print(dni, pacientes[dni][0], pacientes[dni][1], pacientes[dni][2])

dni_buscado: int = int(input("Ingrese un DNI: "))
if dni_buscado in pacientes:
    pacientes[dni_buscado][0] += 1
else:
    print("No hay ningun paciente con ese DNI")

print(pacientes[14972142][2], pacientes[6409217][2])
print(edad_promedio_diabeticos(pacientes))
print(hay_mayor_sin_diabetes(pacientes))
