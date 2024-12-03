"""
Ejemplos de [:] en strings
"""
posiciones = "0123456789"
cadena = "ABCDEFGHIJKL"

print(posiciones)
print(cadena)
print(cadena[:])  # Copia de la cadena entera
print(cadena[:3])  # Hasta la posición 3 no incluida, desde inicio
print(cadena[3:])  # Desde la posición 3 incluida al final
# Empieza en la última letra, avanza hacia la derecha, y por eso devuelve solo una
print(cadena[-1:])
# Empieza en la última letra, avanza hacia la derecha, y por eso devuelve dos
print(cadena[-2:])
print(cadena[-2:-5])

print(cadena[-2:-5:-1])

print(cadena[::-1])
print(cadena[::-2])
print(cadena[::-3])

print(cadena[::2])
print(cadena[::3])

print(cadena[:-1])
