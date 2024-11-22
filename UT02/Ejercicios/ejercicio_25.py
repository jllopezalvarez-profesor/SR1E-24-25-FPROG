"""
Ejercicio 25 - Iterativas
"""

numero = int(input("¿De qué número quieres generar la tabla de multiplicar? "))

for otro_numero in range(1, 11):
    print(f"{numero} x {otro_numero} = {numero * otro_numero}")
