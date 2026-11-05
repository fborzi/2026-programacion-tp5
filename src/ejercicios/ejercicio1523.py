from funciones import contarPacientes

"""Programa que almacena en una lista de diccionarios los datos
 de los pacientes con DNI,edad,sexo y si es diabetico"""

pacientes = [
    { "DNI": 11412625, "Edad": 60, "Sexo": "Masculino", "Diabetico": True },
    { "DNI": 6409217, "Edad": 65, "Sexo": "Femenino", "Diabetico": False },
    {"DNI": 19172162, "Edad": 45, "Sexo": "Masculino", "Diabetico": False },
    {"DNI": 28141815, "Edad": 34, "Sexo": "Femenino", "Diabetico": True },
    {"DNI": 14972142, "Edad": 58, "Sexo": "Masculino", "Diabetico": True },
    {"DNI": 36843316, "Edad": 23, "Sexo": "Femenino", "Diabetico": False },
]


""" Contar la cantidad de pacientes en la lista y mostrarla por pantalla
"""

print("Cantidad de pacientes:", contarPacientes(pacientes))


"""Listar pacientes con su DNI y demas datos"""

for paciente in pacientes:
    print("DNI:", paciente["DNI"], "Edad:", paciente["Edad"], "Sexo:", paciente["Sexo"], "Diabetico:", paciente["Diabetico"])

"""Solicitar al usuario un DNI e incrementar la edad en 1 del paciente correspondiente"""

dni_paciente = int(input("Ingrese un DNI: "))

for paciente in pacientes:
    if paciente["DNI"] == dni_paciente:
        paciente["Edad"] += 1
        print("DNI:", paciente["DNI"], "Edad:", paciente["Edad"], "Sexo:", paciente["Sexo"], "Diabetico:", paciente["Diabetico"])
        break


"""Indicar si los pacientes con dni 14972142 y 6409217 son diabeticos o no"""
for paciente in pacientes:
    if paciente["DNI"] == 14972142 or paciente["DNI"] == 6409217:
        print("DNI:", paciente["DNI"], "Diabetico:", paciente["Diabetico"])


"""Calcular la edad promedio de los pacientes con diabetes"""
suma_edad = 0
contador = 0

for paciente in pacientes:
    if paciente["Diabetico"]:
        suma_edad += paciente["Edad"]
        contador += 1

if contador > 0:
    edad_promedio = suma_edad / contador
    print("Edad promedio de pacientes con diabetes:", edad_promedio)
else:
    print("No hay pacientes con diabetes.")


"""Comprueba si en el diccionario hay algun paciente con mas de 80 años sin diabetes, decir si hay o no sin imprimir sus datos"""
hay_paciente = False
for paciente in pacientes:
    if paciente["Edad"] > 80 and not paciente["Diabetico"]:
        print(True)
        hay_paciente = True

if not hay_paciente:
    print(False)