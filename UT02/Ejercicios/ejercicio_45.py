"""
Ejercicio 45
"""

import random

tam_lista = int(input("Introduce el tamaño de la lista: "))

lista = [random.randint(-10, 10) for _ in range(tam_lista)]

print(lista)

# Cambiar los negativos por un cero usando bucle
for posicion in range(len(lista)):
    if lista[posicion] < 0:
        lista[posicion] = 0

print(lista)

# Cambiar los positivos por 25 usando comprension de listas

lista = [25 if elemento > 0 else elemento for elemento in lista]

print(lista)
