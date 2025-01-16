"""
Repaso de listas
"""

lista_vacia = []
print(f"El tipo de la variable lista_vacia es {type(lista_vacia)}")

print(lista_vacia)

lista_de_caracteres = list("Hola, esto es una frase")

print(lista_de_caracteres)

lista_con_elementos = [2, "hola", 342.45]

print(lista_con_elementos)

lista = []
lista.append(2)
lista.append(4)
print(lista)
lista.insert(0, 0)
lista.insert(30, 100)
print(lista)
lista.append([2, 4, 5, 6])
print(lista)
lista.extend([2, 3, 4, 5])
print(lista)
lista2 = lista
print(lista2)
lista3 = lista.copy()
print(lista3)
lista4 = lista[:]
print(lista4)
lista5 = lista[::2]
print(lista5)
lista.clear()
print("lista tras clear:", lista)
print("lista2 tras clear:", lista2)
print("lista3 tras clear:", lista3)
print("lista4 tras clear:", lista4)
print("lista5 tras clear:", lista5)

if 7 in lista5:
    print("El 7 está en la lista")
else:
    print("El 7 no está en la lista")

print("Recorrido en orden normal iterando:")
for elemento in lista5:
    print("Elemento: ", elemento)

print("Recorrido en orden normal por índice:")
for indice in range(len(lista5)):
    print(f"Elemento en posición {indice}: {lista5[indice]}")

print("Recorrido en orden inverso por índice:")
for indice in range(len(lista5)-1, -1, -1):
    print(f"Elemento en posición {indice}: {lista5[indice]}")
