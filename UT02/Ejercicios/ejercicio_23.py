"""
Ejercicio 23
"""

inicio = int(input("Introduce el número inicial: "))
final = int(input("Introduce el número final: "))

if not (inicio <= final):
    print("El inicio tiene que ser menor o igual al final")
else:
    for numero in range(inicio, final+1):
        print(numero, end=" ")
