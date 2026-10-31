def borrar_adyacentes(lista):
    if not lista:
        return []

    resultado = [lista[0]]

    for char in lista[1:]:
        if char != resultado[-1]:
            resultado.append(char)
    
    return resultado

# Ejemplos:
print(borrar_adyacentes(['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']))
# -> ['a', 'b', 'c', 'a']

print(borrar_adyacentes(['a', 'a', 'a', 'a']))
# -> ['a']

print(borrar_adyacentes(['a', 'b', 'c']))
# -> ['a', 'b', 'c']

print(borrar_adyacentes([]))
# -> []