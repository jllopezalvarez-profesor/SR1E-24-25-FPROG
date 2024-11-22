"""
Ejemplo de uso de flags para saber si ha pasado algo en alguna iteración
"""

# Inicializamos a false porque asumimos que no se ha encontrado lo que buscamos
multiplo_encontrado = False

# Preguntamos 5 números al usuario
for i in range(5):
    numero = int(input("Introduce un número: "))
    if numero % 5 == 0:
        multiplo_encontrado = True

print("Se ha encontrado al menos un múltiplo de cinco" if multiplo_encontrado else "No se ha encontrado ningún múltiplo de cinco")
