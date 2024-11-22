"""
Ejercicio 15
"""
# Casos y valores representativos para las circunferencias
# -----------------------------------------------------------------------
# | Caso                | x1  | y1  | r1   | x2  | y2  | r2   | d       |
# -----------------------------------------------------------------------
# | Exteriores          | 0   | 0   | 5    | 15  | 0   | 5    | 15.00   |
# | Tangentes exteriores| 0   | 0   | 5    | 10  | 0   | 5    | 10.00   |
# | Secantes            | 0   | 0   | 5    | 6   | 0   | 5    | 6.00    |
# | Tangentes interiores| 0   | 0   | 5    | 3   | 0   | 2    | 3.00    |
# | Interiores          | 0   | 0   | 5    | 2   | 0   | 2    | 2.00    |
# | Concéntricas        | 0   | 0   | 5    | 0   | 0   | 3    | 0.00    |
# | Coincidentes        | 0   | 0   | 5    | 0   | 0   | 5    | 0.00    |
# -----------------------------------------------------------------------


from math import sqrt

# Primera circunferencia
print("Introduce los datos de la primera circunferencia: centro (x1, y1) y radio (r1)")
# Pedir x1 e y1, de la primera circunferencia
x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
# Pedir el radio de la primera circunferencia
r1 = float(input("Introduce el radio de la primera circunferencia (r1): "))


# Segunda circunferencia
print("Introduce los datos de la segunda circunferencia: centro (x2, y2) y radio (r2)")
# Pedir x2 e y2, de la segunda circunferencia
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))
# Pedir el radio de la primera circunferencia
r2 = float(input("Introduce el radio de la segunda circunferencia (r2): "))

# Cálculo de la distancia entre los centros
d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Determinación de la relación entre las circunferencias
if d > r1 + r2:
    clasificacion = "Exteriores"
elif d == r1 + r2:
    clasificacion = "Tangentes exteriores"
elif d == 0 and r1 != r2:
    clasificacion = "Concéntricas"
elif d == 0 and r1 == r2:
    clasificacion = "Coincidentes"
elif d == abs(r1 - r2):
    clasificacion = "Tangentes interiores"
elif r1 - r2 < d < r1 + r2 or r2 - r1 < d < r1 + r2:
    clasificacion = "Secantes"
elif 0 < d < abs(r1 - r2):
    # Como no sabemos qué radio es menor, abs calcula el valor absoluto de la resta.
    clasificacion = "Interiores"
else:
    # Este caso no se dará nunca, pero lo ponemos para probar
    clasificacion = "Clasificación no determinada"

# Salida
print(f"\nLa distancia entre los centros es: {d:.2f}")
print(f"Las circunferencias son: {clasificacion}.")
