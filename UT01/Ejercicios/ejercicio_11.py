"""
Ejercicio 11
"""

# Pedir al usuario el número importe de la compra antes de descuento
importe_inicial = float(
    input("Introduce el importe de la compra antes del descuento: "))

# Constante para el descuento
DESCUENTO = 0.15

# Calcular el importe del descuento
importe_descuento = importe_inicial * DESCUENTO

# Calcular el importe final. Puede hacerse con una resta o multiplicando
importe_final = importe_inicial - importe_descuento  # primera forma
importe_final = importe_inicial * (1-DESCUENTO)  # otra forma

# Mostar el resultado
print(f"El importe final a pagar es de {importe_final}")
