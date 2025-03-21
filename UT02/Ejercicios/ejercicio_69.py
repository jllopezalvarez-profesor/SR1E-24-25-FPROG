"""
Ejercicio 69
"""


def mostrar_n_veces(texto, cuantas_veces):
    if cuantas_veces <= 0:
        print("error")
        return

    while (cuantas_veces > 0):
        print(texto)
        cuantas_veces -= 1


mostrar_n_veces("Hola", -1)
mostrar_n_veces("Adiós", 3)

numero_veces = 3

mostrar_n_veces("Otra cosa", numero_veces)
print(numero_veces)
