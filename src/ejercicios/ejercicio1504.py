def cargar_nombres():
    lista = []
    nombre = input("ingresa un nombre(blanco para terminar): ")
    
    while nombre != "":
        lista.append(nombre)
        nombre = input("ingresa un nombre(blanco para terminar): ")
        
        return lista
    
def mostrar_lista(lista):
    for elem in lista:
        print(elem)
        
nombres = cargar_nombres()
print("nombres cargados:")
mostrar_lista(nombres)