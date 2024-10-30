class Saludador:
    def __init__(self, nombre):
        self.nombre = nombre

    def __call__(self, saludo):
        return f"{saludo}, {self.nombre}!"

# Crear una instancia de la clase
s = Saludador("Ana")

# Llamar a la instancia como si fuera una función
print(s("Hola"))  # Output: Hola, Ana!
#print(s.nombre)