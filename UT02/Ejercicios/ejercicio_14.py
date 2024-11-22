"""
Ejercicio 14
"""
# Constantes para las caras y las caras opuestas
CARA_1 = 1
CARA_OPUESTA_1 = "seis"
CARA_2 = 2
CARA_OPUESTA_2 = "cinco"
CARA_3 = 3
CARA_OPUESTA_3 = "cuatro"
CARA_4 = 4
CARA_OPUESTA_4 = "tres"
CARA_5 = 5
CARA_OPUESTA_5 = "dos"
CARA_6 = 6
CARA_OPUESTA_6 = "uno"

# Entrada del usuario
resultado = int(input("Introduce el resultado del dado (1-6): "))

if (resultado < CARA_1 or resultado > CARA_6):
    print("No es un resultado válido")
else:
    # Determinación de la cara opuesta
    # No hay else final porque ya hemos filtrado
    # previamente los casos que se salen del tramo 1-6
    if resultado == CARA_1:
        cara_opuesta = CARA_OPUESTA_6
    elif resultado == CARA_6:
        cara_opuesta = CARA_OPUESTA_1
    elif resultado == CARA_2:
        cara_opuesta = CARA_OPUESTA_5
    elif resultado == CARA_5:
        cara_opuesta = CARA_OPUESTA_2
    elif resultado == CARA_3:
        cara_opuesta = CARA_OPUESTA_4
    elif resultado == CARA_4:
        cara_opuesta = CARA_OPUESTA_3

    # Mostrar cara opuesta
    # Pylint puede mostrar un error, pero es porque el análisis
    # de código que realiza no tiene en cuenta el if previo que
    # no deja entrar con valores incorrectos
    print(f"La cara opuesta es: {cara_opuesta}.")
