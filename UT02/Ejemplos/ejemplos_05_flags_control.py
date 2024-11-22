"""
Ejemplo de uso de flags para controlar salida de un bucle
"""

# Inicializamos a false para que entre en el bucle
seguir_preguntando = True

# Seguimos mientras se cumpla la condición (flag = true)
while seguir_preguntando:
    numero = int(input("Introduce un número, cero para salir: "))
    if numero == 0:
        seguir_preguntando = False
print("Se ha salido del bucle 'while seguir_preguntando'")

# La lógica se puede invertir: seguir mientras no se cumpla
# En este caso se inicializa a False
salir_del_bucle = False

# Seguimos mientras se cumpla la condición (flag = false)
while not salir_del_bucle:
    numero = int(input("Introduce un número, cero para salir: "))
    if numero == 0:
        salir_del_bucle = True
print("Se ha salido del bucle 'while not salir_del_bucle'")
