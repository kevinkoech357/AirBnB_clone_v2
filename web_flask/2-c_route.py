#!/usr/bin/python3

"""
This file starts a simple
Flask web app
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns
    Hello HBNB when called.
    """
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns
    HBNB when called.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """
    This function returns
    text.
    """
    new_text = text.replace('_', ' ')
    return "C " + new_text


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
