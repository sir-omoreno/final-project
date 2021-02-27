import os
import csv
import requests
import json
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from flask_pymongo import PyMongo

#################################################
# Flask Setup
#################################################

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)

#################################################
# Database Setup
#################################################
# setup mongo connection

app.config["MONGO_URI"] = "mongodb://localhost:27017/base_database"
# app.config["MONGO_URI"] = "mongodb+srv://<dbName>:<password>@cluster0.s0gp3.mongodb.net/rescue_angels_db?retryWrites=true&w=majority"

mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/find_your_scent")
def find_your_scent():
    return render_template("find_your_scent.html")


@app.route("/perfume_info")
def perfume_info():
    return render_template("perfume_info.html")


@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)