"""

"""


def contar_ocurrencias(lista):
    cuenta = {}

    for elemento in lista:
        if elemento in cuenta:
            cuenta[elemento] += 1
        else:
            cuenta[elemento] = 1

    return cuenta


num_elementos = int(input("Intorduce cuantas cosas vas a poner en la lista."))
lista_cosas = []
for _ in range(num_elementos):
    cosa = input("Introduce un elemento")
    lista_cosas.append(cosa)

print(lista_cosas)

cuenta_cosas = contar_ocurrencias(lista_cosas)

print(cuenta_cosas)
