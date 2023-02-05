#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''return Hello HBNB!'''
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''return hbnb'''
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space )'''
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    '''display “Python ” followed by the value of the text
    variable (replace underscore _ symbols with a space )'''
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    ''' display “n is a number” only if n is an integer'''
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_num_template(n=None):
    ''' display a HTML page only if n is an integer:'''
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
