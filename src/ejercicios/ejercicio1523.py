"""Registra pacientes mediante un diccionario, utilizando el DNI como
clave y un diccionario interno para almacenar edad, sexo y diabetes.

El programa:
- Cuenta y lista los pacientes registrados.
- Solicita un DNI e incrementa la edad del paciente.
- Consulta si dos pacientes específicos tienen diabetes.
- Calcula la edad promedio de los pacientes diabéticos.
- Indica si existe algún paciente mayor de 80 años sin diabetes."""


from funciones import (
    contar_pacientes,
    listar_pacientes,
    incrementar_edad,
    tiene_diabetes,
    promedio_edad_diabeticos,
    existe_mayor_80_sin_diabetes
)

pacientes = {
    11412625: {"edad": 60, "sexo": "Masculino", "diabetico": True},
    6409217: {"edad": 65, "sexo": "Femenino", "diabetico": False},
    19172162: {"edad": 45, "sexo": "Masculino", "diabetico": False},
    28141815: {"edad": 34, "sexo": "Femenino", "diabetico": True},
    14972142: {"edad": 58, "sexo": "Masculino", "diabetico": True},
    36843316: {"edad": 23, "sexo": "Femenino", "diabetico": False}
}


print("Cantidad de pacientes:", contar_pacientes(pacientes))


print("\nListado de pacientes:")
listar_pacientes(pacientes)


dni = int(input("\nIngresá el DNI del paciente: "))

if incrementar_edad(pacientes, dni):
    print("Edad actualizada:", pacientes[dni]["edad"])
else:
    print("No se encontró el paciente.")

# d. Consultar si los pacientes tienen diabetes
print("\nConsulta de diabetes:")

for dni in [14972142, 6409217]:
    resultado = tiene_diabetes(pacientes, dni)

    if resultado:
        print(dni, "tiene diabetes.")
    else:
        print(dni, "no tiene diabetes.")


print(
    "\nPromedio de edad de pacientes con diabetes:",
    promedio_edad_diabeticos(pacientes)
)


if existe_mayor_80_sin_diabetes(pacientes):
    print("Existe un paciente mayor de 80 años sin diabetes.")
else:
    print("No existe ningún paciente mayor de 80 años sin diabetes.")
