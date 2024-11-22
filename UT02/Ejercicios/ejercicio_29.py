"""
Ejercicio 29

Crea un programa que pida números enteros positivos hasta que se 
introduzca un cero. Debe calcular la suma y la media de todos los 
números introducidos. Si el usuario introduce un número menor que 
cero, debe mostrar un mensaje indicando que no es válido y no 
tenerlo en cuenta para el cálculo.
"""

terminar = False
suma = 0
cuenta = 0

while not terminar:
    numero = int(
        input("Introduce un número entero positivo, o cero para terminar: "))
    if numero == 0:
        terminar = True
    elif numero < 0:
        print("Error: el número introducido es menor que cero.")
    else:
        suma += numero
        cuenta += 1

print(f"La suma de los numeros mayores que cero es {
      suma} y la media es {(suma / cuenta): .2f}.")
print(f"La media sin decimales (truncando) es {suma // cuenta}")
print(f"La media sin decimales (convertido a int) es {int(suma / cuenta)}")
print(f"La media sin decimales (redondeado) es {round(suma / cuenta)}")
