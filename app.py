from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return "Flask ML App is running on Azure!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]
    prediction = int(sum(features) > 10)

    return jsonify(
        {
            "prediction": prediction,
            "message": "Prediction successful",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)