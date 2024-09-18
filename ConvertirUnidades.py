from pint import UnitRegistry

ureg = UnitRegistry()

def convertir_longitud(valor, unidad_origen, unidad_destino):
    """Convierte una longitud de una unidad a otra."""
    cantidad = valor * ureg(unidad_origen)
    resultado = cantidad.to(unidad_destino)
    return resultado

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    """Convierte una temperatura de una unidad a otra."""
    cantidad = valor * ureg(unidad_origen)
    resultado = cantidad.to(unidad_destino)
    return resultado

if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Convertir longitud")
        print("2. Convertir temperatura")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Ingrese la unidad de origen (e.g., meter, feet, miles): ")
            unidad_destino = input("Ingrese la unidad de destino: ")
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} son equivalentes a {resultado}")

        elif opcion == '2':
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Ingrese la unidad de origen (e.g., celsius, fahrenheit, kelvin): ")
            unidad_destino = input("Ingrese la unidad de destino: ")
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} son equivalentes a {resultado}")

        elif opcion == '3':
            break

        else:
            print("Opción inválida. Intente de nuevo.")