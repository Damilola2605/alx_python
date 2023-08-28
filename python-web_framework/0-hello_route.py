#!/usr/bin/python3
"""
Import from  flask and start a 
a web application"""

from flask import Flask


"""Create the instancce of the app"""
app = Flask(__name__)

"""The route for the homepage"""
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB"

if __name__ == '__main__':
    # Run the app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)