"""
Ejercicio 04
Crea un programa que pida al usuario dos números y muestre la división del 
primero por el segundo sólo si el segundo no es cero. Si el segundo es cero, 
mostrará un mensaje de aviso indicando que no se puede hacer la operación.
"""

# Podrían ser "float". El problema no especifica
dividendo = int(input("Introduce el primer número (dividendo): "))
divisor = int(input("Introduce el segundo número (divisor): "))

# Comprobamos si el divisor es cero
if divisor == 0:
    print("No se puede realizar la división porque el divisor es cero.")
else:
    # La división puede tener decimales, aunque los operandos sean enteros
    print(f"El resultado de dividir {dividendo} por {
          divisor} es {dividendo / divisor}.")
