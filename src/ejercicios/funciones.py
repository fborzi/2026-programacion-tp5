def minimo_elemento(lista):
        menor = 4
        for i in lista:
            if menor > i:
                menor = i
                
        return menor 

def piedra_papel_tijera(uno, dos):
    
    uno = uno.lower()
    dos = dos.lower()

    
    if uno == dos:
        return 0

  
    elif (uno == 'piedra' and dos == 'tijera') or \
         (uno == 'tijera' and dos == 'papel') or \
         (uno == 'papel' and dos == 'piedra'):
        return 1

   
    else:
        return 2


def borrar_adyacentes(lista):
    resultado = []          

    for elemento in lista:
       
        if len(resultado) == 0 or elemento != resultado[-1]:
            resultado.append(elemento)

    return resultado



def suma_digitos(numero: int) -> int:
    """Devuelve la suma de los dígitos de un número entero."""


    if numero < 0:
        numero = -numero

    suma = 0
    while numero > 0:
        ultimo_digito = numero % 10
        suma = suma + ultimo_digito
        numero = numero // 10

    return suma



def sumatoria_digitos(lista):
    resultado = []

    for numero in lista:
        resultado.append(suma_digitos(numero))

    return resultado
