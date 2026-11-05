""" Conteo y agrupacion de ciudades por pais """
total_ciudades = 0
conteo_por_pais = {}

ciudad = input("Ingrese el nombre de la ciudad ('zz' para terminar): ")

while ciudad.lower() != "zz":
    pais = input(f"¿país al que pertenece {ciudad}?: ")
    total_ciudades += 1
    
    if pais in conteo_por_pais:
        conteo_por_pais[pais] += 1  
    else:
        conteo_por_pais[pais] = 1     
    ciudad = input("Ingrese el nombre de la ciudad ('zz' para terminar): ")

print(f"\n--- RESULTADOS (Versión A) ---")
print(f"Cantidad total de ciudades ingresadas: {total_ciudades}")
print("Ciudades por país:")
for pais, cantidad in conteo_por_pais.items():
    print(f"- {pais}: {cantidad}")



listado_completo = []


ciudad = input("Ingrese el nombre de la ciudad ('zz' para terminar): ")

while ciudad.lower() != "zz":
    pais = input(f"¿A qué país pertenece {ciudad}?: ")
    listado_completo.append([ciudad, pais])
    ciudad = input("Ingrese el nombre de la ciudad ('zz' para terminar): ")

total_ciudades = len(listado_completo) 
conteo_por_pais = {}

for elemento in listado_completo:
    pais = elemento[1]
    
    if pais in conteo_por_pais:
        conteo_por_pais[pais] += 1
    else:
        conteo_por_pais[pais] = 1

print("\n--- RESULTADOS (Versión B) ---")
print(f"Cantidad total de ciudades ingresadas: {total_ciudades}")
print("Ciudades por país:")
for pais, cantidad in conteo_por_pais.items():
    print(f"- {pais}: {cantidad}")
