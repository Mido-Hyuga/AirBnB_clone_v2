#!/usr/bin/python3
"""
 starts a Flask web application.

 - Your web application must be listening on 0.0.0.0, port 5000
Routes:
        - /: display “Hello HBNB!”
        - /hbnb: display “HBNB”
- You must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def redirect():
    return('HBNB')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
