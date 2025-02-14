"""
Ejemplos de diccionarios
"""

dias_semana = {1: "lunes", 2: "martes", 3: "miércoles"}


print(dias_semana)


dia = int(input("Introduce un número de día de la semana. 0 para terminar"))

while dia != 0:
    # print(dias_semana[dia])
    print(dias_semana.get(dia, 'no encontrado'))
    dia = int(input("Introduce un número de día de la semana. 0 para terminar"))
