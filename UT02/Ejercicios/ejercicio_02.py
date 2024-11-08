"""
Ejercicio 02
Escribir un programa que pida un número y diga si es positivo, negativo o 0.
"""

numero = int(input("Introduce un número: "))

# Primera forma: anidamiento de condicionales
if numero == 0:
    print("El número es un cero")
else:
    if numero > 0:
        print("El número es mayor que cero")
    else:
        print("El número es menor que cero")

# Segunda forma: if/elif
if numero == 0:
    print("El número es un cero")
elif numero > 0:
    print("El número es mayor que cero")
else:
    print("El número es menor que cero")

# Tercera forma: if independientes.
# Se puede hacer porque los tes casos (mayor, menor, o igual a cero)
# son independientes. Nunca se pueden dar dos de ellos a la vez.
if numero == 0:
    print("El número es un cero")
if numero > 0:
    print("El número es mayor que cero")
if numero < 0:
    print("El número es menor que cero")
