"""
Ejercicio 03
Escribe un programa que lea un número e indique si es par o impar. 
El resto de la división entera (o módulo) de un número entre dos 
es cero si es par, y uno si es impar.
"""

numero = int(input("Introduce un número: "))

# % es el resto de la división entera.
# El resultado de 4 % 2 es cero, y el de 5 % 2 es uno.
if (numero % 2) == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
