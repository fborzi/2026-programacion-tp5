"""
En este ejercicio, se lista y se cuenta los pacientes registrados, se puede modificar
la edad de un paciente seleccionado. Se puede consultar si un determinado paciente tiene
diabetes y calcula el promedio de los pacientes diabeticos.
"""

pacientes = {
    11412625: {"edad": 60, "sexo": "Masculino", "diabetico": True},
    6409217: {"edad": 65, "sexo": "Femenino", "diabetico": False},
    19172162: {"edad": 45, "sexo": "Masculino", "diabetico": False},
    28141815: {"edad": 34, "sexo": "Femenino", "diabetico": True},
    14972142: {"edad": 58, "sexo": "Masculino", "diabetico": True},
    36843316: {"edad": 23, "sexo": "Femenino", "diabetico": False}
}

print("Cantidad de pacientes:", len(pacientes))
for dni, datos in pacientes.items():
    print(dni, datos)

dni = int(input("DNI del paciente cuya edad desea incrementar: "))
if dni in pacientes:
    pacientes[dni]["edad"] += 1
    print("Edad actualizada:", pacientes[dni]["edad"])
else:
    print("No existe ese DNI")

for dni in (14972142, 6409217):
    if dni in pacientes:
        print(f"Paciente {dni} diabético:", "Sí" if pacientes[dni]["diabetico"] else "No")

edades_diabeticos = [p["edad"] for p in pacientes.values() if p["diabetico"]]
print("Edad promedio de pacientes diabéticos:",
      sum(edades_diabeticos) / len(edades_diabeticos) if edades_diabeticos else 0)

hay_mayor_sin_diabetes = any(p["edad"] > 80 and not p["diabetico"] for p in pacientes.values())
print("¿Hay algún paciente mayor de 80 sin diabetes?:", hay_mayor_sin_diabetes)