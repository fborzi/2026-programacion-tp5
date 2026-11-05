"""Conteo de elementos en una lista"""

L = [5, 6, [9, 5], 2, 5]

""""Instruccion para evaluar cada elemento de la lista y verificar si es 5 o si es una lista"""

total_cincos = sum(el.count(5) if isinstance(el, list) else (1 if el == 5 else 0) for el in L)

print(total_cincos)  