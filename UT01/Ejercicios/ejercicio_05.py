"""
Ejercicio 05
"""

# Leemos del usuario el lado, y lo guardamos en una variable
# Como input SIEMPRE devuelve texto, lo convertimos a un número
# con decimales con float(.....). Sin decimales sería con int(....)
lado = float(input("Introduce el lado del cuadrado: "))

# Calculamos el perímetro multiplicando el lado por cuatro
perimetro = lado * 4

# Mostramos el resultado de calculat el perímetro
print("El perímetro del cuadrado es ", perimetro, ".")

# Calculamos el área elevando al cuadrado.
# Se podría haber hecho multiplicando lado por lado
area = lado ** 2

# Mostramos el área
print("El área del cuadrado es ", area, ".")

# Forma alternativas, para mostrar los resultados con la forma
# "En un cuadrado de lado ... el perímetro es ... y el área es ..."

print("En un cuadrado de lado ... el perímetro es ... y el área es ...")

print("En un cuadrado de lado", lado, "el perímetro es",
      perimetro, "y el área es", area, ".")


print(f"En un cuadrado de lado {lado} el perímetro es {
      perimetro} y el área es {area}")
