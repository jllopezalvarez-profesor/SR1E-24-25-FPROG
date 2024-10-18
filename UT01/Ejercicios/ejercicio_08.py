"""
Ejercicio 08
"""

# Pedir al usuario la temperatura en F
# No olvidar convertir a número con decimales
temp_fahrenheit = input("Introduce la temperatura en grados Fahrenheit: ")
temp_fahrenheit = float(temp_fahrenheit)

# Calcular la temperatura en C
temp_celsius = (temp_fahrenheit - 32) * 5 / 9

# Mostar el resultado
# Lo voy a intentar mostrar con 2 decimales
print(f"{temp_fahrenheit} Fahrenheit son {temp_celsius:.4f} Celsius.")
