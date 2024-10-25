"""
Ejercicio 15
"""


# Pedir al usuario cuantas monedas tiene de cada tipo
monedas_2_euros = int(input("¿Cuántas monedas de dos euros tienes? "))
monedas_1_euro = int(input("¿Cuántas monedas de un euro tienes? "))
monedas_50_cts = int(input("¿Cuántas monedas de cincuenta céntimos tienes? "))
monedas_20_cts = int(input("¿Cuántas monedas de veinte céntimos tienes? "))
monedas_10_cts = int(input("¿Cuántas monedas de diez céntimos tienes? "))

# Calcular el número total, en céntimos
total_centimos = 0
total_centimos += monedas_2_euros * 2 * 100
total_centimos += monedas_1_euro * 100
total_centimos += monedas_50_cts * 50
total_centimos += monedas_20_cts * 20
total_centimos += monedas_10_cts * 10

# Calcular el número de euros
euros = total_centimos // 100

# Calcular el número de céntimos que quedan
centimos = total_centimos % 100

# Mostar el resultado
print(f"Tienes {euros} euros y {centimos} céntimos.")
