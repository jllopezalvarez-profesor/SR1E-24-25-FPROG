"""
Primer programa en Python: Operaciones básicas
"""
# Solicitar al usuario el primer número
num1 = input("Introduce el primer número: ")
num1 = float(num1)   # Convertir el valor a número con decimales
# Solicitar al usuario el segundo número
num2 = input("Introduce el segundo número: ")
num2 = float(num2)   # Convertir el valor a número con decimales
# Sumar los dos números
suma = num1 + num2   # Completa con la variable que falta
# Restar los dos números
resta = num1 - num2   # Completa con la variable que falta
# Multiplicar los dos números
multiplicacion = num1 * num2   # Completa con la variable que falta
# Dividir los dos números (Ten en cuenta el divisor no puede ser 0)
division = num1 / num2
divisionEntera = num1 // num2
# Mostrar los resultados
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)   # Puedes probar que pasa si num2 es 0
print("La división entera es:", divisionEntera)   # ¿Es igual que la anterior?
