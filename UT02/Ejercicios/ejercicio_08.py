"""
Ejercicio 08
Escribe un programa que pida tres números y los muestre ordenados (de mayor a menor);
"""

# Solicitar los tres números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))


if num1 >= num2 and num1 >= num3:
    # Primer caso: num1 es el mayor de los tres
    # Sólo queda ver cuál de los dos restantes (num2, num3) es mayor
    if num2 >= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    # Segundo caso: num2 es el mayor de los tres
    # Sólo queda ver cuál de los dos restantes (num1, num3) es mayor
    if num1 >= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    # Tercer caso: num3 es el mayor de los tres
    # Sólo queda ver cuál de los dos restantes (num1, num2) es mayor
    if num1 >= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
