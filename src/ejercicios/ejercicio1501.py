"""
Importamos las funciones creadas en funcione.py, creamos
la lista indicada del ejercicio y guardamos los elementos
que queremos comprobar. Se hace el recorrido para verificar
si pertenece y se muestra el elemento y el resultado obtenido.
Luego buscamos el indice de la lista interna y mostramos la posicion.
"""
from funciones import pertenece, buscar_indice

b = [4, "palabra", [0,1], 9.6, False ]

elementos= [9.6, 0, False, [0,1], 4.0, "p"]

for elemento in elementos:
    resultado = pertenece(b, elemento)
    print(elemento, "pertenece a la lista: ", resultado)

    indice = buscar_indice(b, [0,1])
    print("Índice del elemento [0,1]: ", indice)
    