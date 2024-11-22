"""
Ejercicio 12
"""

# Pedir al usuario número de alumnos
numero_alumnos = int(input("Ingrese el número de alumnos que van al viaje: "))


# Determinamos el costo según el número de alumnos
if numero_alumnos >= 100:
    costo_por_alumno = 65
    costo_total = numero_alumnos * costo_por_alumno
elif 50 <= numero_alumnos <= 99:
    costo_por_alumno = 70
    costo_total = numero_alumnos * costo_por_alumno
elif 30 <= numero_alumnos <= 49:
    costo_por_alumno = 95
    costo_total = numero_alumnos * costo_por_alumno
else:  # Menos de 30 alumnos. En este caso se divide el total
    # por el número de alumnos para calcular cuanto paga cada uno.
    costo_total = 4000
    costo_por_alumno = costo_total / numero_alumnos

# Mostrar resultados
print(f"\nCosto total a pagar a la compañía de autobuses: {
      costo_total:.2f} euros")
print(f"Costo por alumno: {costo_por_alumno:.2f} euros")
