"""
Solución al ejercicio 2 del modelo A del examen del día 31/01/2025
Autor: José Luis López Álvarez
"""

# Enunciado
# Escribe un programa en python que:
#   - Pida al usuario una frase, una línea de texto.
#   - Si la línea de texto está vacía, se informa del error y el programa termina.
#   - Para terminar no se pueden usar funciones como exit() o quit(), ni lanzar excepciones, etc.
#   - El programa contará cuantas vocales hay en la frase, y mostrará el resultado.
#   - Se consideran vocales: a, A, e, E, i, I, o, O, u U. Ninguna otra letra se considera vocal, ni siquiera las acentuadas(á, à, â, etc.)
#   - No se pueden usar listas, conjuntos, o diccionarios en este ejercicio


linea = input("Introduce una línea de texto: ")
if len(linea) == 0:
    print("La línea de texto está vacía. El programa terminará.")
else:
    vocales = "aAeEiIoOuU"
    contador = 0
    for letra in linea:
        if letra in vocales:
            contador += 1
    print(f"En el texto introducido hay {contador} vocales.")
