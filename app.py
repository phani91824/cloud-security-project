from flask import Flask, request, jsonify
from flask_cors import CORS

from detector import detect_sensitive_data, calculate_risk

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Sensitive Data Exposure Detector is running"
    })


@app.route("/detect", methods=["POST"])
def detect():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Please provide text"
        }), 400

    text = data["text"]

    results = detect_sensitive_data(text)

    risk = calculate_risk(results)

    return jsonify({
        "risk": risk,
        "count": len(results),
        "detected_data": results
    })


if __name__ == "__main__":
    app.run(debug=True)