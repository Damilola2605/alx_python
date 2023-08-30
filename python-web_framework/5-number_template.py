"""
This script creates a simple Flask web application.
"""

from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """
    This function defines the route '/' which displays "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function defines the route '/hbnb' which displays "HBNB".
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    This function defines the route '/c/<text>' which displays "C " followed by the value of the text variable.
    """
    return "C " + escape(text.replace("_", " "))

@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    This function defines the route '/python/' and '/python/<text>' which displays "Python " followed by the
    value of the text variable.
    """
    return "Python " + escape(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    This function defines the route '/number/<n>' which displays "<n> is a number" if n is an integer.
    """
    return "{} is a number".format(n)

"""This function links an html file."""
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template("5-number.html", n=n)
    else:
        return "Invalid input. Please provide an integer."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)