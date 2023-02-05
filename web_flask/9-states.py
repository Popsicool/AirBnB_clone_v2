#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """display states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, type='1')


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """state by id"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, type='2')
    return render_template('9-states.html', states=state, type='3')


@app.teardown_appcontext
def teardown(self):
    """remove sqlAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
