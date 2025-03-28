"""
Función extraer_primos
"""

from math import sqrt, ceil
from random import randint


def es_primo(num):
    # No es número, o es <= 1
    if not isinstance(num, int) or num <= 1:
        return False

    # El 2 es el único par primo
    if num == 2:
        return True

    # Cualquier otro par no es primo, porque es divisible por 2
    if num % 2 == 0:
        return False

    # Como hemos descartado el 2 como factor, podemos saltar (no comprobar) los pares
    # Para optimizar, se puede llegar a num/2, o mejor aún a math.sqrt(num)
    # Como la raíz de un número puede tener decimales se redondea hacia arriba (ceiling)
    for divisor in range(3, ceil(sqrt(num))+1, 2):
        if num % divisor == 0:
            return False

    return True


def extraer_primos(lista):
    lista_primos = []
    for numero in lista:
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos


tamanio_lista = int(input("¿Cuántos números quieres generar? "))

lista_numeros = [randint(1, 20) for _ in range(tamanio_lista)]

print(f"Números generados: {lista_numeros}")
lista_numeros_primos = extraer_primos(lista_numeros)
print(f"Números primos encontrados: {lista_numeros_primos}")
print(f"Números generados, después de buscar primos: {lista_numeros}")
