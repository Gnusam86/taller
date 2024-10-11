import pandas as pd

#Cargas los datos
ventas_df = pd.read_csv("datos_de_ventas.csv")

#Mostrar las primeras 5 filas
print(ventas_df.head())

#Mostrar las ultimas 3 filas
print(ventas_df.tail(3))

#Obtener informacion sobre las columnas y sus tipos
print(ventas_df.info())

#Calcular estadisticas descriptivas
media_cantidad = ventas_df['Cantidad'].mean()
mediana_cantidad = ventas_df['Cantidad'].median()
desviacion_cantidad = ventas_df['Cantidad'].std()

#Imprimir estadisticas
print(f"Media de Cantidad:{media_cantidad}")
print(f"Mediana de Cantidad:{mediana_cantidad}")
print(f"Desviacion de cantidad:{desviacion_cantidad}")

#Calcular el precio total de cada venta (Cantidad * Precio) y agregarlo como una nueva columna "Total"
ventas_df['Total'] = ventas_df['Cantidad']*ventas_df['Precio']
print(ventas_df.head(5))

#Crear un nuevo dataframe que contenga solo las ventas del producto
camisetas_df = ventas_df[ventas_df['Producto']=='Camiseta']
print(camisetas_df.head(5))

#Ordenar el Dataframe original por la columna "TOtal" en orden descendente
ventas_df_ordenado = ventas_df.sort_values(by = 'Total',ascending=False)
print(ventas_df_ordenado.head())