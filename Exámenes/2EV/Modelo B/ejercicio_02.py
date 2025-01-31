"""
Solución al ejercicio 2 del modelo B del examen del día 31/01/2025
Autor: José Luis López Álvarez
"""

# Enunciado
# Escribe un programa en python que:
#   - Pida al usuario dos números, numero_mayor y numero_menor.
#   - Se debe cumplir que numero_mayor > numero_menor. Si no lo es, se informará del problema.
#   - Mientras que no se cumpla la condición anterior, se debe informar del problema y volver a preguntar al usuario los dos números
#   - Cuando el usuario haya escrito bien los números, se mostrarán:
#   - Números del mayor al menor(en orden descendente), ambos incluidos. En una sola línea, separados por un espacio.
#   - Números del menor al mayor(en orden ascendente), ambos incluidos. En una sola línea, separados por un espacio.
#   - No se pueden usar listas, conjuntos, o diccionarios en este ejercicio


print("Necesito que me digas dos números, uno mayor que otro.")
numero_mayor = int(input("Dime el mayor de los dos números: "))
numero_menor = int(input("Dime el menor de los dos números: "))

while numero_menor >= numero_mayor:
    print(f"El número {numero_menor} es mayor o igual que {
          numero_mayor}. Vuelve a intentarlo.")
    numero_mayor = int(input("Dime el mayor de los dos números: "))
    numero_menor = int(input("Dime el menor de los dos números: "))

print(f"Los números del {numero_mayor} al {
      numero_menor} ambos incluidos son: ")
for numero in range(numero_mayor, numero_menor-1, -1):
    print(numero, end=" ")
print()

print(f"Los números del {numero_menor} al {
      numero_mayor} ambos incluidos son: ")
for numero in range(numero_menor, numero_mayor+1):
    print(numero, end=" ")
print()
