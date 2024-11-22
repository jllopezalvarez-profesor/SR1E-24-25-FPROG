"""
Ejercicio 11
"""
INCREMENTO_A_1 = 20
INCREMENTO_A_2 = 30
INCREMENTO_B_1 = -30
INCREMENTO_B_2 = -50

tipo_uva = input("Introduce el tipo de uva: ")
tamanio = int(input("Introduce el tamaño de la uva: "))

# Validamos el tipo de uva
if tipo_uva != "A" and tipo_uva != "B":
    print("El tipo que has introducido no es válido")
else:  # puedo cambiar el ele + if en elif
    if tamanio != 1 and tamanio != 2:
        print("El tamaño introducido no es correcto")
    else:  # No puedo poner elif porque el print está dentro de este else
        incremento = 0
        if tipo_uva == "A":
            if tamanio == 1:
                incremento = INCREMENTO_A_1
            else:
                incremento = INCREMENTO_A_2
        else:
            if tamanio == 1:
                incremento = INCREMENTO_B_1
            else:
                incremento = INCREMENTO_B_2
        print(f"El cambio de precio es de {incremento} céntimos por kilo")
