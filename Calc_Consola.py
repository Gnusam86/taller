def sumar(x, y):
    """Suma dos números."""
    return x + y

def restar(x, y):
    """Resta dos números."""
    return x - y

def multiplicar(x, y):
    """Multiplica dos números."""
    return x * y

def dividir(x, y):
    """Divide dos números.

    Args:
        x: El dividendo.
        y: El divisor.

    Returns:
        El resultado de la división si el divisor no es cero.
        Un mensaje de error si el divisor es cero.
    """
    if y == 0:
        return "Error: División por cero"
    else:
        return x / y

while True:
    print("\nSeleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese su elección (1/2/3/4/5): ")

    if opcion == '5':
        break

    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(num1, "+", num2, "=", sumar(num1, num2))

        elif opcion == '2':
            print(num1, "-", num2, "=", restar(num1, num2))

        elif opcion == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif opcion == '4':
            print(num1, "/", num2, "=", dividir(num1, num2))

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")