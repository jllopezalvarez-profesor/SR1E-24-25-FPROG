"""
Ejercicio 40
"""

cadena_usuario = input("Introduce una frase: ")

resultado = ""

for letra in cadena_usuario:
    resultado = resultado + letra + "."

# if len(resultado) > 0:
print(f"Resultado antes de cortar el final: '{resultado}'")
# resultado = resultado[:len(resultado)-1] # Más fácil con -1
resultado = resultado[:-1]

print(f"Resultado después de cortar el final: '{resultado}'")
