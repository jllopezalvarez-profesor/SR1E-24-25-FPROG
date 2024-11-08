"""
Ejercicio 05
Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al 
sistema”, si no, se mostrará un error.
"""

usuario = input("Introduce el nombre de usuario: ")
password = input("Introduce la contraseña: ")

# Para comprobar dos condiciones a la vez, tenemos que usar "and"
if usuario == "pepe" and password == "asdasd":
    print("Has entrado al sistema")
else:
    print("Usuario y/o contraseña incorrectos")
