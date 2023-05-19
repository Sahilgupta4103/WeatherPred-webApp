import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# create the flask app
app = Flask(__name__)

# load the pickle model
model = pickle.load(open("model.pkl", "rb"))


# defining the homepage
@app.route("/")
def home():
    return render_template("index.html")


# defining the predict page
@app.route("/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict():
    input = request.get_json()
    features = [np.array(list(input.values()))]
    prediction = model.predict(features)[0]
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

    return jsonify({"prediction_text": "{}".format(prediction)})


if __name__ == "__main__":
    app.run(debug=True)
