"""
Ejercicio 02
"""

numero = int(input("Introduce el número: "))

# Primera forma: anidamiento de condicionales
if (numero == 0):
    print("El número es un cero")
else:
    if (numero > 0):
        print("El número es mayor que cero")
    else:
        print("El número es menor que cero")

# Segunda forma if/elif
if (numero == 0):
    print("El número es un cero")
elif (numero > 0):
    print("El número es mayor que cero")
else:
    print("El número es menor que cero")

# tercera forma: if independientes
if (numero == 0):
    print("El número es un cero")
if (numero > 0):
    print("El número es mayor que cero")
if (numero < 0):
    print("El número es menor que cero")
