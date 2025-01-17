"""
Ejercicio 46
"""

import random

tamanio_lista = int(input("¿De que tamaño quieres la lista de números?"))

# lista = [random.randint(-10, 10) for _ in range(tamanio_lista)]
lista = []
for _ in range(tamanio_lista):
    num = random.randint(0, 9)
    lista.append(num)
    # lista.append(random.randint(0, 9))

print(lista)

otra_lista = []
for posicion in range(len(lista)):
    if (posicion % 2) == 0:
        otra_lista.append(lista[posicion])

print(otra_lista)

print(lista)
