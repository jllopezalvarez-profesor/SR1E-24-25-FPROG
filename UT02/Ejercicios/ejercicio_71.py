"""
Función es_primo
"""


def es_primo_peor(num):
    if not isinstance(num, int) or num <= 1:
        return False

    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True


def es_primo_algo_mejor(num):
    # No es número, o es <= 1
    if not isinstance(num, int) or num <= 1:
        return False

    # El 2 es el único par primo
    if num == 2:
        return True

    # Cualquier otro par no es primo, porque es divisible por 2
    if num % 2 == 0:
        return False

    # Como hemos descartado el 2 como factor, podemos saltar (no comprobar) los pares
    # Para optimizar, se puede llegar a num/2, o mejor aún a math.sqrt(num)

    for divisor in range(3, num, 2):
        if num % divisor == 0:
            return False

    return True


print(f"¿el número 1 es primo? {es_primo_peor(1)}")
print(f"¿el número 0 es primo? {es_primo_peor(0)}")
print(f"¿el número -3 es primo? {es_primo_peor(-3)}")
print(f"¿el número 'x' es primo? {es_primo_peor('x')}")
print(f"¿el número 'hola' es primo? {es_primo_peor('hola')}")
print(f"¿el número 2 es primo? {es_primo_peor(2)}")
print(f"¿el número 6 es primo? {es_primo_peor(6)}")
print(f"¿el número 11 es primo? {es_primo_peor(11)}")

print("_"*100)

print(f"¿el número 1 es primo? {es_primo_algo_mejor(1)}")
print(f"¿el número 0 es primo? {es_primo_algo_mejor(0)}")
print(f"¿el número -3 es primo? {es_primo_algo_mejor(-3)}")
print(f"¿el número 'x' es primo? {es_primo_algo_mejor('x')}")
print(f"¿el número 'hola' es primo? {es_primo_algo_mejor('hola')}")
print(f"¿el número 2 es primo? {es_primo_algo_mejor(2)}")
print(f"¿el número 6 es primo? {es_primo_algo_mejor(6)}")
print(f"¿el número 11 es primo? {es_primo_algo_mejor(11)}")
