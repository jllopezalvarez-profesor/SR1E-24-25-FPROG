"""
Ejemplos de if
"""

edad = 20

if edad > 30:
    print("La edad es mayor que 30")
else:
    print("La edad es menor o igual que 30")


edad = int(input("Dime tu edad: "))

if edad > 50:
    print("Ya estás mayor")
elif edad > 30:
    print("Estás mayor, pero no demasiado")
elif edad > 10:
    print("Eres joven")
else:
    print("Eres un niño")


print("Esto se ejecuta siempre, pase lo que pase")


edad = int(input("Dime tu edad, otra vez: "))


# Ojo, que el orden puede importar

if edad > 30:
    print("Estás mayor, pero no demasiado")
elif edad > 50:
    print("Ya estás mayor")
elif edad > 10:
    print("Eres joven")
else:
    print("Eres un niño")
