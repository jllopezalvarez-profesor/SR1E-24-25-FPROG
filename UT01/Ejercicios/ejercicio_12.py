"""
Ejercicio 12
"""

# Pedir al usuario las cinco calificaciones
primer_parcial = float(input("Introduce la nota del primer parcial: "))
segundo_parcial = float(input("Introduce la nota del segundo parcial: "))
tercer_parcial = float(input("Introduce la nota del tercer parcial: "))
examen_final = float(input("Introduce la nota del examen final: "))
trabajo_final = float(input("Introduce la nota del trabajo final: "))

# Constantes para porcentajes
PESO_PARCIALES = 0.55
PESO_FINAL = 0.30
PESO_TRABAJO = 0.15

# Calculo la nota final
nota_final = ((primer_parcial+segundo_parcial+tercer_parcial) / 3) * \
    PESO_PARCIALES + examen_final * PESO_FINAL + trabajo_final * PESO_TRABAJO

# Mostar el resultado
print(f"La nota final es {nota_final}.")
