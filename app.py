import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# create the flask app
app = Flask(__name__)


# load the pickle model
model = pickle.load(open("model.pkl", "rb"))


# defining the homepage
@app.route("/")  # app will take you to homepage
def ome():
    return render_template("index.html")


# defining the predict page
@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    print(features)
    if prediction == 0:
        prediction = "Drizzle"
    elif prediction == 1:
        prediction = "Foggy"
    elif prediction == 2:
        prediction = "Rain"
    elif prediction == 3:
        prediction = "Snow"
    elif prediction == 4:
        prediction = "Sunny"

    return render_template(
        "index.html",
        prediction_text="The weather of your city is {}".format(prediction),
    )


if __name__ == "__main__":
    app.run(debug=True)
