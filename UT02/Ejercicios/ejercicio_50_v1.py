"""
Ejercicio 50
"""
#         0   1   2   3   4
lista = [10, 20, 30, 40, 50]

print("La lista antes de eliminar posiciones pares:", lista, sep="\n")

for posicion in range(len(lista)):
    print(lista[posicion])

# Esto falla porque el tamaño de la lista cambia
# a medida que eliminamos. SSi inicialmente tiene 5,
# el range(len(lista)) nos lleva de 0..4, pero si
# se reduce a tres, debería ser de 0..2
for posicion in range(len(lista)):
    if (posicion % 2 == 0):
        del lista[posicion]

print("La lista tras eliminar posiciones pares:", lista, sep="\n")
