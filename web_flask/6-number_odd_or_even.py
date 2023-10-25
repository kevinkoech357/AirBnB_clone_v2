#!/usr/bin/python3

"""
This file starts a simple
Flask web app
"""


from flask import Flask, render_template

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
def c_lang(text):
    """
    This function returns
    text.
    """
    new_text = text.replace('_', ' ')
    return "C " + new_text


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    This function returns
    text.
    """
    new_text = text.replace('_', ' ')
    return "Python " + new_text


@app.route('/number/<int:n>', strict_slashes=False)
def show_num(n):
    """
    This function returns if param is int
    number.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_template(n):
    """
    This function renders an html_template
    if n is a number.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    This function renders an html_template
    indicating if n is even or odd provided its of int type.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
