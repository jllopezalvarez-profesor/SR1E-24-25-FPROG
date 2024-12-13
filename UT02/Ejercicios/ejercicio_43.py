"""
Ejercicio 43
"""

# Cómo añadir a una lista
lista = []

# Con append
lista.append("Primera")
print(lista)
# Con + []
lista = lista + ["Segunda"]
# Con insert -- En una posición (p. ej. al principio)
lista.insert(0, "Nuevo primero")
print(lista)


numero_palabras = int(input("Cuántas palabras vas a escribir: "))

# Crear la lista vacía
palabras = []

for _ in range(numero_palabras):
    palabra = input("Introduce una palabra: ")
    # Añadir palabra a la lista
    palabras.append(palabra)

palabras.sort()

for palabra in palabras:
    print(palabra)
