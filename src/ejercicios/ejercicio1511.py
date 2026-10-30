"""
Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
Recorre una lista y agrupa los elementos iguales que aparecen uno detrás de otro.
Para cada grupo, devuelve el elemento y la cantidad de veces que se repite consecutivamente.
La función compara cada elemento con el último grupo registrado. Si coincide, aumenta el contador;
si es diferente, crea un grupo nuevo.
"""

from funciones import ocurrencias

lista = ['z', 7, True, True, 34, 'z', 'z', 'z', 3.14]
print(ocurrencias(lista))
