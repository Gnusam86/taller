# Crear un diccionario
estudiantes = [
    {"nombre": "Ana", "calificacion": 85},
    {"nombre": "Luis", "calificacion": 65},
    {"nombre": "Marta", "calificacion": 90},
    {"nombre": "Juan", "calificacion": 72}
]

# Acceder a un valor
print(estudiante["nombre"])  # Output: Juan

# Modificar un valor
estudiante["edad"] = 22
print(estudiante)  # Output: {"nombre": "Juan", "edad": 22, "carrera": "Ingeniería"}

# Agregar un nuevo par clave-valor
estudiante["universidad"] = "UNAM"
print(estudiante)  # Output: {"nombre": "Juan", "edad": 22, "carrera": "Ingeniería", "universidad": "UNAM"}

# Eliminar un par clave-valor
del estudiante["carrera"]
print(estudiante)  # Output: {"nombre": "Juan", "edad": 22, "universidad": "UNAM"}
