"""
Ejemplos for
"""

# For de 0 a un número no incluido
print("For de 0 a un número no incluido")
for numero in range(10):
    print(numero)


# For de 10 a un número no incluido
print("For de 10 a un número no incluido")
for numero in range(10, 20):
    print(numero)

# For de 10 a un número negativo no incluido
print("For de 10 a un número no incluido")
for numero in range(10, -10, -1):
    print(numero)


# For de 10 a un número negativo no incluido, de tres en tres
print("For de 10 a un número negativo no incluido, de tres en tres")
for numero in range(10, -10, -3):
    print(numero)


# For que recorre los caracteres de un str
print("Mostrar los caracteres de 'Esto es lo que hay' uno por línea")
cadena = "Esto es lo que hay"
for caracter in cadena:
    print(caracter)
