# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#Sin comprensión de listas
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)
print(cuadrados)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



#Comprensión con condición
# Crear una lista de números pares
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Output: [0, 2, 4, 6, 8]


# Lista de frutas en mayúsculas
frutas = ["manzana", "banana", "cereza"]
frutas_mayusculas = [fruta.upper() for fruta in frutas]
print(frutas_mayusculas)  # Output: ['MANZANA', 'BANANA', 'CEREZA']


#CREAR UNA LISTA DE PARES ORDENADOS
# Lista de pares (x, y) donde x es de 0 a 2 y y es de 0 a 2
pares_ordenados = [(x, y) for x in range(3) for y in range(3)]
print(pares_ordenados)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#FILTRARY TRANSFORMAR SIMULTANEAMENTE
# Lista de cuadrados de números pares del 0 al 9
cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(cuadrados_pares)  # Output: [0, 4, 16, 36, 64]


#LISTAS ANIDADAS
# Lista de listas, donde cada sublista contiene números del 0 al 2
anidada = [[x for x in range(3)] for _ in range(3)]
print(anidada)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


