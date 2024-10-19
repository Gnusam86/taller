import pandas as pd
import matplotlib.pyplot as plt

# Crea un DataFrame con los datos proporcionados
data = {
    'Ciudad': ['Acapulco', 'Acapulco', 'Acapulco', 'Monterrey', 'Monterrey', 'Monterrey', 'Guadalajara', 'Guadalajara', 'Guadalajara'],
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo'],
    'Temperatura': [25, 28, 30, 15, 18, 22, 18, 20, 25]
}
df = pd.DataFrame(data)

# Calcula la temperatura media de cada ciudad
mean_temp = df.groupby('Ciudad')['Temperatura'].mean()

# Define una función lambda para convertir Celsius a Fahrenheit
celsius_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32

# Aplica la función lambda a la columna `Temperatura`
df['Temperatura_Fahrenheit'] = df['Temperatura'].apply(celsius_to_fahrenheit)

# Define una función para graficar las temperaturas de una ciudad dada
#El primer argumento es df y representa el dataframe que contiene las temperaturas
#La segunda linea filtra el dataframe para obtener solo las filas de una ciudad
def plot_city_temps(df, city, title='Temperaturas Mensuales', xlabel='Mes', ylabel='Temperatura (°C)', color='blue'):
    city_data = df[df['Ciudad'] == city]
    plt.figure(figsize=(8, 6))
    plt.plot(city_data['Mes'], city_data['Temperatura'], marker='o', linestyle='-', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Genera un gráfico de barras que compara las temperaturas medias de las tres ciudades
plt.figure(figsize=(8, 6))
plt.bar(mean_temp.index, mean_temp.values, color=['blue', 'green', 'red'])
plt.title('Temperatura Media por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Temperatura (°C)')
plt.grid(axis='y')
plt.show()

# Genera gráficos de línea para cada ciudad
plot_city_temps(df, 'Acapulco', color='red')
plot_city_temps(df, 'Monterrey', color='green')
plot_city_temps(df, 'Guadalajara', color='blue')