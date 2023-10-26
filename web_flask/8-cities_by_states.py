#!/usr/bin/python3

"""
This file starts a simple Flask web app
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


def get_state_name(state):
    return state.name


@app.route('/cities_by_states', strict_slashes=False)
def list_of_states():
    """
    This function renders an HTML template
    listing all states and their cities available.
    """
    states = storage.all(State).values()
    # states = sorted(states, key=get_state_name)

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
