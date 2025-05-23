"""
Ejercicio 61 - diccionarios
"""

palabras_usuario = {}

palabra = ""

while palabra != "salir":
    palabra = input("Introduce una palabra (\"salir\" para terminar)")

    # Si el usuario ha escrito "salir", no queremos procesar esa palabra
    # Solo nos interesan las que sean distintas de "salir"
    if palabra != "salir":
        # Si la palabra no está en el diccionario (no es una clave del diccionario)
        if palabra not in palabras_usuario:
            # Añadirla al diccionario con valor 1
            palabras_usuario[palabra] = 1
        else:
            # La palabra ya está en el diccionario
            # Obtener el valor actual, sumar 1 y actualizar el diccionario
            palabras_usuario[palabra] += 1
            # En otros leguajes el += no funciona y se hace así
            # palabras_usuario[palabra] = palabras_usuario[palabra] + 1


# recorrer el diccionario y mostrar clave (palabra) y valor (cuantas veces se escribió).
for palabra, num_veces_escrita in palabras_usuario.items():
    print(palabra, "-", num_veces_escrita)
