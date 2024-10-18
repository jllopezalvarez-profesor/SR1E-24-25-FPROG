"""
Ejercicio 07
"""

# Leemos del usuario el primer lado, y lo guardamos en una variable
primer_lado = float(input("Introduce un lado del rectángulo: "))

# Leemos del usuario el segundo lado, y lo guardamos en una variable
segundo_lado = float(input("Introduce el otro lado del rectángulo: "))

# Calculamos el perímetro multiplicando por dos la suma de los lados
perimetro = (primer_lado + segundo_lado) * 2

# Calculamos el área multiplicando lado por lado.
area = primer_lado * segundo_lado

# Muestro el resultado
print(f"En un rectangulo con lados {primer_lado} y {segundo_lado} el perímetro es {
      perimetro} y el área es {area}")
