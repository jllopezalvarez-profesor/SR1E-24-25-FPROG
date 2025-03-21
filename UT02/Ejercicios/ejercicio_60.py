"""
Ejercicio 60 - Diccionarios
"""

datos_usuario = {
    'nombre_completo': "José Luis López Álvarez",
    "edad": 52,
    "ciudad nacimiento": "Madrid"
}

print(datos_usuario)

# print("Me llamo", datos_usuario["nombre_completo"])
# print(f"Tengo {datos_usuario["edad"]} años")
# print(f"Nací en {datos_usuario["ciudad nacimiento"]}")

for clave, valor in datos_usuario.items():
    print(f"\t{clave} - {valor}")

# Añadimos dos elementos al diccionario
datos_usuario["profesion"] = "Informático"
datos_usuario["estudios"] = "Diplomatura en informática"

print(datos_usuario)

# print("Me llamo", datos_usuario["nombre_completo"])
# print(f"Tengo {datos_usuario["edad"]} años")
# print(f"Nací en {datos_usuario["ciudad nacimiento"]}")
# print("Soy", datos_usuario["profesion"])
# print("Estudié", datos_usuario["estudios"])

for clave in datos_usuario:
    print(f"\t{clave} - {datos_usuario[clave]}")

# Modificar elementos del diccionario
# Cambiar la profesion:
datos_usuario["profesion"] = "Profesor"
datos_usuario["edad"] = 55

print(datos_usuario)

# print("Me llamo", datos_usuario["nombre_completo"])
# print(f"Tengo {datos_usuario["edad"]} años")
# print(f"Nací en {datos_usuario["ciudad nacimiento"]}")
# print("Soy", datos_usuario["profesion"])
# print("Estudié", datos_usuario["estudios"])

# Recorro solo los valores del diccionario
num_valor = 1
for valor in datos_usuario.values():
    print(f"\tValor en elemento {num_valor} - {valor}")
    num_valor += 1


# Eliminar edad y ciudad de nacimiento
del datos_usuario["edad"]
if "ciudad_nacimiento" in datos_usuario:
    del datos_usuario["ciudad_nacimiento"]
else:
    print(f"No se encuentra la clave \"ciudad_nacimiento\" en el diccionario")
