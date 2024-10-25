# Generador de cuadrados de números del 0 al 9
cuadrados_gen = (x**2 for x in range(10))
for cuadrado in cuadrados_gen:
    print(cuadrado)
# Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 (uno por línea)
