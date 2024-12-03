"""
Ejemplos de listas
"""

# Crear una lista vacía
lista = []

# añadir algo a la lista
lista.append(123)
print(lista)

lista = lista + ["hola"]
print(lista)


# recorrer lista y mostrar tipo
for elemento in lista:
    print(f"{elemento} - {type(elemento)}")


# Lista de numeros del 100 al 50 (en ese orden)
numeros = list(range(100, 49, -1))
print(numeros)
for num in numeros:
    if num % 7 == 0:
        print(f"el número {num} es multiplo de 7")

# multiplos_7 = [num in range(100) if num % 7 == 0 num]
# print(multiplos_7)


lista_ordenada = []
lista_ordenada.append(2)
lista_ordenada.append(7)
lista_ordenada.append(5)
lista_ordenada.append(1)
print(lista_ordenada)
lista_ordenada.insert(0, 40)
print(lista_ordenada)

lista_ordenada.sort()
print(lista_ordenada)
lista_ordenada[3] = 100
print(lista_ordenada)
lista_ordenada.remove(5)
print(lista_ordenada)
# lista_ordenada.remove(300)
print(lista_ordenada.pop(1))
print(lista_ordenada)
del lista_ordenada[0]
print(lista_ordenada)
