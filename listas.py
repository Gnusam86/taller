# Crear una lista
frutas = ["manzana", "banana", "cereza"]

# Acceder a elementos
print(frutas[0])  # Output: manzana

# Modificar un elemento
frutas[1] = "mango"
print(frutas)  # Output: ["manzana", "mango", "cereza"]

# Agregar un elemento
frutas.append("naranja")
print(frutas)  # Output: ["manzana", "mango", "cereza", "naranja"]

# Eliminar un elemento
frutas.remove("mango")
print(frutas)  # Output: ["manzana", "cereza", "naranja"]
