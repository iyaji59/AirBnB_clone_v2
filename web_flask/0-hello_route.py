#!/usr/bin/python3
""" module to import flask """
from flask import Flask
# Create a flask web application
app = Flask(__name__)

@app.route('/', 
