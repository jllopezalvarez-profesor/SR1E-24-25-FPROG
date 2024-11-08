"""
Ejercicio 06
Programa que lea una cadena de texto por teclado y compruebe si es una letra mayúscula. 
Debe comprobar que es de longitud 1 (sólo una letra), y que esta es mayúscula.
"""

letra_original = input("Introduce una letra mayúscula: ")

# Para calcular la longitud de un string:
longitud = len(letra_original)

# Para convertir algo a mayúsculas
letra_mayusculas = letra_original.upper()

# Comprobamos que es de longitud 1 y que las dos cadenas son iguales
if longitud == 1 and letra_original == letra_mayusculas:
    print(f"'{letra_original}' es una letra mayúscula")
else:
    print(f"'{letra_original}' NO es una letra mayúscula")

# Se puede hacer con expresiones, sin las variables "intermedias"
if len(letra_original) == 1 and letra_original == letra_original.upper():
    print(f"'{letra_original}' es una letra mayúscula")
else:
    print(f"'{letra_original}' NO es una letra mayúscula")
