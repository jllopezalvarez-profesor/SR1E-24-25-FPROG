"""
Ejercicio 50
"""
import random

longitud_lista = int(input("Dime la cantidad de números a generar: "))

lista = [random.randint(0, 9) for _ in range(longitud_lista)]

# #         0   1   2   3   4
# lista = [10, 20, 30, 40, 50]

lista_copia_impares = lista[1::2]
print("La copia de la lista es: ", lista_copia_impares, sep="\n")

print("La lista antes de eliminar posiciones pares:", lista, sep="\n")

ultima_posicion_lista = len(lista)-1

for posicion in range(len(lista)-1, -1, -1):
    if (posicion % 2 == 0):
        del lista[posicion]

print("La lista tras eliminar posiciones pares:", lista, sep="\n")
