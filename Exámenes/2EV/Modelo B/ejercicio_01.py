"""
Solución al ejercicio 1 del modelo B del examen del día 31/01/2025
Autor: José Luis López Álvarez
"""
# Enunciado
# Escribe un programa en python que:
#   - Pida al usuario el tamaño de las listas de numeros que se van a crear.
#   - Guardará este tamaño en una variable tamanio_listas
#   - Cree dos listas de longitud tamanio_listas, llenas de números enteros.
#   - Cada una de estas listas estará llena de números aleatorios, entre - 10 y 10 ambos incluidos.
#   - Muestre las dos listas por pantalla.
#   - Cree una tercera lista y, en cada posición de esta nueva lista guardará, operando con los números de las mismas posiciones de las dos listas originales:
#       - En posiciones pares, el valor será el número de la primera lista menos el de la segunda lista(de las mismas posiciones)
#       - En posiciones impares, el valor será el número de la primera primera lista más el de la segunda(de las mismas posiciones).
# Ver ejemplo de ejecución para más información

import random

tamanio_listas = int(input("Dime de que tamaño deseas crear las listas: "))
primera_lista = [random.randint(-10, 10) for _ in range(tamanio_listas)]
segunda_lista = [random.randint(-10, 10) for _ in range(tamanio_listas)]

print("Primera lista:", primera_lista, sep="\n")
print("Segunda lista:", segunda_lista, sep="\n")

lista_resultados = []
for posicion in range(tamanio_listas):
    resultado = primera_lista[posicion]
    if (posicion % 2) == 0:
        resultado -= segunda_lista[posicion]
    else:
        resultado += segunda_lista[posicion]
    lista_resultados.append(resultado)

print("Resultados:", lista_resultados, sep="\n")
