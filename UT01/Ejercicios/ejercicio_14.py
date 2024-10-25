"""
Ejercicio 14
"""

# Pedir al usuario los dos números enteros
numero_a = int(input("Introduce el primer número: "))
numero_b = int(input("Introduce el segundo número: "))

# Mostrar números
print(f"A vale {numero_a} y B vale {numero_b}.")

# Intercambiar números. Se necesita una variable auxiliar
aux = numero_a
numero_a = numero_b
numero_b = aux

# Mostar el resultado
print(f"A vale {numero_a} y B vale {numero_b}.")
