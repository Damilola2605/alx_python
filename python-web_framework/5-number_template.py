"""
This script creates a simple Flask web application.
"""

from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """
    This function defines the route '/' which displays "Hello HBNB!".

    Returns:
        str: The string "Hello HBNB!" which is displayed in the browser.
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function defines the route '/hbnb' which displays "HBNB".

    Returns:
        str: The string "HBNB" which is displayed in the browser.
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    This function defines the route '/c/<text>' which displays "C " followed by the value of the text variable.

    Returns:
        str: The string "C " followed by the text value, with underscores replaced by spaces.
    """
    return "C " + escape(text.replace("_", " "))

@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    This function defines the route '/python/' and '/python/<text>' which displays "Python " followed by the
    value of the text variable.

    Returns:
        str: The string "Python " followed by the text value, with underscores replaced by spaces.
    """
    return "Python " + escape(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    This function defines the route '/number/<n>' which displays "<n> is a number" if n is an integer.

    Returns:
        str: The string "<n> is a number" if n is an integer.
    """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    This function defines the route '/number_template/<n>' which displays an HTML page with the H1 tag
    "Number: n" inside the BODY tag.

    Returns:
        render_template: Renders the HTML template with the H1 tag displaying "Number: n".
    """
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)