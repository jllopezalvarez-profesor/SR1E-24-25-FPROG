"""
Ejercicio 42 - Listas
"""

numeros = [1, 4, 2, 6, 10]

print(f"Lista de números: {numeros}")

suma_for_each = 0
for numero in numeros:
    print(f"Sumando {numero} en for-each")
    suma_for_each += numero
print(f"La suma usando for-each es: {suma_for_each}")

suma_range = 0
for posicion in range(len(numeros)):
    print(f"Sumando {numeros[posicion]} (posicion {posicion}) en for-range")
    suma_range = suma_range + numeros[posicion]
    print(f"La suma vale de momento: {suma_range}")
print(f"La suma usando for-range es: {suma_range}")


print(f"La suma de los valores de la lista con sum() es: {sum(numeros)}")

print(f"La suma de las posiciones pares de la lista con sum() es: {
      sum(numeros[::2])}")
