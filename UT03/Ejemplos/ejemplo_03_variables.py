"""
Ejemplos de variables y temas relacionados
"""

# No se pueden usar palabras reservadas como variables
# Si se descomenta la siguiente línea falla
# elif = input("Escribe algo: ")

# Crear variable y dar un valor
nombre = "José Luis"

# Crear una variable de tipo entero, y darle el valor 10
numero = 10
numero = 20
numero = input("dame un número: ")
print(numero)

# Cambiar el tipo de dato de una variable:
edad = input("Dime tu edad: ")  # "Dime tu edad: " es un literal
edad = int(edad)
print(edad)

# Constante mal escrita, si no cambia valor, debe ser mayúsculas
valor_constante = 4  # MAL
VALOR_CONSTANTE = 4  # Bien - 4 es un literal

# Declarar constante
IVA_GENERAL = 0.21  # Es float, porque tiene decimales
# Usar la contante
precio_sin_iva = 125  # 125 es un literal
precio_con_iva = precio_sin_iva + (precio_sin_iva * IVA_GENERAL)


# Asignaciones compuestas
print("Ejemplos de asignaciones compuestas")
numero = 10
print(numero)
numero += 5  # numero = numero + 5;
print(numero)
numero //= 3  # numero = numero // 3
print(numero)
