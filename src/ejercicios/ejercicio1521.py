lineas = []
while True:
    linea = input()
    lineas.append(linea)
    if linea.endswith(''):
        break

texto = " ".join(lineas)
if texto.endswith(''):
    texto = texto[:-1]

palabras_limpias = []
for p in texto.split():
    palabra = "".join(c for c in p if c.isalnum())
    if palabra:
        palabras_limpias.append(palabra)

vocal_map = str.maketrans("áéíóúüÁÉÍÓÚÜ", "aeiouuaeiouu")
palabras_3_vocales = []
for p in palabras_limpias:
    p_norm = p.translate(vocal_map).lower()
    vocales_distintas = set(c for c in p_norm if c in "aeiou")
    if len(vocales_distintas) >= 3:
        palabras_3_vocales.append(p)

oraciones_raw = texto.split('. ')
oraciones = [o.strip() for o in oraciones_raw if o.strip()]

cant_oraciones = len(oraciones)
oraciones_mas_5_palabras = 0
for o in oraciones:
    cant_palabras = len(o.split())
    if cant_palabras > 5:
        oraciones_mas_5_palabras += 1

porcentaje_mas_5 = (oraciones_mas_5_palabras / cant_oraciones * 100) if cant_oraciones > 0 else 0

print("a. Palabras con al menos 3 vocales diferentes:", palabras_3_vocales)
print("b. Cantidad de oraciones en el texto:", cant_oraciones)
print(f"c. Porcentaje de oraciones con más de 5 palabras: {porcentaje_mas_5:.2f}%")