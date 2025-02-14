"""
Ejemplos de conjuntos
"""

import random

lista_numeros = [random.randint(1, 9) for _ in range(30)]

print(lista_numeros)

conjunto_numeros = set(lista_numeros)

print(conjunto_numeros)

numero = int(input("Introduce un número, 0 para terminar "))

while numero != 0:
    if (numero not in conjunto_numeros):
        print("El número no esta entre lso generados")
    else:
        print("Has acertado uno de los números")
    numero = int(input("Introduce un número, 0 para terminar "))
