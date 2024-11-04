# train_model.py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Cargar el conjunto de datos Iris
data = load_iris()
X = data.data
y = data.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluar el modelo
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Exactitud del modelo: {accuracy * 100:.2f}%")

# Guardar el modelo entrenado
joblib.dump(model, "iris_model.pkl")
print("Modelo guardado como 'iris_model.pkl'")