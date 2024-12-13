"""
Ejercicio 41 - Listas
"""
#  0
numeros = [12, 17, 12, 9, 8]

print(f"Los números generados son: {numeros}")

print(f"El primer número de la lista es: {numeros[0]}")
print(f"El último número de la lista es: {numeros[len(numeros)-1]}")
print(f"El último número de la lista es: {numeros[-1]}")

# Modificar el tercer elemento (en posición 2)
numeros[2] = 100

print(numeros)
