"""
Ejercicio 46
"""

import random

tamanio_lista = int(input("¿De que tamaño quieres la lista de números? "))

lista = [random.randint(0, 9) for _ in range(tamanio_lista)]

otra_lista = lista[::2]

print(otra_lista)

print(lista)
