#!/usr/bin/python3
""" module to import flask """
from flask import Flask, render_template

# Create a flask web application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function to return hello hbnb """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ handles hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ handles c route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False) # defaults case
@app.route('/python/<text>', strict_slashes=False) # case with text
def python_str(text):
    """ handles python route """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """handles /number/n route"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """handles /number_template/n route"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """handles /number_odd_or_even/n route"""
    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
