"""
Ejercicio 09
Escribir un programa que lea un año e indique si es bisiesto. 
Un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
excepto que también sea divisible por 400. O lo que es lo mismo, si es divisible por 
400, o si es divisible por 4 y no por 100.
Dicho de otra manera, es bisiesto si es divisible por 400 o lo es por 4 pero no por 100.
"""

# Solicitar el año al usuario
anio = int(input("Introduce un año: "))

# Verificar si el año es bisiesto
# Se tiene que cumplir una de las dos condiciones:
# - Divisible por 400
# o
# - Divisible por 4 pero no por 100
if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    print("El año", anio, "es bisiesto.")
else:
    print("El año", anio, "no es bisiesto.")
