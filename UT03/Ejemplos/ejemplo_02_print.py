"""
Ejemplos de uso de print
"""

# Print con un literal (con una cadena de texto)
print("Esto es una cadena de texto literal")

# Print con un literal (un número)
print(345)

# Print con variables
NUMERO = 234.45
print(NUMERO)

# Print con varios valores en distintas llamadas
print("uno")
print("dos")
print("tres")

# Print con varios valores en la misma llamada
print("uno", "dos", "tres")

# Print con vario valores, y con un separador especial
print("uno", "dos", "tres", sep="-")

# Print con un terminador especial, que incluye el caracter de escape \n
print("uno", "dos", "tres", end="Esto es el final\n")

# Print con un separador y con un terminador especiales
print("uno", "dos", "tres", sep="-", end="!\n")

# Caracter especial de salto de línea
print("Esto es la linea 1\nEsto es la linea 2\n\nEsto es la tres separada dos líneas")

# Escapado de comillas
print("Ahora voy a escribir una comilla doble (\") en medio del texto")

# Uso de comilla simple para evitar escapes
print('Ahora puedo usar la comilla doble todo lo que quiera " porque está delimitado con simples')
