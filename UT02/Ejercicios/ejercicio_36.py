"""
Ejercicio 36
"""

texto_usuario = input("Introduce una frase: ")

print(f"La longitud de la frase es {len(texto_usuario)}")

contador = 0


for letra in texto_usuario:
    print(f"Procesando la letra '{letra}'.")
    if letra == " ":
        contador += 1

print(f"Buscando con un for-each en la frase '{
      texto_usuario}' he encontrado {contador} espacios.")

contador = 0
for posicion in range(len(texto_usuario)):
    print(f"Procesando la letra '{texto_usuario[posicion]}'.")
    if texto_usuario[posicion] == " ":
        contador += 1

print(f"Buscando con un for por índice en la frase '{
      texto_usuario}' he encontrado {contador} espacios.")


print(f"Buscando con un count en la frase '{
      texto_usuario}' he encontrado {texto_usuario.count(' ')} espacios.")
