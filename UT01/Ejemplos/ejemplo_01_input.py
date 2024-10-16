"""
Ejemplos de uso de input y print
Todos los módulos (ficheros .py) deben empezar, 
por convención, con una explicación del módulo, 
que se debe encerrar entre comillas triples (docstring)
"""
# Pedir al usuario texto
texto = input("Escribe lo que quieras: ")

# Mostrar el texto del usuario:
print(texto)

# Pedir al usuario un número sin decimales (entero)
# Como input devuelve str (string), se convierte con int()
# Si el usuario introduce algo que no pueda convertirse a int, falla
numero_entero = int(input("Escribe un número entero: "))
# Mostrar el valor introducido por el usuario
print(numero_entero)

# Pedir un número real (float) con decimales
# Igual que con los enteros, hay que convertir de str a float
# Si el usuario introduce algo que no pueda convertirse a float, falla
numero_real = float(input("Escribe un número con decimales: "))
# Mostar el valor que ha introducido el usuario.
print(numero_real)
