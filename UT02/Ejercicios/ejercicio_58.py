"""
Ejercicio 58 - Diccionarios
"""

datos_usuario = {
    'nombre_completo': "José Luis López Álvarez",
    "edad": 52,
    "ciudad nacimiento": "Madrid"
}

print(datos_usuario)

print("Me llamo", datos_usuario["nombre_completo"])
print(f"Tengo {datos_usuario["edad"]} años")
print(f"Nací en {datos_usuario["ciudad nacimiento"]}")

datos_usuario["profesion"] = "Informático"
datos_usuario["estudios"] = "Diplomatura en informática"

print(datos_usuario)

print("Me llamo", datos_usuario["nombre_completo"])
print(f"Tengo {datos_usuario["edad"]} años")
print(f"Nací en {datos_usuario["ciudad nacimiento"]}")
print("Soy", datos_usuario["profesion"])
print("Estudié", datos_usuario["estudios"])

# Modificar elementos del diccionario
# Cambiar la profesion:
datos_usuario["profesion"] = "Profesor"
datos_usuario["edad"] = 55

print("Me llamo", datos_usuario["nombre_completo"])
print(f"Tengo {datos_usuario["edad"]} años")
print(f"Nací en {datos_usuario["ciudad nacimiento"]}")
print("Soy", datos_usuario["profesion"])
print("Estudié", datos_usuario["estudios"])
