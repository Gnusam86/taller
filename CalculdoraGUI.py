import tkinter as tk

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    else:
        return x / y

def button_click(number):
    """Agrega el número presionado a la pantalla."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    """Limpia la pantalla."""
    entry.delete(0, tk.END)

def button_add():
    """Almacena el primer número y la operación de suma."""
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "suma"
    entry.delete(0, tk.END)

def button_subtract():
    """Almacena el primer número y la operación de resta."""
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "resta"
    entry.delete(0, tk.END)

def button_multiply():
    """Almacena el primer número y la operación de multiplicación."""
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "multiplicacion"
    entry.delete(0, tk.END)

def button_divide():
    """Almacena el primer número y la operación de división."""
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "division"
    entry.delete(0, tk.END)

def button_equal():
    """Realiza la operación almacenada y muestra el resultado."""
    second_number = float(entry.get())
    entry.delete(0, tk.END)

    if math_operation == "suma":
        result = sumar(first_number, second_number)
    elif math_operation == "resta":
        result = restar(first_number, second_number)
    elif math_operation == "multiplicacion":
        result = multiplicar(first_number, second_number)
    elif math_operation == "division":
        result = dividir(first_number, second_number)

    entry.insert(0, result)

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# Crear la pantalla de entrada
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(window, text="+", padx=39, pady=20, command=button_add)
button_subtract = tk.Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=41, pady=20, command=button_divide)
button_equal = tk.Button(window, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=79, pady=20, command=button_clear)

# Colocar los botones en la ventana
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)

# Iniciar el bucle principal de la aplicación
window.mainloop()