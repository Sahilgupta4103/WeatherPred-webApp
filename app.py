import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# create the flask app
weatherpredapp = Flask(__name__)


# load the pickle model
model = pickle.load(open("model.pkl", "rb"))


# defining the homepage
@weatherpredapp.route("/")  # app will take you to homepage
def Home():
    return render_template("index.html")


# defining the predict page
@weatherpredapp.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template(
        "index.html",
        prediction_text="The weather of your city is {}".format(prediction),
    )


if __name__ == "__main__":
    weatherpredapp.run(debug=True)
