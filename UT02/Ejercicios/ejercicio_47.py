"""
Ejercicio 46
"""

import random

tamanio_lista = int(input("¿De que tamaño quieres la lista de números?"))

lista = []
for _ in range(tamanio_lista):
    num = random.randint(0, 9)
    lista.append(num)

print(lista)

print("El tamaño de la lista es", len(lista), "elementos")

# Ejemplo de diferencia entre posición y valor dentro de una posición de la lista
for posicion in range(len(lista)):
    print("En la posición", posicion)
    print("¿Es posicion par?", "SI" if (posicion % 2) == 0 else "NO")
    valor = lista[posicion]
    print(f"El valor de la posicion {posicion} es {valor}.")
    print("¿El valor es par?", "SI" if valor % 2 == 0 else "NO")
    print("------------------")

lista_pares = []
for valor in lista:
    if valor % 2 == 0:
        lista_pares.append(valor)


print(lista_pares)

print(lista)
