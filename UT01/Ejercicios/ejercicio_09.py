"""
Ejercicio 09
"""

# Pedir al usuario tres números
# No olvidar convertir a número con decimales
primer_num = float(input("Introduce el primer número: "))
segundo_num = float(input("Introduce el segundo número: "))
tercer_num = float(input("Introduce el tercer número: "))

# Calcular la media
media = (primer_num + segundo_num + tercer_num) / 3

# Mostar el resultado
# Lo voy a mostrar con 2 decimales
print(f"La media de {primer_num}, {
      segundo_num} y {tercer_num} es {media:.2f}.")
