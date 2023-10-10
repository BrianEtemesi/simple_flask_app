#!/usr/bin/env python3
"""
A simple Flask application to display "Hello world".
"""

# Import the Flask module
from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    """
    Show the "Hello world" text when the root URL is accessed.
    """
    return "Hello world"

# Entry point for the application
if __name__ == '__main__':
    # Run the Flask app in debug mode, which provides better error messages
    app.run(debug=True)
