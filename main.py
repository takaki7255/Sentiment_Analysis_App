from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import sys
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():
    return render_template("index.html")