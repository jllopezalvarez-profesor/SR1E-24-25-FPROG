"""
Ejercicio 10
Escribe un programa que pida una fecha (día, mes y año, por separado) y diga si
es correcta. Ten en cuenta que hay años bisiestos. En un problema anterior 
hicimos una comprobación de si un año es bisiesto o no.
"""

# Solicitar la fecha al usuario
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

# Comprobar si el año es válido
# Consideramos que cualquier año es válido menos el cero
if anio == 0:
    print("Fecha incorrecta. El año no es correcto")
elif mes < 1 or mes > 12:
    print("Fecha incorrecta. El mes no es correcto")
elif dia < 1:
    print("Fecha incorrecta. El día no es correcto")
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
    # Mes de 31 días, y el día es incorrecto
    print("Fecha incorrecta. El dia no es correcto")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    # Mes de 30 días, y el día es incorrecto
    print("Fecha incorrecta. El dia no es correcto")
else:
    # Determinar si el año es bisiesto
    es_bisiesto = False
    if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
        es_bisiesto = True

    # También puede hacerse como una asignación
    es_bisiesto = (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0)

    # Determinamos el número de días del mes
    dias_febrero = 29 if es_bisiesto else 28

    if mes == 2 and dia > dias_febrero:
        print("Fecha incorrecta. El día no es correcto")
    else:
        print("Fecha correcta")
