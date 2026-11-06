nombres = []

print("Ingresa nombres uno por uno. Presiona Enter sin escribir nada para terminar.")

while True:
    nombre = input("Ingresa un nombre: ").strip()
    
    if nombre == "":
        break
    
    nombres.append(nombre)

print("\n--- Lista de nombres ingresados ---")
for nombre in nombres:
    print(nombre)