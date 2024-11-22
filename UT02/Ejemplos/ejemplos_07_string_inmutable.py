"""
Ejemplos de inmutabilidad de string
"""

cadena = "Hola a todos los alumnos de SR1E"

# Si muestro la cadena sale tal y como se definió
print(cadena)

# La primera de cada palabra a mayúsculas
cadena.title()
# No cambia porque es inmutable
print(cadena)

# Tengo que guardar el resultado de title() en la misma variable u otra
cadena_title = cadena.title()
print(cadena_title)

# Si queremos que "cadena" cambie:
cadena = cadena.title()
print(cadena)

# Concateno  cadenas
cadena_saludo = "El saludo es " + cadena
print(cadena_saludo)

# Lo mismo sin concatenar
print("El saludo es", cadena)
