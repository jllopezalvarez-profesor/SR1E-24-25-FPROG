"""

"""


def suma3(num):
    num = num + 3
    return num


def elimina_primero(lista):
    del lista[0]


def cambia_totalmente_lista(lista):
    lista = ['a', 'b', 'c']


numero = 10

print(f"El valor de 'numero' antes de llamar a 'suma3' es: {numero}")
suma3(numero)
print(f"El valor de 'numero' despues de llamar a 'suma3' es: {numero}")
print(
    f"El valor de 'numero' si llamo a suma3 dentro de la f-string es: {suma3(numero)}")


lista_numeros = [1, 2, 3, 4, 5]
print(f"La lista antes de llamar a elimina_primero: {lista_numeros}")
elimina_primero(lista_numeros)
print(f"La lista después de llamar a elimina_primero: {lista_numeros}")
cambia_totalmente_lista(lista_numeros)
print(f"La lista después de llamar a cambia_totalmente_lista: {lista_numeros}")
