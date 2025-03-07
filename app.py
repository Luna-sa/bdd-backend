from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешает запросы с любого домена

@app.route("/", methods=["GET"])
def home():
    return "Backend is working!"

@app.route("/upload", methods=["POST"])
def upload_file():
    return jsonify({"message": "File received!"})
