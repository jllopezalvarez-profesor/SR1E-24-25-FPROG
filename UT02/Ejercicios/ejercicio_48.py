"""
Ejercicio 48
"""

frase = input("Introduce una frase o una palabra: ")

print("Frase sin convertir a lista")
print(frase)

# Convertir frase a lista
lista = list(frase)
print("Frase convertida a lista")
print(lista)

# Creo una lista para los caracteres de la frase (pero sin repetirse)
lista_no_repetidos = []
# Quiero que los caracteres aparezcan en el mismo orden que en la frase
for letra in lista:
    # Si la letra NO está ya en la lista de no repetidos, se añade
    if letra not in lista_no_repetidos:
        lista_no_repetidos.append(letra)

print(lista_no_repetidos)

conjunto_letras = set(frase)
print("El conjunto de letras (usando set) es:")
print(conjunto_letras)
