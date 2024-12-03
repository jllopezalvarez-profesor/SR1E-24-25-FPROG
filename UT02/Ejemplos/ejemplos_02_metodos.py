"""
Ejemplos de llamadas a métodos
"""

# Uso una función para pedir un string
nombre = input("Dime tu nombre: ")

# Método de str que devuelve la misma cadena en mayúsculas:
print(nombre.upper())

# Método de str que devuelve la misma cadena en minúsculas:
print(nombre.lower())

# Llamar a un método de str no cambia el valor de la cadena
print(nombre)

numero = float(input("Introduce un número"))

# Los métodos de int son distintos a los de str
print(numero.is_integer())
