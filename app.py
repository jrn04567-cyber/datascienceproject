from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from datascience.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/train", methods=["GET"])
def training():
    import os
    os.system("python main.py")
    return "Training Successful!"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Reading form data
        fixed_acidity = float(request.form["fixed_acidity"])
        volatile_acidity = float(request.form["volatile_acidity"])
        citric_acid = float(request.form["citric_acid"])
        residual_sugar = float(request.form["residual_sugar"])
        chlorides = float(request.form["chlorides"])
        free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
        total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
        density = float(request.form["density"])
        pH = float(request.form["pH"])
        sulphates = float(request.form["sulphates"])
        alcohol = float(request.form["alcohol"])

        data = [
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol,
        ]

        data = np.array(data).reshape(1, 11)
        columns = [
            "fixed acidity",
            "volatile acidity",
            "citric acid",
            "residual sugar",
            "chlorides",
            "free sulfur dioxide",
            "total sulfur dioxide",
            "density",
            "pH",
            "sulphates",
            "alcohol",
        ]
        df = pd.DataFrame(data, columns=columns)

        pipeline = PredictionPipeline()
        prediction = pipeline.predict(df)

        return render_template("results.html", prediction=str(round(prediction[0], 2)))

    except Exception as e:
        return f"Prediction failed with exception: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)