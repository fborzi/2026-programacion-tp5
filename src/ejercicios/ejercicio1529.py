"""Este programa solicita al usuario un número entero n y calcula los primeros n términos
de la sucesión Mira y Decí, que comienza con el número 1.
Cada término se construye a partir del anterior, contando cuántas veces
aparece consecutivamente cada dígito y formando un nuevo número.
Finalmente, muestra por pantalla la lista con los términos generados."""


from funciones import sucesion_mira_y_deci

n = int(input("¿Cuántos números querés generar? "))

resultado = sucesion_mira_y_deci(n)

print(resultado)
