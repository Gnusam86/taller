#Importar las librerias necesarias
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Cargar el conjunto de datos Iris
iris = load_iris()
data = pd.DataFrame(data=np.c_[iris['data'],iris['target']],columns=iris['feature_names']+['target'])

#Mostrar las primeras filas del conjunto de datos
#print(data.head())

#Dividir los datos en caracteristicas (X) y etiquetas (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

#Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Estandarizar las características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#CONSTRUCCION DEL MODELO
#Importar el clasificador KNN de scikit.learn
from sklearn.neighbors import KNeighborsClassifier

#Inicializar el modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)

#ENTRENAMIENTO DEL MODELO
#Entrenar KNN con los datos de entrenamiento
knn.fit(X_train, y_train)

#Evaluación del modelo con los datos de prueba
accuracy = knn.score(X_test, y_test)
print(f'Precision del modelo:{accuracy*100:.2f}%')

#Predicción y comparacion con las etiquetas reales
y_pred = knn.predict(X_test)
comparison = pd.DataFrame({'Real':y_test,'Prediccion':y_pred})
print(comparison.head())


