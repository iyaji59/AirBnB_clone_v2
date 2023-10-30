#!/usr/bin/python3
""" module to import flask """
from flask import Flask

# Create a flask web application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function to return hello hbnb """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
