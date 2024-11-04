from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Cargar el modelo
model = joblib.load("iris_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Obtener valores de entrada del formulario
    sepal_length = float(request.form["sepal_length"])
    sepal_width = float(request.form["sepal_width"])
    petal_length = float(request.form["petal_length"])
    petal_width = float(request.form["petal_width"])

    # Crear un arreglo para el modelo
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Realizar la predicción
    prediction = model.predict(features)
    species = ["Iris Setosa", "Iris Versicolor", "Iris Virginica"]
    predicted_species = species[prediction[0]]

    # Retornar el resultado como JSON
    return jsonify({"prediction": predicted_species})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)