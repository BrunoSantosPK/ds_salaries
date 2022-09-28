import os
from dotenv import load_dotenv
from flask import Flask, render_template
from src.controllers.predict import ControllerPredict


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(f"{BASE_PATH}/config/.env")
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    return ControllerPredict.predict(BASE_PATH)
