from funciones import borrar_adyacentes

print(borrar_adyacentes(['a', 'a', '*', 'b', '=', '=', 'c', 'a']))  # ['a', '*', 'b', '=', 'c', 'a']
print(borrar_adyacentes(['x', 'x', 'x']))                           # ['x']
print(borrar_adyacentes([]))                                         # []
