"""
Ejemplos de funciones
"""


def print_with_tabs(info_list, num_tabs_inicial=0):
    print("-"*30)
    num_tabs = num_tabs_inicial
    for num in info_list:
        if num % 2 == 0:
            print("\t"*num_tabs, num, sep="")
            num_tabs += 1
        else:
            print(num*2)
    print("-"*30)


lista_numeros = [1, 3, 1, 4, 56, 2, 1, 4, 6, 2, 1, 4, 2]

# print("-"*30)
# num_tabs = 0
# for num in lista:
#     if num % 2 == 0:
#         print("\t"*num_tabs, num, sep="")
#         num_tabs += 1
#     else:
#         print(num*2)
# print("-"*30)

print_with_tabs(lista_numeros, 3)

for i in range(len(lista_numeros)):
    lista_numeros[i] = lista_numeros[i]*2


print_with_tabs(lista_numeros)


# Tuplas

edad_y_color_pelo = (30, "rubio")
print(edad_y_color_pelo)

edad, color_pelo = edad_y_color_pelo
print(edad)
print(color_pelo)


# Cadena de llamadas
print(min(max(2, 3), max(3, 5)))
