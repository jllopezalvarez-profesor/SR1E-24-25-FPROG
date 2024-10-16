"""
Ejemplos de uso de print
"""

# Print con un literal
# Un literal es un texto o un número que aparece
# en el código fuente, y que no es una variable,
# palabra reservada, método, operador, etc.
# En este caso, el literal es string (cadena de
# texto), rodeada de dobles comillas
print("Esto es una cadena de texto literal")

# Print con otro tipo de literal.
# En este caso el literal es un número entero.
print(345)

# Print con variables y constantes
# NUMERO se escribe en mayúsculas porque es
# una constante, no cambia nunca
NUMERO = 234.45
print(NUMERO)

# Distintas llamadas a print
print("uno")
print("dos")
print("tres")

# Print con varios valores en la misma llamada
# Separa los distintos elementos con un separador
# El separador por defecto es el espacio, pero puede cambiarse
# Al final de los elementos escribe un finalizador
# El finalizador por defecto es el salto de línea (\n),
# pero puede cambiarse
print("uno", "dos", "tres")

# Print con varios valores, y con un separador especial (guion),
# distinto del separador por defecto (espacio)
print("uno", "dos", "tres", sep="-")

# Print con varios valores, y un terminador especial (una frase),
# que incluye el caracter de escape \n
print("uno", "dos", "tres", end="Esto es el final\n")

# Print combinando un separador especial (guion)
# y  un terminador especial (exclamación y salto de línea)
print("uno", "dos", "tres", sep="-", end="!\n")

# En las cadenas (str) se pueden incluir caracteres especiales.
# Caracter especial de salto de línea
print("Esto es la linea 1\nEsto es la linea 2\n\nEsto es la tres separada dos líneas")

# Escapado de comillas
print("Ahora voy a escribir una comilla doble (\") en medio del texto")

# Uso de comilla simple para evitar escapes
print('Ahora puedo usar la comilla doble todo lo que quiera " porque está delimitado con simples')
