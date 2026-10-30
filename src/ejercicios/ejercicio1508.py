from funciones import piedra_papel_tijera

print(piedra_papel_tijera('piedra', 'tijera'))   # 1
print(piedra_papel_tijera('Papel', 'TIJERA'))    # 2
print(piedra_papel_tijera('papel', 'piedra'))    # 1
print(piedra_papel_tijera('Tijera', 'tijera'))   # 0
