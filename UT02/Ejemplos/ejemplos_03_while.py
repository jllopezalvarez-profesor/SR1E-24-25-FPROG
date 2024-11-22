"""
Ejemplos de while
"""

numero = 0
while numero < 10:
    print("En el primer bucle")
    print(numero)
    numero += 1  # Si no ponemos esto no termina el bucle


# Ejemplo de bucle infinito
# numero = 0
# while numero >= 0:
#     print("En el segundo bucle")
#     print(numero)
#     numero += 1  # Si no ponemos esto no termina el bucle


nombre = input("Dime tu nombre: ")
while nombre != "JL":
    print("Nombre equivocado.")
    nombre = input("Dime tu nombre otra vez: ")


print("Fin del programa")
