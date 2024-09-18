numero = int(input("Ingresa un número: "))
factorial = 1
i = 1

while i <= numero:
  factorial *= i
  i += 1

print("El factorial de", numero, "es:", factorial)