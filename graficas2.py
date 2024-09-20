import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos.csv")

class EstadisticasBasicas:
    """
    Clase para realizar análisis estadísticos básicos y visualización de datos.
    """

    def __init__(self, datos):
        """
        Inicializa la clase con los datos proporcionados.

        Args:
            datos (pandas.DataFrame): Un DataFrame de pandas que contiene los datos a analizar.
        """
        self.datos = datos

    def calcular_media(self, columna):
        """
        Calcula la media (promedio) de una columna numérica.

        Args:
            columna (str): El nombre de la columna numérica.

        Returns:
            float: La media de la columna.
        """
        return self.datos[columna].mean()

    def calcular_mediana(self, columna):
        """
        Calcula la mediana de una columna numérica.

        Args:
            columna (str): El nombre de la columna numérica.

        Returns:
            float: La mediana de la columna.
        """
        return self.datos[columna].median()

    def calcular_moda(self, columna):
        """
        Calcula la moda (valor más frecuente) de una columna.

        Args:
            columna (str): El nombre de la columna.

        Returns:
            list: Una lista que contiene la(s) moda(s) de la columna.
        """
        return self.datos[columna].mode().tolist()

    def mostrar_histograma(self, columna, titulo="Histograma", bins=10):
        """
        Muestra un histograma de una columna numérica.

        Args:
            columna (str): El nombre de la columna numérica.
            titulo (str, optional): El título del histograma. Por defecto es "Histograma".
            bins (int, optional): El número de bins (intervalos) en el histograma. Por defecto es 10.
        """
        plt.figure(figsize=(8, 5))
        plt.hist(self.datos[columna], bins=bins, edgecolor='black')
        plt.title(titulo)
        plt.xlabel(columna)
        plt.ylabel("Frecuencia")
        plt.show()

    def mostrar_boxplot(self, columna, titulo="Boxplot"):
        """
        Muestra un boxplot de una columna numérica.

        Args:
            columna (str): El nombre de la columna numérica.
            titulo (str, optional): El título del boxplot. Por defecto es "Boxplot".
        """
        plt.figure(figsize=(6, 4))
        plt.boxplot(self.datos[columna])
        plt.title(titulo)
        plt.xlabel(columna)
        plt.show()

# Ejemplo de uso con los datos proporcionados:

# Supongamos que `df` es el DataFrame que contiene los datos del archivo "datos.csv"
estadisticas = EstadisticasBasicas(df)

# Calcular y mostrar medidas de tendencia central para la columna "Edad"
media_edad = estadisticas.calcular_media("Edad")
mediana_edad = estadisticas.calcular_mediana("Edad")
moda_edad = estadisticas.calcular_moda("Edad")

print(f"Media de Edad: {media_edad}")
print(f"Mediana de Edad: {mediana_edad}")
print(f"Moda de Edad: {moda_edad}")

# Mostrar un histograma y un boxplot de la columna "Edad"
estadisticas.mostrar_histograma("Edad", titulo="Distribución de Edades")
estadisticas.mostrar_boxplot("Edad")