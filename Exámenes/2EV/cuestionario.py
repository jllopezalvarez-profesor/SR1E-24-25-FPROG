"""
Fragmentos de código del cuestionario
"""

lista = [10, 20, 30, 40, 50]
print(lista[1:4])

##############

lista = [10, 20, 30, 40]
for i in range(len(lista) - 1, -1, -1):
    print(lista[i], end=" ")

print()

##############

numeros = [1, 2, 3, 4, 5, 6]
print(numeros[::-1])

##############

texto = "Python"
for letra in texto:
    print(letra, end="-")

print()

##############

valores = [x if x % 2 == 0 else -x for x in range(5)]
print(valores)

##############

i = 1
while i < 5:
    print(i, end=" ")
    i += 2

print()

##############

numeros = [5, 10, 15]
for i in range(len(numeros)):
    numeros[i] += 5
print(numeros)

##############

numeros = [2, 4, 6, 8]
for n in numeros:
    n *= 2
print(numeros)

##############

x = 1
while x < 10:
    x *= 2
print(x)

##############

x = 0
for i in range(1, 4):
    x += i
print(x)

##############

numeros = [x * 2 for x in range(3)]
print(numeros)

##############

texto = "hola"
resultado = ""
for letra in texto:
    resultado = letra + resultado
print(resultado)

###############

letras = ["a", "b", "c", "d", "e", "f"]
print(letras[:4:2])

################

contador = 0
for _ in range(3):
    contador += 1
print(contador)

################

palabra = "python"
resultado = ""
for letra in palabra:
    if letra in "aeiou":
        resultado += letra.upper()
    else:
        resultado += letra
print(resultado)
