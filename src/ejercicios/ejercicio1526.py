# ======================================================
# VERSION A) Sin almacenar las ciudades
# ======================================================
print("--- VERSION A ---")
conteo_paises = {}
total = 0

ciudad = input("Ciudad (zz para terminar): ")
while ciudad.lower() != "zz":
    pais = input("País: ")
    
    total += 1
    conteo_paises[pais] = conteo_paises.get(pais, 0) + 1
    
    ciudad = input("Ciudad (zz para terminar): ")

print(f"\nTotal de ciudades: {total}")
for pais, cant in conteo_paises.items():
    print(f"  {pais}: {cant}")

# ======================================================
# VERSION B) Guardando en lista de listas
# ======================================================
print("\n--- VERSION B ---")
ciudades = []

ciudad = input("Ciudad (zz para terminar): ")
while ciudad.lower() != "zz":
    pais = input("País: ")
    ciudades.append([ciudad, pais])
    
    ciudad = input("Ciudad (zz para terminar): ")

# proceso la lista después
conteo_paises_b = {}
for par in ciudades:
    pais = par[1]
    conteo_paises_b[pais] = conteo_paises_b.get(pais, 0) + 1

print(f"\nTotal de ciudades: {len(ciudades)}")
print(f"Lista: {ciudades}")
for pais, cant in conteo_paises_b.items():
    print(f"  {pais}: {cant}")