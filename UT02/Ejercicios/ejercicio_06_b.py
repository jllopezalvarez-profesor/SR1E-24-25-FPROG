"""
Ejercicio 06
Programa que lea una cadena de texto por teclado y compruebe si es una letra mayúscula. 
Debe comprobar que es de longitud 1 (sólo una letra), y que esta es mayúscula.
Versión alternativa que usa el método isupper. No hemos visto métodos todavía, pero 
los veremos dentro de poco 
"""

letra = input("Introduce una letra mayúscula: ")

# Para calcular la longitud de un string:
longitud = len(letra)

# Comprobamos que es de longitud 1 y que las dos cadenas son iguales
if longitud == 1 and letra.isupper():
    print(f"'{letra}' es una letra mayúscula")
else:
    print(f"'{letra}' NO es una letra mayúscula")
