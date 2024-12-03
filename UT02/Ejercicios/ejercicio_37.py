"""
Ejercicio 37
"""

num_palabras = int(input("Cuantas palabras quieres escribir: "))

# SEPARADOR = "-"
SEPARADOR = "\t"

frase1 = ""
frase2 = ""
frase3 = ""
for i in range(1, num_palabras+1):
    palabra = input(f"Dime la palabra número {i}: ")
    frase1 = frase1 + SEPARADOR + palabra
    frase2 = frase2 + palabra + SEPARADOR
    if frase3 != "":
        frase3 += SEPARADOR
    frase3 += palabra


print("Frase 1:")
print(frase1)
print("Frase 2:")
print(frase2)
print("Frase 3:")
print(frase3)
