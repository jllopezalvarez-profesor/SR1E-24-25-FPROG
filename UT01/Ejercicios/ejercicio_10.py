"""
Ejercicio 10
"""

# Pedir al usuario el número de minutos
total_minutos = int(input("Introduce el número de minutos: "))

# Constante para el número de minutos en una hora
MINUTOS_EN_UNA_HORA = 60

# Calcular el número de horas (división entera):
horas = total_minutos // MINUTOS_EN_UNA_HORA

# Calcular minutos restantes
minutos = total_minutos % MINUTOS_EN_UNA_HORA

# Mostar el resultado
print(f"En {total_minutos} minnutos hay {horas} horas y {minutos} minutos.")
