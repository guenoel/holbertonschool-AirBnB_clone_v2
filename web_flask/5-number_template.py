#!/usr/bin/python3
'''blabla'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web_flask():
    '''blabla comeback'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    return(render_template('5-number.html', n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
