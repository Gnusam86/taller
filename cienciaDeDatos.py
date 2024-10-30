# Cargar los datos (suponiendo que están en un archivo CSV)
data = pd.read_csv('datos_casas.csv')

# Separar las características (X) y la variable objetivo (y)
X = data[['tamaño']]
y = data['precio']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo (por ejemplo, con el coeficiente de determinación R²)
from sklearn.metrics import r2_score
print('R²:', r2_score(y_test, y_pred))

import joblib

# Guardar modelo
joblib.dump(model, "modelo_knn.pkl")

# Cargar modelo
loaded_model = joblib.load("modelo_knn.pkl")






