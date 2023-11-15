#!/usr/bin/python3

"""
This file starts a simple
Flask web app
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet_hbnb():
    """
    This function returns
    Hello HBNB when called.
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
