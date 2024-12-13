"""
Ejercicio 44
"""

numeros = list(range(1, 10))
print(numeros)

# Primera: con bucle
for posicion in range(len(numeros)):
    numeros[posicion] = numeros[posicion]**2

print(numeros)

# Segunda: con comprensión de listas
numeros = [numero**2 for numero in numeros]
print(numeros)
