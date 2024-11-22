"""
Ejercicio 13
"""
# Constantes para fin de tramo
FIN_TRAMO_1 = 5
FIN_TRAMO_2 = 8
FIN_TRAMO_3 = 10
# Constantes calculadas para duraciones de tramos
DURACION_TRAMO_1 = FIN_TRAMO_1
DURACION_TRAMO_2 = FIN_TRAMO_2 - FIN_TRAMO_1
DURACION_TRAMO_3 = FIN_TRAMO_3 - FIN_TRAMO_1
# Constantes para los precios por minuto de los tramos
PRECIO_MINUTOS_TRAMO_1 = 1
PRECIO_MINUTOS_TRAMO_2 = 0.8
PRECIO_MINUTOS_TRAMO_3 = 0.7
PRECIO_MINUTOS_RESTO = 0.5
# Constantes para impuestos
IMPUESTO_DOMINGO = 0.03
IMPUESTO_DIARIO_MANIANA = 0.15
IMPUESTO_DIARIO_TARDE = 0.10


# Pedir tiempo de llamada en minutos
duracion_llamada = int(input("Duración de la llamada (en minutos): "))

# Pedir dia de la semana
# Pasamos a minúsculas para comparar mejor
dia = input("Día de la llamada (lunes a domingo): ").lower()

# Pedir turno. Sólo lo pedimos si el día de la semana es Domingo
if dia != "domingo":
    # Pasamos a minúsculas para comparar mejor
    turno = input("Ingrese el turno de la llamada (mañana/tarde): ").lower()

# Inicializamos el coste
# No es necesario, porque se le da valor en cualquier
# alternativa, pero así queda más claro el código.
costo_base = 0

# Calculamos el coste según la duración
if duracion_llamada <= FIN_TRAMO_1:
    costo_base = duracion_llamada * PRECIO_MINUTOS_TRAMO_1
elif duracion_llamada <= FIN_TRAMO_2:
    costo_base = DURACION_TRAMO_1 * PRECIO_MINUTOS_TRAMO_1
    costo_base += (duracion_llamada - FIN_TRAMO_1) * PRECIO_MINUTOS_TRAMO_2
elif duracion_llamada <= FIN_TRAMO_3:
    costo_base = DURACION_TRAMO_1 * PRECIO_MINUTOS_TRAMO_1
    costo_base += DURACION_TRAMO_2 * PRECIO_MINUTOS_TRAMO_2
    costo_base += (duracion_llamada - FIN_TRAMO_2) * PRECIO_MINUTOS_TRAMO_3
else:
    costo_base = DURACION_TRAMO_1 * PRECIO_MINUTOS_TRAMO_1
    costo_base += DURACION_TRAMO_2 * PRECIO_MINUTOS_TRAMO_2
    costo_base += DURACION_TRAMO_3 * PRECIO_MINUTOS_TRAMO_3
    costo_base += (duracion_llamada - FIN_TRAMO_3) * PRECIO_MINUTOS_RESTO

# Calculamos el impuesto
if dia == "domingo":
    impuesto = costo_base * IMPUESTO_DOMINGO
else:
    if turno == "mañana":
        impuesto = costo_base * IMPUESTO_DIARIO_MANIANA
    elif turno == "tarde":
        impuesto = costo_base * IMPUESTO_DIARIO_TARDE
    else:
        # Quizá se podría mostrar un error.
        impuesto = 0

# Total a pagar
total = costo_base + impuesto

# Mostramos los datos
print(f"\nCosto base de la llamada: {costo_base:.2f} euros")
print(f"Impuesto aplicado: {impuesto:.2f} euros")
print(f"Total a pagar: {total:.2f} euros")
