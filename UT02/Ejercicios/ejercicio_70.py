"""
Funcion factorial
"""


def factorial_compleja(n):
    # Dentro de la función
    if isinstance(n, int):
        if n >= 0:
            # Calcular el factorial
            acumulador = 1
            for i in range(2, n+1):
                acumulador *= i
            return acumulador
        else:
            return -1
    else:
        return -1


def factorial_semi_compleja(n):
    # Dentro de la función
    if isinstance(n, int):
        if n >= 0:
            # Calcular el factorial
            acumulador = 1
            for i in range(2, n+1):
                acumulador *= i
            return acumulador
        else:
            return -1
    else:
        return -1


def factorial(n):
    # Dentro de la función
    if not isinstance(n, int):
        return -1

    if n < 0:
        return -1

    # Calcular el factorial
    acumulador = 1
    for i in range(2, n+1):
        acumulador *= i
    return acumulador

    # Recursivo
    # if n == 0:
    #     return 1
    # return n * factorial(n-1)


# Fuera de la función
print(f"El factorial de 0 es {factorial_compleja(0)}")
print(f"El factorial de 1 es {factorial_compleja(1)}")
print(f"El factorial de 2 es {factorial_compleja(2)}")
print(f"El factorial de 5 es {factorial_compleja(5)}")

# Fuera de la función
print(f"El factorial de 0 es {factorial(0)}")
print(f"El factorial de 1 es {factorial(1)}")
print(f"El factorial de 2 es {factorial(2)}")
print(f"El factorial de 5 es {factorial(5)}")
