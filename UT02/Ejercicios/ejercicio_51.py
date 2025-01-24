"""
Ejercicio 50
"""
import random

longitud_lista = int(input("Dime la cantidad de números a generar: "))

lista = [random.randint(0, 9) for _ in range(longitud_lista)]

print("La lista antes de eliminar los números pares:", lista, sep="\n")

ultima_posicion_lista = len(lista)-1

for posicion in range(len(lista)-1, -1, -1):
    if lista[posicion] % 2 == 0:
        del lista[posicion]

print("La lista tras eliminar los números pares:", lista, sep="\n")
