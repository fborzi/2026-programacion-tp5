pacientes = {
    "11.412.625": {"edad": 60, "sexo": "Masculino", "diabetico": True},
    "6.409.217":  {"edad": 65, "sexo": "Femenino",  "diabetico": False},
    "19.172.162": {"edad": 45, "sexo": "Masculino", "diabetico": False},
    "28.141.815": {"edad": 34, "sexo": "Femenino",  "diabetico": True},
    "14.972.142": {"edad": 58, "sexo": "Masculino", "diabetico": True},
    "36.843.316": {"edad": 23, "sexo": "Femenino",  "diabetico": False}
}

print("a. Cantidad de pacientes registrados:", len(pacientes))

print("b. Listado de todos los pacientes:")
for dni, datos in pacientes.items():
    print(f"  DNI: {dni} -> Edad: {datos['edad']}, Sexo: {datos['sexo']}, Diabético: {datos['diabetico']}")

dni_ingresado = input("c. Ingresá un DNI para incrementar su edad en 1: ").strip()
if dni_ingresado in pacientes:
    pacientes[dni_ingresado]["edad"] += 1
    print(f"  Nueva edad de {dni_ingresado}: {pacientes[dni_ingresado]['edad']}")

print("d. ¿14.972.142 sufre diabetes?:", pacientes.get("14.972.142", {}).get("diabetico", False))
print("   ¿6.409.217 sufre diabetes?:", pacientes.get("6.409.217", {}).get("diabetico", False))

edades_diabeticos = [d["edad"] for d in pacientes.values() if d["diabetico"]]
promedio_edad = sum(edades_diabeticos) / len(edades_diabeticos) if edades_diabeticos else 0
print(f"e. Edad promedio de pacientes con diabetes: {promedio_edad:.2f}")

existe_mayor_80_sin_diab = any(d["edad"] > 80 and not d["diabetico"] for d in pacientes.values())
print("f. ¿Existe algún paciente mayor de 80 años sin diabetes?:", existe_mayor_80_sin_diab)