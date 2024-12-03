numeros = list(range(2, 100))

print(numeros)

i = 0
while i < len(numeros):
    for j in range(len(numeros)-1, i, -1):
        if numeros[j] % numeros[i] == 0:
            del numeros[j]
    i += 1

print(numeros)
