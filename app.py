from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "CFD predictor is running!"

@app.route("/predict")
def predict():
    result = {
        "velocity": 3.14,
        "pressure_drop": 12.5,
        "status": "success"
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
