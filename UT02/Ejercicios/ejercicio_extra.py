"""
Traducir usando un diccionario
"""

traductor = {
    '0': 'cero',
    '1': 'uno',
    '2': 'dos',
    '3': 'tres',
    '4': 'cuatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'siete',
    '8': 'ocho',
    '9': 'nueve'
}


def traducir(texto):
    texto_traducido = ""

    for letra in texto:
        if letra in traductor:
            texto_traducido += traductor[letra]
        else:
            texto_traducido += letra

    return texto_traducido


texto_usuario = input("Introduce un texto")

print(
    f"El texto cambiando números por su 'nombre' es: '{traducir(texto_usuario)}'. ")
