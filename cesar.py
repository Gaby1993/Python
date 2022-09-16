# Cesar



def codificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)
        alfabeto_a_usar = alfabeto
        limite = 97 
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto

        codificado += alfabeto_a_usar[posicion]
    return codificado


def decodificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    decodificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            decodificado += letra
            continue
        valor_letra = ord(letra)
        alfabeto_a_usar = alfabeto
        limite = 97  
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_letra - limite - rotaciones) % longitud_alfabeto

        decodificado += alfabeto_a_usar[posicion]
    return decodificado


mensaje = "My name is Gaby"
print("El mensaje original es: ", mensaje)
rotaciones = 1
codificado = codificar(mensaje, rotaciones)
print("Codificado es: ", codificado)
decodificado = decodificar(codificado, rotaciones)
print("Descodificado es: ", decodificado)