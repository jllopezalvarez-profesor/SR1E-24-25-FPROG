"""
Ejercicio 07
Crea un programa que pida dos números "nota" y "edad" y un carácter "sexo" y muestre
el mensaje "ACEPTADA" si la nota es mayor o igual a cinco, la edad es mayor o igual a
dieciocho y el sexo es "F". En caso de que se cumpla lo mismo, pero el sexo sea "M", 
debe imprimir "POSIBLE". Si no se cumplen dichas condiciones se debe mostrar "NO ACEPTADA".
"""

# Solicitar los valores al usuario
nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ")

# Convertir la entrada del usuario a mayúsculas, para que sea más fácil comparar
sexo = sexo.upper()

# Evaluar las condiciones
if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")


letra_original = input("Introduce una letra mayúscula: ")

# Para calcular la longitud de un string:
longitud = len(letra_original)

# Para convertir algo a mayúsculas
letra_mayusculas = letra_original.upper()

# Comprobamos que es de longitud 1 y que las dos cadenas son iguales
if longitud == 1 and letra_original == letra_mayusculas:
    print(f"'{letra_original}' es una letra mayúscula")
else:
    print(f"'{letra_original}' NO es una letra mayúscula")

# Se puede hacer con expresiones, sin las variables "intermedias"
if len(letra_original) == 1 and letra_original == letra_original.upper():
    print(f"'{letra_original}' es una letra mayúscula")
else:
    print(f"'{letra_original}' NO es una letra mayúscula")
