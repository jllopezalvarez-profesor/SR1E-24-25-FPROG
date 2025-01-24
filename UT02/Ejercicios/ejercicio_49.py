"""
Ejercicio 49
"""

palabra_1 = input("Introduce la primera palabra: ")
palabra_2 = input("Introduce la segunda palabra: ")

lista_1 = list(palabra_1)
lista_2 = list(palabra_2)

conjunto_todas = []
# Recorro la primera lista buscando letras que no estén ya en el conjunto
for letra in lista_1:
    if letra not in conjunto_todas:
        conjunto_todas.append(letra)
# Recorro la segunda lista buscando letras que no estén ya en el conjunto
for letra in lista_2:
    if letra not in conjunto_todas:
        conjunto_todas.append(letra)

print("Todas las letras de ambas palabras:", conjunto_todas, sep="\n")

conjunto_primera_no_segunda = []
for letra in lista_1:
    if letra not in lista_2 and letra not in conjunto_primera_no_segunda:
        conjunto_primera_no_segunda.append(letra)

print("Letras de la primera que no están en la segunda:",
      conjunto_primera_no_segunda, sep="\n")

conjunto_segunda_no_primera = []
for letra in lista_2:
    if letra not in lista_1 and letra not in conjunto_segunda_no_primera:
        conjunto_segunda_no_primera.append(letra)

print("Letras de la segunda que no están en la primera:",
      conjunto_segunda_no_primera, sep="\n")

conjunto_comunes = []
for letra in lista_1:
    if letra in lista_2 and not letra in conjunto_comunes:
        conjunto_comunes.append(letra)

print("Letras comunes a ambas palabras:",
      conjunto_comunes, sep="\n")
