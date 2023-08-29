#!/usr/bin/python3
"""
Import from  flask and start a 
a web application"""

from flask import Flask, escape


"""Create the instancce of the app"""
app = Flask(__name__)

"""The route for the homepage"""
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

"""Define a route for /hbnb"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

"""Define a route for /c/<text>"""
@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    text = escape(text).replace('_', ' ')
    return f"C {text}"

""" Define a route for /python/<text>"""
@app.route('/python/<text>', strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def python_is_cool(text):
    return "Python " + escape(text.replace("_", " "))

if __name__ == '__main__':
    # Run the app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)