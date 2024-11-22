"""
Ejercicio 15
"""
# Constantes para los días de la semana (1 a 7)
DIA_1 = 1
DIA_2 = 2
DIA_3 = 3
DIA_4 = 4
DIA_5 = 5
DIA_6 = 6
DIA_7 = 7
# Constantes para los días de la semana (nombres en texto)
LUNES = "lunes"
MARTES = "martes"
MIERCOLES = "miércoles"
JUEVES = "jueves"
VIERNES = "viernes"
SABADO = "sábado"
DOMINGO = "domingo"

# Entrada del usuario
dia_semana = int(input("Introduce el de la semana (1-7): "))

if (dia_semana < DIA_1 or dia_semana > DIA_7):
    print("No es un día de la semana válido")
else:
    # Determinación del texto del día de la semana
    if dia_semana == DIA_1:
        dia_en_letras = LUNES
    elif dia_semana == DIA_2:
        dia_en_letras = MARTES
    elif dia_semana == DIA_3:
        dia_en_letras = MIERCOLES
    elif dia_semana == DIA_4:
        dia_en_letras = JUEVES
    elif dia_semana == DIA_5:
        dia_en_letras = VIERNES
    elif dia_semana == DIA_6:
        dia_en_letras = SABADO
    elif dia_semana == DIA_7:
        dia_en_letras = DOMINGO

    # Mostrar el día de la semana en letras
    # Pylint puede mostrar un error, pero es porque el análisis
    # de código que realiza no tiene en cuenta el if previo que
    # no deja entrar con valores incorrectos
    print(f"El día que corresponde a {dia_semana} es el {dia_en_letras}.")
