# Ejercicio 1522 gestion de poblacion de ciudades con diccionarios

"""Este archivo importa las funciones necesarias desde funciones.py cuando corresponde,
utiliza los datos de la consigna y muestra los resultados solicitados.
No se redefinen aquí las funciones compartidas.
"""

from funciones import cargar_socios

socios = cargar_socios()
print("Cantidad de socios:", len(socios))
print("Cantidad de socios morosos:",
      sum(1 for socio in socios.values() if not socio["cuota_al_dia"]))

dni_buscar = "25123555"
if dni_buscar in socios:
    print("Socio:", socios[dni_buscar]["nombre"], socios[dni_buscar]["apellido"])
else:
    print("No existe un socio con DNI", dni_buscar)

socios["40151724"] = {"nombre": "Esteban", "apellido": "Quito",
                      "edad": 17, "cuota_al_dia": True}
mayor = max(socios.items(), key=lambda item: item[1]["edad"], default=None)
print("Socio de mayor edad:", mayor)

dni_baja = "15188125"
if dni_baja in socios:
    if socios[dni_baja]["cuota_al_dia"]:
        del socios[dni_baja]
        print("Socio dado de baja.")
    else:
        print("No se puede dar de baja: tiene cuota pendiente.")
else:
    print("No existe el socio para dar de baja.")

if "28731431" in socios:
    socios["28731431"]["cuota_al_dia"] = True
    print("Cuota registrada como paga.")
else:
    print("No existe el socio con DNI 28731431.")

