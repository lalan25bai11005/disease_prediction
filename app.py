from flask import Flask, render_template, request
import pickle
import numpy as np
import os

if not os.path.exists("model.pkl"):
    raise Exception("Model not trained. Run train.py first.")

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        int(request.form["fever"]),
        int(request.form["cough"]),
        int(request.form["headache"]),
        int(request.form["fatigue"]),
        int(request.form["body_pain"]),
        int(request.form["age"])
    ]

    prediction = model.predict([features])[0]

    return render_template("index.html", result=prediction)

if __name__ == "__main__":
    app.run(debug=True)
