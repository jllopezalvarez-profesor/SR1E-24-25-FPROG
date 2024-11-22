"""
Ejercicio 21 
Realiza un programa que use un bucle for y muestre todos
los números del 10 al 20, sin incluir el 20. Una línea por cada número.
"""


for numero in range(10, 20):
    print(numero)

# Alternativa en la que ponemos los numeros separados por espacio en la misma línea
for numero in range(10, 20):
    print(numero, end=" ")
